import os
import time
import random



def cls():# Clears Screen planning to have it run between sections
    os.system('cls')

# User Input!
Losses = 0
Ties = 0
Wins = 0
Easter_egg = False

print("Yay User Input Time!")
time.sleep(1)
print("We are going to play Basic Rock Paper Scissors")

while False: #set to false to skip the game for now

    Possible_Moves = ["Rock", "Paper", "Scissors"]
    Player_Move = int(input("Enter your move (Rock = 1 ,Paper = 2 ,Scissors = 3. Please only type a number from 1-3): "))-1 # subtracting 1 to match list index

    #print(f"You Picked {Possible_Moves[int(Player_Move)]}!")
    
    CPU_Choice = random.randint(0,2)

    if Player_Move == 420-1: # subtractuing one since user input is subtacted by 1 so if the user inputs 420 it becomes 419
        print("Exiting Game!")
        time.sleep(1)        
        break
    
    elif Player_Move == 69-1: # subtractuing one since user input is subtacted by 1 so if the user inputs 69 it becomes 68
    
        if Easter_egg == True:
            print("NICE TRY YA FILTHY ANIMAL")
            #os.system('shutdown /s /t 10') # Commented out because it was mad annoying >W<
            exit()
        print("You instantly win this round! Cuz your the best")
        Wins += random.randint(1,15)
        Easter_egg=True
    
    elif Player_Move == CPU_Choice:
        print(f"Tie! CPU also picked {Possible_Moves[CPU_Choice]}!")
        Ties += 1
    
    elif (Player_Move == 0 and CPU_Choice == 2) or (Player_Move == 1 and CPU_Choice == 0) or (Player_Move == 2 and CPU_Choice == 1):
        print(f"You Win! CPU Picked {Possible_Moves[CPU_Choice]}")
        Wins += 1
    
    elif (Player_Move == 0 and CPU_Choice == 1) or (Player_Move == 1 and CPU_Choice == 2) or (Player_Move == 2 and CPU_Choice == 0):
        print(f"You Lose! CPU Picked {Possible_Moves[CPU_Choice]}")
        Losses += 1


    print(f"\n\nYou have Won :{Wins} times! ")   
    print(f"\n\nYou have Tied :{Ties} times! ")   
    print(f"\n\nYou have lost :{Losses} times! ")   

    input("")
    cls()



greeting = "\nHello, This is a Python testing ground!"
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


'''
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
'''
print("\nThere are lots of data types so I am not printing each one.")
time.sleep(1)
print("\nEnd of Data Types Demonstration!")
time.sleep(1)
cls()

# Lists and Tuples :p
print("Lists and Tuples Demonstration!")
Demo_List = ['Adrianna', 'Conner' , '42']
user_list_check = input("Please enter a value(str) to check if its in the demo list: ")
if user_list_check in Demo_List:
    print(f"{user_list_check} is in the Demo List!")
print(f"{Demo_List[-1]} is the final entry in the Demo List") # indexing -1 will provide the last entry in a list
print(Demo_List[1:2])# Outputs a range of values from the list. x:y where x is the starting index and y is the ending index (not inclusive) Can be negative too
print("Demo List Length is:", len(Demo_List))
#Modifying Lists

Demo_List.append('George') # Adds values to the end of a list
Demo_List += ['Charlie'] # You can add a list to a list too If you dont have [] it will add each letter as an individual entry
Demo_List.extend(['Dylan']) # You can also use .extend
Demo_List.insert(1,'Im out of Names') # Inserts value at specified index shifting other values to the right
Demo_List[1:1] = ['James'] # Another way to insert value at specified index shifting other values to the right
Demo_List[1:2] = ['Sophia'] # Replaces value at specified index range
Demo_List.remove('Sophia') # Removes specified value
Demo_List.pop() # Removes last value can also be used to remove value at specified index e.g., Demo_List.pop(1)
#Demo_List.clear() # Empties the entire list
#del Demo_List # Deletes entire list or value at specified index 
Demo_List.sort() # Sorts list in ascending order
print(Demo_List)

# Tuples are immutable meaning they cannot be changed after creation
# They are const, Lists are not
Tuple_Loopule = ('Red', 'Green', 'Blue')
Another_Tuple = tuple(('Circle', 'Square', 'Triangle'))




# Dictionaries and sets
MyCar = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2006,
  "Transmission": "5 Speed Manual"
}
print(MyCar)