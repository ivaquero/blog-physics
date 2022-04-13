def stability_2D(eigen_values):

    eig1, eig2 = tuple(eigen_values)
    stability = np.zeros(5)
    if im(eig1) < 10**-10 and im(eig2) < 10**-10:
        if eig1 < 0 and eig2 < 0:
            stab_type = "Stable node"
            stability[0] = 1
        elif eig1 > 0 and eig2 > 0:
            stab_type = "Unstable node"
            stability[1] = 1
        else:
            stab_type = "Saddle point"
            stability[2] = 1
    elif re(eig1) < 0:
        stab_type = "Stable spiral"
        stability[3] = 1
    else:
        stab_type = "Unstable spiral or limit cycle"
        stability[4] = 1
    return stab_type, stability
