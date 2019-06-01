#!/usr/bin/env python3

from d2s import dice, roll

for x in dice.blue():
    print(x)

for attack, defense, chance in roll(
    attack_dice=(dice.blue(), dice.red()), defense_dice=(dice.gray(),)
):
    print(chance, attack, defense)
