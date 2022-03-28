# -*- coding: UTF-8 -*-
from justice_bert.segmentation import Segmentation
import re


def raw_process_from_list(doc_context):
    for i in range(0, len(doc_context)):
        doc_context[i] = doc_context[i].strip()
    del doc_context[0:8]
    for line in doc_context:
        if re.match('^审判.+[^，。：；？！“”（）…‘’、(),.:;?!\'\"]$', line):
            del doc_context[doc_context.index(line):len(doc_context)]
            break
    final_doc = []
    seg = Segmentation()
    for line in doc_context:
        if re.match('^[（(].+[）)]$', line):
            final_doc.append(line)
            continue
        tmp = seg.ss.segment(line)
        for t in tmp:
            if len(t.strip()):
                if re.match('[，。：；？！“”（）…‘’、(),.:;?!\'\"]$', t):
                    if re.match('^[^（(].+[）)]$', t) or re.match('^[^“‘].+[”’]$', t):
                        t = t + '。'
                else:
                    t = t + '。'
                final_doc.append(t)
    return final_doc


def raw_process_from_file(path):
    doc_file = open(path, mode='r', encoding='utf-8')
    doc_context = []
    for line in doc_file:
        if len(line.strip()):
            doc_context.append(line.strip())
    doc_file.close()
    final_doc = raw_process_from_list(doc_context)
    return final_doc



# print('Document path: ')
# # doc_path = input()
# doc_file = open('wlq.txt', mode='r',encoding='utf-8')
# doc_context = []
# for line in doc_file:
#     if len(line.strip()):
#         doc_context.append(line.strip())
# doc_file.close()
# del doc_context[0:8]
# for line in doc_context:
#     if re.match('^审判', line) and not re.match('[，。：；？！“”（）…‘’、(),.:;?!\'\"]$', line):
#         del doc_context[doc_context.index(line):len(doc_context)]
#         break
# final_doc = []
# seg = Segmentation()
# for line in doc_context:
#     if re.match('^[（(].+[）)]$', line):
#         final_doc.append(line)
#         continue
#     tmp = seg.ss.segment(line)
#     for t in tmp:
#         if len(t.strip()):
#             if re.match('[，。：；？！“”（）…‘’、(),.:;?!\'\"]$', t):
#                 if re.match('^[^（(].+[）)]$', t) or re.match('^[^“‘].+[”’]$', t):
#                     t = t + '。'
#             else:
#                 t = t + '。'
#             final_doc.append(t)
# for line in final_doc:
#     print(line)
