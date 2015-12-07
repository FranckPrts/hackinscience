
def love_meet(bob, alice):
    return list(set(bob) & set(alice))


def affair_meet(bob, alice, silvester):
    pasbon = set(alice) & set(bob)
    pasbien = set(alice) & set(silvester)
    adultere = pasbien - pasbon
    return(adultere)
