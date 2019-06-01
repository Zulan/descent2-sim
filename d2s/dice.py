from .rolls import AttackRoll, DefenseRoll, Chance


def blue():
    yield Chance(AttackRoll(fail=True))
    yield Chance(AttackRoll(damage=2, range=2, surge=1))
    yield Chance(AttackRoll(damage=2, range=3))
    yield Chance(AttackRoll(damage=2, range=4))
    yield Chance(AttackRoll(damage=1, range=5))
    yield Chance(AttackRoll(damage=1, range=6, surge=1))


def red():
    yield Chance(AttackRoll(damage=1))
    yield Chance(AttackRoll(damage=2), chances=3)
    yield Chance(AttackRoll(damage=3))
    yield Chance(AttackRoll(damage=3, surge=1))


def yellow():
    yield Chance(AttackRoll(range=1, surge=1))
    yield Chance(AttackRoll(damage=1, range=1))
    yield Chance(AttackRoll(damage=1, range=2))
    yield Chance(AttackRoll(damage=1, surge=1))
    yield Chance(AttackRoll(damage=2))
    yield Chance(AttackRoll(damage=2, surge=1))


def brown():
    yield Chance(DefenseRoll(0), chances=3)
    yield Chance(DefenseRoll(1), chances=2)
    yield Chance(DefenseRoll(2))


def gray():
    yield Chance(DefenseRoll(0))
    yield Chance(DefenseRoll(1), chances=3)
    yield Chance(DefenseRoll(2))
    yield Chance(DefenseRoll(3))


def black():
    yield Chance(DefenseRoll(0))
    yield Chance(DefenseRoll(2), chances=3)
    yield Chance(DefenseRoll(3))
    yield Chance(DefenseRoll(4))
