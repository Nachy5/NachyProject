# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('bro')
    print (2**4)
    print (18%6)
print(2*5**2)
growth_multiplier = 1.1
savings = 100
result=savings*growth_multiplier**7
print(result)
Desc='compound interest'
profitable=True
Year1= growth_multiplier*savings
print(type(Year1))
Doubledesc= Desc+Desc
print(Doubledesc)
#Joining Multiple values
#You have to convert them to strings str() or floats Float() or integers int()
print(int(result) + int(savings))
print("I started with $") + str(savings) + "and now have $" +str(result) + "Awesome!")
pi_string= "3.1415926"
pi_float= float(pi_string)
