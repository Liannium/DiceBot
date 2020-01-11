# DiceBot

Commands are in the form (XdY) or (with optional parts surronded by brackets) ([label] XdY [+-Z] [Advantage/Disadvantage])

For example:
user: (4d6)
DiceBot: 4d6: 4+2+5+3 = 14
user: (perception 1d20+3 advantage)
DiceBot: perception 1d20: 14+3 = 17
DiceBot: perception 1d20: 10+3 = 13

Dicebot also distinguishes natural ones and twenties from "dirty" ones and twenties:
user: (1d20)
DiceBot: 1d20: 1 = 1 (natural one)

The command does not have to have its own message:
user: I try to determine if the guard is lying to me (1d20)
Dicebot: 1d20: 4 = 4