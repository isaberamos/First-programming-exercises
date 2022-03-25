def soma_matrizes(m1, m2):
    import numbers as np
    m1 = np.array(m1)
    m2 = np.array(m2)
    if m1.shape != m2.shape:
        return False
    else:
        return (m1 + m2).tolist()