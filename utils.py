import turtle

bob = turtle.Turtle()
print(bob)

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()


#square(bob, 500)

def polygon(t, n, length):
    angle = 360/n

    for i in range(n):
        t.fd(length)
        t.lt(angle)


polygon(bob, 7, 100)

for i in range(1500):
    print(i)

