Line1=input().split()
x1=float(Line1[0])
y1=float(Line1[1])
Line2=input().split()
x2=float(Line2[0])
y2=float(Line2[1])
Distance=((x2-x1)**(2)+(y2-y1)**(2))**(1/2)
print('{:.4f}'.format(Distance))