import matplotlib.pyplot as plt

X = []
Y = []
XY = []
X2 = []
y = []

#taking inputs of n, X and Y
n = int(input("Enter n:"))

for i in range(0, n): 
    ele = float(input("Enter value of X:"))
    X.append(ele)


for i in range(0, n): 
    ele = float(input("Enter value of Y:"))
    Y.append(ele)
    
#calculating attributes
for i in range(0, n):   
    XY.append(X[i] * Y[i])
    X2.append((X[i]) ** 2 )

#total of all attributes
sX = sum(X)
sY = sum(Y)
sXY = sum(XY)
sX2 = sum(X2)

#calculation of a and b
a = ((n*sXY) - (sX*sY)) / ((n*sX2) - (sX)**2)
b = (sY - (a*sX))/n

for i in range(0, n): 
    y.append((a*X[i])+b)

print(X,"total =",sX)
print(Y,"total =",sY )
print(XY,"total =",sXY)
print(X2,"total =",sX2)
print("\na =", a ,"\nb =", b)
print("\n",y)

choice = int(input("What do you want to do?\n1. Plot graph\n2. Predict values of Y for X\n3. Both 1 and 2\n4.Exit\n"))
if choice == 1:
    plt.scatter(X, y, color = "green", s=30)
    plt.scatter(X, Y, color = "blue", s=30)
    plt.plot(X, y, color = "grey")
    plt.xlabel('X') 
    plt.ylabel('Y')
    plt.legend(["Regression Line","Predicted","Actual"])
    plt.show

elif choice == 2:
    x = float(input("Enter the value of X to predict the op: "))
    print("For X = ",x," Y = ", ((a*x)+b))

elif choice ==3:
    x = float(input("Enter the value of X to predict the op: "))
    yy = (a*x)+b
    print("For X = ",x," Y = ", (yy))

    plt.scatter(X, y, color = "green", s=30)
    plt.scatter(X, Y, color = "blue", s=30)
    plt.plot(X, y, color = "grey")
    plt.xlabel('X') 
    plt.ylabel('Y')
    plt.legend(["Regression Line","Predicted","Actual"])
    plt.show

else:
    print("Invalid option")