from typing import Generator
from itertools import product
from collections import defaultdict

from .rolls import Chance, AttackRoll, DefenseRoll, Bonus


def roll_all(attack_dice=(), defense_dice=()) -> Generator[Chance, None, None]:
    for roll_chance in product(*attack_dice, *defense_dice):
        yield sum(roll_chance, Chance())


def roll(attack_dice=(), defense_dice=()) -> Generator[Chance, None, None]:
    rolls = defaultdict(int)
    total = 0
    for roll_chance in roll_all(attack_dice=attack_dice, defense_dice=defense_dice):
        rolls[roll_chance.attack_roll, roll_chance.defense_roll] += roll_chance.chances
        total += roll_chance.chances

    for (attack_roll, defense_roll), chances in rolls.items():
        yield attack_roll, defense_roll, chances / total


def fight(attack_dice, defense_dice, bonus=Bonus(), surge_bonuses=()):
    results = defaultdict(float)
    for attack, defense, chance in roll(attack_dice, defense_dice):
        if attack.fail:
            damage = 0
            # TODO check range!
        else:
            damage = attack.damage + bonus.damage
            shields = defense.shields + bonus.shields
            pierce = bonus.pierce
            surge = attack.surge + bonus.surge

            # TODO pick *best* bonus first
            for surge_bonus in surge_bonuses[:surge]:
                damage += surge_bonus.damage
                pierce += surge_bonus.pierce

            shields = max(shields - pierce, 0)
            damage = max(damage - shields, 0)
        results[damage] += chance

    for damage, chance in results.items():
        yield damage, chance
