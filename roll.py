import random


class Roll:
    """a class to represent a roll of a/some dice/die"""
    total = 0
    dice = 1
    faces = 0
    modifier = 0
    output = ''
    modifiersign = ''
    rolls = []
    is1d20 = False
    isNat1 = False
    isNat20 = False
    hasModifier = False

    def __init__(self, output: str, dice: int, faces: int, modifiersign: str, modifier: int):
        """initializes a roll object"""
        if output:
            self.output = output
        if dice:
            self.dice = dice
        self.faces = faces
        if self.dice == 1 and self.faces == 20:
            self.is1d20 = True
        self.output += str(self.dice) + 'd' + str(self.faces)
        if modifiersign != '' and modifier != 0:
            self.modifiersign = modifiersign
            self.modifier = modifier
            self.hasModifier = True
            self.output += modifiersign + str(modifier)
        self.output += ': '

    def rolldice(self):
        """returns a list of results based on the dice code and the number of dice passed"""
        for i in range(0, self.dice):
            self.rolls.insert(i, random.randint(1, self.faces))

    def sumrolls(self):
        """Takes the sum of all the rolls and configures the output"""
        for i in range(0, len(self.rolls)):
            roll = self.rolls.pop()
            self.total += roll
            if 0 != i:
                self.output += '+'
            self.output += ' ' + str(roll) + ' '

    def checknaturals(self):
         if self.total == 1:
            self.isNat1 = True
         if self.total == 20:
            self.isNat20 = True

    def handlemodifiers(self):
        """Handles the modifier, if one has been specified"""
        if self.modifiersign == '+':
            self.total += self.modifier
            self.output += '+ ' + str(self.modifier)
        elif self.modifiersign == '-':
            self.total -= self.modifier
            self.output += '- ' + str(self.modifier)

    def getfinalstring(self) -> str:
        """gets the final version of the output string"""
        self.output += " = " + str(self.total)
        if self.isNat1:
            self.output += ' _(NATURAL 1)_'
        elif self.isNat20:
            self.output += ' _(NATURAL 20)_'
        return self.output

    def gettotal (self) -> int:
        return self.total
