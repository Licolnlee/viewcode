import numpy as np


def sim_pair(v1, v2):
    return np.dot(v1, v2)


def sims(vecs):
    return np.dot(vecs, vecs.T)


def sim_pair_cos(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def sims_cos(vecs):
    dem = len(vecs)
    scores = []
    for i in range(0, dem):
        tmp = []
        for j in range(0, dem):
            if i == j:
                s = 1
            else:
                s = sim_pair_cos(vecs[i], vecs[j])
            tmp.append(s)
        scores.append(tmp)
    return scores


def sims_normalized(vecs, beta=0):
    scores = sims(vecs)
    dem = scores.shape[0]
    min_e = min(map(min, scores))
    for i in range(0, dem):
        scores[i][i] = 0
    max_e = max(map(max, scores))
    threshold = 1 + beta * (max_e - min_e)
    for i in range(0, dem):
        for j in range(0, dem):
            s = scores[i][j]
            s = s - threshold
            # print(s)
            if s > 0:
                scores[i][j] = s
            else:
                scores[i][j] = 0
    return scores

