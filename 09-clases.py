class OperasBas:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.res = 0

    def suma(self, a, b):
        self.num1 = a
        self.num2 = b
        self.res = self.num1 + self.num2
        print("La suma es:", self.res)

    def resta(self, a, b):
        self.num1 = a
        self.num2 = b
        self.res = self.num1 - self.num2
        print("La resta es:", self.res)


def main():
    obj = OperasBas()
    obj.suma(5, 3)
    obj.resta(5, 3)


if __name__ == "__main__":
    main()
