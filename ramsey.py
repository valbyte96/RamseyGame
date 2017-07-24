'''
Ramsey Games

An opportunity to demonstrate well organized OOP

'''

from graphics import *
from RGraph import *
import math

WIDTH = 500
HEIGHT = 500
N = 3
rads = 6.28319  # 2 pi
R = 100
P = []  # list of points
count = 0

# Edge lists
User = []
Comp = []


def main():
    win = GraphWin('Ramsey', WIDTH, HEIGHT)
    graph = RGraph(N, R, WIDTH / 2, HEIGHT / 2)
    graph.draw(win)

    while True:  # Game loop
        count = 0
        while True:  # user turn
            clickPoint = win.getMouse()
            ans1, n1 = graph.isTouched(clickPoint)
            if ans1:
                while True:
                    clickPoint = win.getMouse()
                    ans2, n2 = graph.isTouched(clickPoint)
                    if ans2:
                        u = []
                        u.append(n1.getID())
                        u.append(n2.getID())
                        u.sort()
                        User.append(u)
                        p1 = n1.getCenter()
                        p2 = n2.getCenter()
                        line = Line(p1, p2)
                        line.setFill('red')
                        line.draw(win)
                        break
                break
        while True:  # Computer's turn
            n1, n2 = graph.getRand()
            c = []
            c.append(n1.getID())
            c.append(n2.getID())
            c.sort()
            count+=1
            if c not in Comp and c not in User:
                Comp.append(c)
                line = Line(n1.getCenter(), n2.getCenter())
                line.setFill('blue')
                line.draw(win)
                break
            elif count>=100:
                break
        if graph.isComplete(User, Comp):
            print("done")
            break


main()
