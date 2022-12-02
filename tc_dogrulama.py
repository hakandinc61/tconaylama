def Tc(value=22205128594):
    value=str(value)

    if not len(value)==11:
        return False

    if not value.isdigit():
        return False

    if int(value[0])==0:
        return False

    digits=[int(d) for d in str(value)]

    if not sum(digits[:10])%10==digits[10]:
        return False

    if not(((7*sum(digits[:9][-1::-2]))-sum(digits[:9][-2::-2]))%10)==digits[9]:
        return False

    return True
