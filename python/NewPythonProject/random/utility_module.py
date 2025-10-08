class Number_Stats():
    def __init__(self,numbers):
        self.numbers = numbers


    def find_max (self):
        Big_one = self.numbers[0]
        for number in self.numbers:
            if number > Big_one:
                Big_one = number

        return Big_one