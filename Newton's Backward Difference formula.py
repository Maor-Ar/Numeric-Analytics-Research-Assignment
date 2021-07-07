"""
 * Authors: Maor Arnon (ID: 205974553) and Neriya Zudi (ID:207073545) and
 *          Matan Ohayon (ID: 311435614) and Matan Sofer (ID: 208491811)
 * Emails: maorar1@ac.sce.ac.il |  neriyazudi@Gmail.com
 *         matan15595m@gmail.com  |  sofermatan123@gmail.com
 * Department of Computer Engineering - Numeric Analytics Research-Assignment
"""

class bcolors:
    ENDC = '\033[0m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def tablePoints(x, y):
    """
    :param x: x values of table points
    :param y: y values of table points, Given as a 2D array so that y values are in the first column
    :return: A list of taples representing the table points
    """
    table = []
    for i in range(len(x)):
        table.append((x[i], y[i][0]))
    return table



def newtonBackward(x, y, n, PointToFind):
    """
    Formula for calculating an approximate value between table points (Interpolation)
      or outside table points (Extrapolation). The function displays calculations until it reaches the final result.
    :param x: x values of table points
    :param y: y values of table points, Given as a 2D array so that y values are in the first column
    :param n:  number of table points
    :param PointToFind: The value we want to find its approximation
    """
    # calculating factorial
    def factorial(a):
        """
        :param a: The number on which we will perform a factorial action
        :return: The result of the calculation a!
        """
        start = 1
        for i in range(2, a + 1):
            start *= i
        return start

    def print1():
        print(bcolors.OKBLUE, "Interpolation & Extrapolation Newton's Backward Difference formula", bcolors.ENDC)
        print(bcolors.OKBLUE, "Table Points", tablePoints(x, y), bcolors.ENDC)
        print(bcolors.OKGREEN, "Finding an approximation to the point ", PointToFind, "\n", bcolors.ENDC)
        print(bcolors.OKBLUE + f"h = (x[1] - x[0]) = {h}" + bcolors.ENDC)
        print(bcolors.OKBLUE + "s = (value - x[n - 1]) / h = " + bcolors.ENDC, s)
        str3 = "y(x) = (yɴ)+ "
        str4 = " "
        for i in range(n - 1):
            str4 = "(∇(" + str(i + 1) + ")*yɴ"
            for j in range(i):
                if j == 0:
                    str4 = str4 + "s"
                str4 = str4 + "(s+" + str(j + 1) + ")"
            if i == n - 2:
                str4 = str4 + "/" + str(i + 1) + "!)"
            else:
                str4 = str4 + "/" + str(i + 1) + "!) + "
            str3 = str3 + str4
        print(bcolors.HEADER + str3 + bcolors.ENDC)
    def print2():
        str2 = ""
        for i in range(n):
            for j in range(i):
                str2 = str2 + "(" + str(s) + "+" + str(j) + ")"
            if i == 0:
                str2 = str2 + str(y[n - 1 - i][0]) + "/" + str(factorial(i)) + "+"
            elif i == n - 1:
                str2 = str2 + "*" + str(y[n - 1 - i][0]) + "/" + str(factorial(i))
            else:
                str2 = str2 + "*" + str(y[n - 1 - i][0]) + "/" + str(factorial(i)) + "+"
        print(bcolors.UNDERLINE + str2 + bcolors.ENDC)
    def print3()  :
        str1 = ""
        if i == 1:
            print(bcolors.WARNING + "P1(" + str(s) + ")" + bcolors.ENDC + "=f5+s∇f5")
            print("yɴ = ", result)
        else:
            if i == n - 1:
                print(
                    bcolors.WARNING + "P" + str(i) + "(" + str(s) + ")=" + bcolors.ENDC + "p" + str(i - 1) + "(" + str(
                        s) + ")-")
            else:
                print(
                    bcolors.WARNING + "P" + str(i) + "(" + str(s) + ")=" + bcolors.ENDC + "p" + str(i - 1) + "(" + str(
                        s) + ")+")
            for j in range(i):
                str1 = str1 + "(" + str(s) + "+" + str(j) + ")"
            if i == 2:
                print("        " + bcolors.FAIL + str1 + "*" + str(y[n - 1][i]) + "/" + str(
                    i) + "! = " + bcolors.ENDC + bcolors.BOLD + str(result) + bcolors.ENDC)
            else:
                print("        " + bcolors.FAIL + str1 + "/" + str(i) + "! = " + bcolors.ENDC + bcolors.BOLD + str(
                    result) + bcolors.ENDC)
            str1 = ""
    # Calculate the defferences
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            y[j][i] = y[j][i - 1] - y[j - 1][i - 1]
    # initializing s and result
    result = y[n - 1][0]
    h = (x[1] - x[0])
    s = round((PointToFind - x[n - 1]) / h, 3)
    result = round(result, 3)
    print1()
    print2()
    #calculate by formula with factorial and y vaulues
    for i in range(1, n):
        t1 = s
        for j in range(1, i):
            t1 = t1* (s + j)
        result = result + (t1 * y[n - 1][i]) / factorial(i)
        result = round(result, 6)
        print3()
    # show  final difference table
    print(bcolors.OKGREEN + "BACKWARD DIFFERENCE TABLE" + bcolors.ENDC)
    print("X  |")
    for i in range(n):
        print(x[i], end="|\t")
        for j in range(i + 1):
            print(bcolors.OKBLUE, y[i][j], end="\t" + bcolors.ENDC)
        print("")

    print(bcolors.BOLD + "The approximation of the point", PointToFind, "is", str(result), bcolors.ENDC)



##input and call main function
n=int(input(bcolors.BOLD+"Please enter number of X,Y Points  "))
x=[]
y = []
for q in range(n):
    y.append([])
    for m in range(n):
        y[q].append(0)
for i in range(n):
    xi = float(input(bcolors.BOLD+"Please enter value of X"+ str(i+1)+" " +bcolors.ENDC))
    if i > 1:
        while round(x[1]-x[0],3) != round(xi-x[i-1],3):
            print(bcolors.FAIL, "must have ordinary differences.",bcolors.ENDC)
            xi = float(input(bcolors.BOLD + "Please enter value of X" + str(i + 1) +" "+ bcolors.ENDC))
    x.append(xi)

for i in range(n):
    yi = float(input(bcolors.BOLD+"Please enter value of Y"+ str(i+1)+" " +bcolors.ENDC))
    y[i][0] = yi
value = float(input(bcolors.BOLD+"Please select the point value you want to find "+bcolors.ENDC))
newtonBackward(x, y, n, value)
