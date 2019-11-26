import random

#Creating 2d arrays a and b
rows,cols = (10,10)
a = [[0 for i in range(cols)] for j in range(rows)]
rows,cols = (10,10)
b = [[0 for i in range(cols)] for j in range(rows)]

#This is to print and add x to an 2d array b
for i in range(10):
    for j in range(10):
        b[i][j]="x"
        print ("x ",end="")
    print()
print("Starting cell is (0,0)")
print()
elements = ["0","@"]
point = 0
flag = 0
key = 0

#Adding random elements to array a
for i in range(10):
    for j in range(10):
        a[i][j] = random.choice(elements)

#gathers how many 0s are there in the array for the loop limit
for i in range(10):
    for j in range(10):
        if (a[i][j]=="0"):
            key += 1

#Game body
for k in range(key+1):
    if (k!=key and flag == 0):
        x = int(input("Enter position (x,y) : "))                       #user input ( starting cell is (0,0) )
        y = int(input())                                                #also note that after typing value for 'x' press enter for adding value to 'y'
        for i in range(10):
            for j in range(10):
                if (x==i and y==j):
                    if (a[i][j] == "@"):                                #check whether it has '@' element
                        for i in range(10):
                            for j in range(10):
                                if (x==i and y==j):
                                    print (a[x][y],"",end="")
                                else:
                                    print (a[i][j],"",end="")
                            print()
                        print("GAME OVER! Your points = ",point)
                        flag = 1                                        #To stop loop
                        break
                    elif (a[i][j] == "0"):                              #check whether it has '0' element
                        point += 1
                        for i in range(10):
                            for j in range(10):
                                if (x==i and y==j):
                                    b[i][j]="0"
                                    if(k==key-1):                       #used to check whether it is the last one and prints the array of a
                                        for i in range(10):
                                            for j in range(10):
                                                print(a[i][j],"",end="")
                                            print()
                                    else:
                                        for i in range(10):                 #uses b array to update the cells for each user input
                                            for j in range(10):
                                                print(b[i][j],"",end="")
                                            print()
    elif (flag == 1):                                                     #triggers when @ are opened
        break
    else:
        print("You win! Points = ",point)
