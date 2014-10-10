import numpy as np


def pagerank(G, beta, epsilon=1.e-9):
    '''
    # Lecture example, https://class.coursera.org/mmds-001/lecture/27, 12mins
    >>> G = np.array([[1,1,0],[1,0,0],[0,1,1]])
    >>> pagerank(G, 0.8)
    array([ 0.21212121,  0.15151515,  0.63636364])

    # Week 1 Homework Q1
    >>> G = np.array([[0,0,0],[1,0,0],[1,1,1]])
    >>> pagerank(G, 0.7)
    array([ 0.1  ,  0.135,  0.765])

    '''
    N = G.shape[0]
    d = G.sum(axis=0)

    r = np.zeros(N) + 1./N
    rnew = np.zeros(N) + 1./N

    while True:
        rprime = np.zeros(N)

        for i in range(N):
            for j in range(N):
                if G[i][j] != 0:
                    rprime[i] += beta * r[j]/d[j]

        S = rprime.sum()

        # reinsert leaked PageRank
        for i in range(N):
            rnew[i] = rprime[i] + (1 - S)/N

        if np.sum(np.abs(rnew - r)) < epsilon:
            break
        else:
            r = rnew * 1.0
        print N * r

    return r


if __name__ == "__main__":
    import doctest
    doctest.testmod()
