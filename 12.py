print('Введите Xbeg, Xend и Dx')
xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))
print("Xbeg={0: 7.2f} Xend={1: 7.2f}".format(xb, xe))
print(" Dx={0: 7.2f}".format(dx))
xt = xb
print("+--------+--------+")
print("I X I Y I")
print("+--------+--------+")
while xt <= xe:
    if xt >= -10 and xt < -6:
        y=2-((4-(xt+8)**2)**0.5)
    if xt >= -6 and xt < -4:
        y=2
    if xt >= -4 and xt < 2:
        y=-(1/2)*xt
    if xt >= 2 and xt <= 4:
        y=1*xt
    else:
        y=None
    if y not None:
        print("I{0: 7.2f} I{1: 7.2f} I".format(xt, y))
        xt += dx
print("+--------+--------+")
