class AttackRoll:
    def __init__(self, damage=0, surge=0, range=0, fail=False):
        self.damage = damage
        self.surge = surge
        self.range = range
        self.fail = fail

    def __add__(self, other):
        assert isinstance(other, AttackRoll)
        return AttackRoll(
            damage=self.damage + other.damage,
            surge=self.surge + other.surge,
            range=self.range + other.range,
            fail=self.fail or other.fail,
        )

    def __eq__(self, other):
        assert isinstance(other, AttackRoll)
        if self.fail or other.fail:
            return self.fail == other.fail
        return (
            self.damage == other.damage
            and self.surge == other.surge
            and self.range == other.range
        )

    def __hash__(self):
        if self.fail:
            return hash(True)
        return hash((self.damage, self.surge, self.range))

    def __str__(self):
        if self.fail:
            return "[✖]"

        s = "[{}↦".format(self.range)
        if self.damage:
            s += ",{}♥".format(self.damage)
        if self.surge:
            s += "," + ("↯" * self.surge)
        s += "]"
        return s


class DefenseRoll:
    def __init__(self, shields=0):
        self.shields = shields

    def __add__(self, other):
        assert isinstance(other, DefenseRoll)
        return DefenseRoll(shields=self.shields + other.shields)

    def __str__(self):
        if self.shields == 0:
            return "()"
        if self.shields == 1:
            return "(🛡)"
        return f"({self.shields}🛡)"

    def __eq__(self, other):
        assert isinstance(other, DefenseRoll)
        return self.shields == other.shields

    def __hash__(self):
        return hash(self.shields)


class Bonus:
    def __init__(self, damage=0, range=0, pierce=0, shields=0, surge=0):
        self.damage = damage
        self.range = range
        self.pierce = pierce
        self.shields = shields
        self.surge = surge


class Chance:
    def __init__(
        self, roll=None, attack_roll=AttackRoll(), defense_roll=DefenseRoll(), chances=1
    ):
        if roll is not None:
            if isinstance(roll, AttackRoll):
                attack_roll = roll
            else:
                assert isinstance(roll, DefenseRoll)
                defense_roll = roll

        self.attack_roll = attack_roll
        self.defense_roll = defense_roll
        self.chances = chances

    def __add__(self, other):
        assert isinstance(other, Chance)
        return Chance(
            attack_roll=self.attack_roll + other.attack_roll,
            defense_roll=self.defense_roll + other.defense_roll,
            chances=self.chances * other.chances,
        )

    def __str__(self):
        return "{} x {}, {}".format(self.chances, self.attack_roll, self.defense_roll)
