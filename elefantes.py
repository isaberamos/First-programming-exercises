def incomodam(n: int) -> str:
    mstr = ""
    if n > 0:
        mstr += "incomodam "
        return mstr + incomodam(n-1)
    return mstr


def elefantes(n: int, max=None) -> str:
    if not max:
        max, n = n, 2

    if n <= max:
        if n == 2:
            mstr = "Um elefante incomoda muita gente\n"
            mstr += "{} elefantes {}muito mais\n".format(n, incomodam(n))
        else:
            mstr = "{} elefantes {}muito mais\n".format(n, incomodam(n))

        if n < max:
            mstr += "{} elefantes incomodam muita gente\n".format(n)

        return mstr + elefantes(n+1, max)

    return ""