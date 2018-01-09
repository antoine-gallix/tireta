def is_in(A, B):
    """test if a dict is a sub-dict of another

    return True if all key/value pairs of A are in B
    """

    try:
        sub = {k: B[k] for k in A}
        return A == sub
    except KeyError:
        return False
