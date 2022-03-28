# -*- coding: UTF-8 -*-
from justice_bert.segmentation import Segmentation
import re

print('Document path: ')
# doc_path = input()
doc_file = open('wlq.txt', mode='r',encoding='utf-8')
doc_context = []
for line in doc_file:
    if len(line.strip()):
        doc_context.append(line.strip())
del doc_context[0:8]
for line in doc_context:
    if re.match('^审判', line) and not re.match('[，。：；？！“”（）…‘’、(),.:;?!\'\"]$', line):
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
for line in final_doc:
    print(line)
