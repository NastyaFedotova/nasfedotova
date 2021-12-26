from lab_python_oop.FigureColor import FigureColor
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Square import Square
from lab_python_oop.Circle import Circle
import pygame

def main():
    pygame.init()
    rectangle = Rectangle(19, 19, FigureColor(0, 0, 255))
    square = Square(19, FigureColor(0, 255, 0))
    circle = Circle(19, FigureColor(255, 0, 0))
    print()
    square.Repr()
    rectangle.Repr()
    circle.Repr()
    print()

if __name__ == "__main__":
    main()
