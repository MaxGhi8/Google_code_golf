def p(g):
    for r, row in enumerate(g):
        for c, color in enumerate(row):
            if r and c and color == 5 and g[r - 1][c - 1] not in [0, 5]:
                g[r][c] = 0
    return g

