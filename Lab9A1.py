# Lab9A1 Calculate the distance between two points
# This program will take an input of two points with their x and y values, and will calculate the distance between them.

import math

class DistanceCalculator(object):
    
    def __init__(self, x1, y1, x2, y2):
        self.firstPointX = x1
        self.firstPointY = y1
        self.secondPointX = x2
        self.secondPointY = y2
        self.distance = 0
        
    def computeDistance(self):
        self.distance = math.sqrt((self.secondPointX - self.firstPointX)**2 + (self.secondPointY-self.firstPointY)**2)

    def __str__(self):
        s = "\nfirst point on X: %0.2f" % self.firstPointX
        s = s + "\nfirst point on Y: %0.2f" % self.firstPointY
        s = s + "\nsecond point on X: %0.2f" % self.secondPointX
        s = s + "\nsecond point on Y: %0.2f" % self.secondPointY
        s = s + "\nDistance Between the points: %0.2f" % self.distance

        return  s

def main():
    x1 = float(input("Please enter the first point on X: "))
    y1 = float(input("Please enter the first point on Y: "))
    x2 = float(input("Please enter the second point on X: "))
    y2 = float(input("Please enter the second point on Y: "))
    result = DistanceCalculator(x1, y1, x2, y2)

    result.computeDistance()

    print(result)
    
if __name__ == "__main__":
    main()
