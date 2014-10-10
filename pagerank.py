import numpy as np


def pagerank(G, beta, epsilon=1.e-9):
    N = G.shape[0]
    d = G.sum(axis=0)

    r = np.zeros(N) + 1./N
    rnew = np.zeros(N) + 1./N

    while True:
        rprime = np.zeros(N)
        for j in range(N):
            for i in range(N):
                if G[j][i] != 0:
                    rprime[j] += beta * r[i]/d[i]

        S = rprime.sum()

        # reinsert leaked PageRank
        for j in range(N):
            rnew[j] = rprime[j] + (1 - S)/N

        if np.sum(np.abs(rnew - r)) < epsilon:
            break
        else:
            r = rnew * 1.0

    return r
