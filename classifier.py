class NumberClassifier:
    def __init__(self, number):
        self.number = number

    def is_even(self):
        return self.number % 2 == 0

    def is_odd(self):
        return not self.is_even()

    def classify(self):
        return "even" if self.is_even() else "odd"

if __name__ == "__main__":
    pass
