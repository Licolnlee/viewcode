# coding=utf-8
import numpy as np
import justice_bert.bdfb_raw_process as bdfb_raw_process
import justice_bert.raw_process as raw_process
import justice_bert.centrality as centrality
import justice_bert.similarity as similarity
from bert_serving.client import BertClient


class Extractor(object):

    def __init__(self, beta=0, lambda1=0.5, lambda2=0.5, n=5):
        self.beta = beta
        self.lambda1 = lambda1
        self.lambda2 = lambda2
        self.n = n

    def extract(self, path, ip='27.155.87.89', port=58059, port_out=59058, is_bdfb=True, is_from_file=False, doc=None):
        if is_from_file:
            if is_bdfb:
                doc = bdfb_raw_process.raw_process_from_file(path)
            else:
                doc_file = open(path, mode='r', encoding='utf-8')
                doc = []
                for line in doc_file:
                    if len(line.strip()):
                        doc.append(line.strip())
                doc_file.close()
        if doc is not None:
            bc = BertClient(ip, port, port_out, show_server_config=True)
            vec = bc.encode(doc)
            bc.close()
            sims = similarity.sims_normalized(vec, self.beta)
            cens = centrality.directed_centrality(sims, self.lambda1, self.lambda2)
            top_n = centrality.get_top_n_indice_doc_order(cens, self.n)
            return top_n
        else:
            return None

    def extract_input(self, doc, ip='27.155.87.89', port=58059, port_out=59058):
        if doc is not None:
            bc = BertClient(ip, port, port_out, show_server_config=True)
            vec = bc.encode(doc)
            bc.close()
            sims = similarity.sims_normalized(vec, self.beta)
            cens = centrality.directed_centrality(sims, self.lambda1, self.lambda2)
            top_n = centrality.get_top_n_indice_doc_order(cens, self.n)
            return doc, top_n
        else:
            return None

    def extract_input_long(self, doc, ip='10.0.0.50', port=5555, port_out=5556):
        if doc is not None:
            bc = BertClient(ip, port, port_out, show_server_config=True)
            doc = raw_process.raw_process_from_list(doc)
            if len(doc) > 120:
                b = 0
                e = 120
                veclist = []
                while b < len(doc):
                    if e < len(doc):
                        vtmp = bc.encode(doc[b:e])
                        veclist.append(vtmp)
                        b = b + 120
                        e = e + 120
                    else:
                        vtmp = bc.encode(doc[b:len(doc)])
                        veclist.append(vtmp)
                        b = b + 120
                        e = e + 120
                vecs = np.array(veclist[0])
                jmp = True
                for vs in veclist:
                    if jmp:
                        jmp = False
                        continue
                    vecs = np.vstack((vecs, np.array(vs)))
            else:
                vecs = bc.encode(doc)
            bc.close()
            print(vecs)
            sims = similarity.sims_normalized(vecs, self.beta)
            print(sims)
            cens = centrality.directed_centrality(sims, self.lambda1, self.lambda2)
            nt = 1
            for c in cens:
                print(c, end='\t')
                if nt == 5:
                    print('\n', end='')
                    nt = 0
                nt = nt + 1
            print('\n', end='')
            top_n = centrality.get_top_n_indice_doc_order(cens, self.n)
            return doc, top_n
        else:
            return None

    def extract_file(self, path, ip='27.155.87.89', port=58059, port_out=59058, is_bdfb=True):
        if is_bdfb:
            doc = bdfb_raw_process.raw_process_from_file(path)
        else:
            doc_file = open(path, mode='r', encoding='utf-8')
            doc = []
            for line in doc_file:
                if len(line.strip()):
                    doc.append(line.strip())
            doc_file.close()
        if doc is not None:
            bc = BertClient(ip, port, port_out, show_server_config=True)
            vec = bc.encode(doc)
            bc.close()
            sims = similarity.sims_normalized(vec, self.beta)
            cens = centrality.directed_centrality(sims, self.lambda1, self.lambda2)
            top_n = centrality.get_top_n_indice_doc_order(cens, self.n)
            return doc, top_n
        else:
            return None
