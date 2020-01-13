# DiceBot

Commands are in the form (XdY) or (with optional parts surronded by brackets) ([label] XdY [+-Z] [Advantage/Disadvantage])

For example: <br/>
user: (4d6)<br/>
DiceBot: 4d6: 4+2+5+3 = 14<br/>
user: (perception 1d20+3 advantage)<br/>
DiceBot: perception 1d20: 14+3 = 17<br/>
DiceBot: perception 1d20: 10+3 = 13<br/>

Dicebot also distinguishes natural ones and twenties from "dirty" ones and twenties:<br/>
user: (1d20)<br/>
DiceBot: 1d20: 1 = 1 (natural one)<br/>

The command does not have to have its own message:<br/>
user: I try to determine if the guard is lying to me (1d20)<br/>
Dicebot: 1d20: 4 = 4<br/>

This bot can be added to servers by visiting https://discordapp.com/api/oauth2/authorize?client_id=634827162137919508&permissions=67584&scope=bot

if you find any bugs, let me know by messaging me on Discord at MidnightDreary#3593