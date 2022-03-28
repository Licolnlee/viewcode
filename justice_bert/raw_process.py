# -*- coding: UTF-8 -*-
from justice_bert.segmentation import Segmentation
import re


def raw_process_from_list(doc_context):
    for i in range(0, len(doc_context)):
        doc_context[i] = doc_context[i].strip()
    i = 0
    to_be_del = []
    for line in doc_context:
        if i < 8:
            i = i + 1
            if re.match('^.+[^,.?!:;\'\"，。？！：；‘’“”]$', line):
                to_be_del.append(line)
                # del doc_context[doc_context.index(line)]
        else:
            break
    for d in to_be_del:
        doc_context.remove(d)
    for line in doc_context:
        if re.match('^审.+[^，。：；？！“”（）…‘’、(),.:;?!\'\"]$', line):
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
