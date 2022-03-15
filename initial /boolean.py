# Statement one:

# Dogs are mammals.
# Statement two:

# My dog is named Pavel.
# Statement three:

# Dogs make the best pets.
# Statement four:

# Cats are female dogs.


from calendar import weekday


example_statement = "No"

statement_one = "Yes"

statement_two = "Yes"

statement_three = "No"

statement_four = "Yes"


print("7" != 7)

my_baby_bool = "true"



print(type(my_baby_bool))


my_baby_bool_two = True

print(type(my_baby_bool_two))


# Controll flow with if else


user_name = "Yeison"


if user_name == "Yeison":
    print("Keep learning Yeison")


if 4 == 2 + 2:
    print("Hello World")



####################################3


user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")


age_user = 13

if age_user <= 13:
    print("Sorry You're no allow here")



    # Boolean Operators: and
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")



# Boolean Operators: or

True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False


statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

credits = 118
gpa = 2.0


if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")


#Boolean Operators: not


# Reverse the value 

not True == False
not False == True


statement_one = not (4 + 5 <= 9)

statement_two =  not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8



if not credits >= 120:
  print("You do not have enough credits to graduate.") 



if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")


if( not credits >=  120) and (not gpa >= 2.0):
  print("You do not meet either requirement to graduate!")


# Else Statements

weekday = True

if weekday:
      print("wake up at 6:30")
else:
  print("sleep in")


age = 35


if age >= 13:
      print("Access granted.")
else:
  print("Sorry, you must be 13 or older to watch this movie.")



if age <= 23:
    print("Hello World")
else: 
    print("Else case just happen")


if (credits >= 120) and (gpa >= 2.0):
      print("You meet the requirements to graduate!")

else: 
  print("You do not meet the requirements to graduate.")


# Else If Statements

print("Thank you for the donation!")
donation = 1000
 
if donation >= 1000:
  print("You've achieved platinum status")
elif donation >= 500:
  print("You've achieved gold donor status")
elif donation >= 100:
  print("You've achieved silver donor status")
else:
  print("You've achieved bronze donor status")


# Mores examples


grade = 86


if grade > 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("D")






import random


name = "Yeison"

question = "Yes"

answer = ""


random_number = random.randint(1,9)

print(random_number)

if random_number == 1:
  answer = "Yes - desfinitely"

elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "eply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."

elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
else: 
  answer = "Error"

















