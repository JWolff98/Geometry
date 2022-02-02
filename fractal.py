import turtle
import math

def hilbertCurve(n, w, l):
    div = 2**(n+1)
    c1 = (122/255, 55/255, 231/255)
    c2 = (80/255, 244/255, 253/255)
    h = turtle.Turtle()
    h.hideturtle()
    h.speed(0)
    turtle.colormode(1)
    h.up()
    h.radians()
    #h.pencolor(255, 255, 255)
    h.setpos(w/(2*div) - w/2, l/(2*div) - l/2)
    h.down()

    A = "-B0F+A0FA0+FB0-"
    B = "+A0F-B0FB0-FA0+"

    res = B

    for i in range(n):
        A = A.replace(f"A{i}", f"A{i+1}").replace(f"B{i}", f"B{i+1}")
        B = B.replace(f"A{i}", f"A{i+1}").replace(f"B{i}", f"B{i+1}")
        res = res.replace(f"A{i}", A).replace(f"B{i}", B)

    res = res.replace(f"A{n}", "").replace(f"B{n}", "")
    delta = [(c - c1[index]) /(len(res)) for index, c in enumerate(c2)]
    j = 0
    for instruction in res:
        h.pencolor([(c1[i] + d*j) % 1 for i, d in enumerate(delta)])
        if instruction == "F":
            h.forward(w/div) if ((h.heading() == 0) or (h.heading() == math.pi)) else h.forward(l/div)
        elif instruction == "+":
            h.left(math.pi/2)
        elif instruction == "-":
            h.right(math.pi/2)
        j += 1
if __name__ == "__main__":
    sc = turtle.Screen()
    sc.setup(600, 600)
    sc.bgcolor(0, 0, 0)
    sc.colormode(255)

    n = int(input("Enter an integer value: "))
    hilbertCurve(n, 500, 500)
    turtle.done()

