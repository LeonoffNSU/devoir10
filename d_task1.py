class Circle:
    all_circles = []
    pi = 3.1415

    def __init__(self, r=1):
        self.__r = r
        Circle.all_circles.append(self)

    def area(self):
        return Circle.pi * self.__r ** 2

    @staticmethod
    def total_area():
        total = 0
        for circle in Circle.all_circles:
            total += circle.area()
        return total
