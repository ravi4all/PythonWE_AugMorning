import turtle

turt = turtle.Pen()
turt.shape('turtle')
turt.color('red')

##for i in range(4):
##    turt.forward(200)
##    turt.left(90)
##
##turt.left(180)
##
##for i in range(5):
##    turt.backward(200)
##    turt.right(90)

for i in range(10):
    turt.circle(5*i)
    turt.forward(10)
