import numpy as np

def border_weight(i, n, alpha=1):
    tmp = n - i + 1
    tmp = alpha * tmp
    if i < tmp:
        return i
    else:
        return tmp


def undirected_centrality(scores):
    cent = []
    dem = scores.shape[0]
    for i in range(0, dem):
        c = 0
        for j in range(0, dem):
            if i == j:
                continue
            else:
                c = c + scores[i][j]
        cent.append(c)
    return cent


def directed_centrality(scores, lambda1=0.5, lambda2=0.5):
    cent = []
    dem = scores.shape[0]
    for i in range(0, dem):
        c1 = 0
        c2 = 0
        c = 0
        for j in range(0, dem):
            if i == j:
                continue
            elif j < i:
                c1 = c1 + scores[i][j]
            else:
                c2 = c2 + scores[i][j]
        c = lambda1 * c1 + lambda2 * c2
        cent.append(c)
    return cent


def directed_centrality_border(scores, lambda1=0.5, lambda2=0.5, alpha=1):
    cent = []
    dem = scores.shape[0]
    for i in range(0, dem):
        c1 = 0
        c2 = 0
        c = 0
        for j in range(0, dem):
            if i == j:
                continue
            elif border_weight(j, dem, alpha) < border_weight(i, dem, alpha):
                c1 = c1 + scores[i][j]
            else:
                c2 = c2 + scores[i][j]
        c = lambda1 * c1 + lambda2 * c2
        cent.append(c)
    return cent


def to_dict(cent):
    cent_dict = {}
    for i in range(0, len(cent)):
        cent_dict[i] = cent[i]
    return cent_dict


def get_top_n_indice(cent, n=5):
    a = np.array(cent)
    n = 0 - n
    f = a.argsort()[n:][::-1]
    return f


def get_top_n_indice_doc_order(cent, n=5):
    f = get_top_n_indice(cent, n)
    return sorted(f)