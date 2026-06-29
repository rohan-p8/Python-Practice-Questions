class calculator:

    def cal(self, n):
        self.n = n

        sqr = n * n
        print(f"Square of {n} is: {sqr}")

        cube = n * n * n
        print(f"Cube of {n} is: {cube}")

        root = n ** 0.5
        print(f"Square root of {n} is: {root}")


    @staticmethod
    def greet():
        print("\nHello Rohan !!! Welcome to Python programming.")

c1 = calculator()
c1.cal(4)
c1.greet()