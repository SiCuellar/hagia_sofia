def identical(L1, L2):
    # index = 0
    if L1 != L2:
        return False
    elif L1[0] and L1[0] == L2[0]:
        # index += 1
        identical(L1[1:],L2[1:])

    # import code;/ code.interact(local=dict(globals(), **locals()))
    else:
        return True
