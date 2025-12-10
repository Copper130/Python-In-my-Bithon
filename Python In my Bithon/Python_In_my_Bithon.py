import os
import time

def cls():# Clears Screen planning to have it run between sections
    os.system('cls')

greeting = "Hello, This is a Python testing ground!"
i = 1
number_of_loops = 5
print(greeting)
for i in range(i,number_of_loops+1):    
    print(5 + 10 * i)
    print("iteration Number:", i)
    i += 1
    time.sleep(0.2)
print("End of the loop!")
time.sleep(2)

# Basic Operations 
print("\n\n\nBasic Python Operations Demonstration")
a = 15
b = 4
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floordivison = a // b
modulus = a % b
exponentiation = a ** b
print("Addition:", addition) # standard addition
print("Subtraction:", subtraction) # standard subtraction
print("Multiplication:", multiplication) # standard multiplication
print("Division:", division) # standard division
print("Floordivison:", floordivison) # used to get the integer part of a division
print("Modulus:", modulus) # used to get the remainder of a division
print("Exponentiation:", exponentiation) # standard exponentiation

print("\nEnd of Basic Operations Demonstration!")
time.sleep(2)

# Data Types
print("\n\nData Types Demonstration!")

x = "Hello World"                               #str	
x = 20	                                        #int	
x = 20.5                                        #float	
x = 1j                                          #complex	
x = ["apple", "banana", "cherry"]	            #list	# Kinda like an vector/array
x = ("apple", "banana", "cherry")	            #tuple	# Kinda like an vector/array but immutable
x = range(6)	                                #range	
x = {"name" : "John", "age" : 36}	            #dict	
x = {"apple", "banana", "cherry"}	            #set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	                                    #bool	
x = b"Hello"	                                #bytes	
x = bytearray(5)	                            #bytearray	
x = memoryview(bytes(5))	                    #memoryview	
x = None                                        #NoneType
# You can also specify the data type you want by type_name(value) e.g., x = str("Hello World") thats called a constructor

print("\nThere are lots of data types so I am not printing each one.")
time.sleep(1)
print("\nEnd of Data Types Demonstration!")
time.sleep(1)
cls()

# User Input!
print("Yay User Input Time!")
time.sleep(2)
print("We are going to play Basic Rock Paper Scissors")

Possible_Moves = ["Rock", "Paper", "Scissors"]

Player_Move = input("Enter your move (rock = 1 ,p = 2 ,s = 3. Please only time a number from 1-3): ")

print(f"You Picked {Possible_Moves[int(Player_Move)+1]}!")


if Player_Move == "r":
    print("I pick Scissors You win!")
elif Player_Move == "p":
    print("I pick Scissors You lose :(")
elif Player_Move == "s":
    print("I pick Scissors Its a tie!")
    

