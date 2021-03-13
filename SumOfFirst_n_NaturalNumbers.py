# SumOfCubesPythonProgram
#Python Program for cube sum of first n natural numbers
# First, we need to define our function
#The aim is to return sum of series, after the use does makes an input
def SumOfSeries(naturalNumber):
    sum = 0
    for i in range(1, int(naturalNumber) +1):   # This is important to ensure successful concatenation
        sum += i*i*i                            # A cube is a number multiplied by itself thrice, hence i*i*i
    return sum

# In this case, we need to ensure the user does an input
# We apply the input function
naturalNumber = input("Enter Natural Number:: ")
print("The Sum of the First n Natural numbers is:: ", SumOfSeries(naturalNumber))