
class TwoDVector:

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"TwoDVector: i={self.i}, j={self.j}")

class ThreeDVector(TwoDVector):

    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"ThreeDVector: i={self.i}, j={self.j}, k={self.k}")


a = TwoDVector(3,5)
a.show()

b = ThreeDVector(8, 5,1)
b.show()