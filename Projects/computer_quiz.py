#This project is my first ever project that I decided to tackle in Python.

#This prompts the user for their name and age to determine if the user is old enough to complete this quiz
user_name = input("Name: ")
user_age = int(input("Age: "))

#This is a score system that counts how many questions the user got right.
score = 0

#This is just an introductory statement with user's name to personal the game
print("Hey there!", user_name,"Welcome to Com. Quiz !") # I didnt concatenate this because i felt it was a bit complicated


if user_age >= 15:
    print("Are You Ready To Conquer This Quiz !!")
    proceed_with_quiz = "yes"
else:
    print("This Quiz may be too challenging for you")
    proceed_with_quiz = input("Would you like to proceed anyway? (yes/no): ").strip().lower()

if proceed_with_quiz.lower() == "no":
    quit()      # I used "quit()" as an instruction to the compiler to skip all the questions and end the program
elif proceed_with_quiz.lower() == "yes":
    
    #Question 1

    answer = input("What is the full name for CPU?  ").strip() #I added ".strip()" to remove any whitespace from user input to ensure it is checked accurately.

    if answer.lower() == "central processing unit":
        print("Correct Answer !")
        score += 1
    else:
        print("Incorrect")
    
    #Question 2

    answer = input("What is the full name for RAM?  ").strip()

    if answer.lower() == "random access memory":
        print("Correct Answer !")
        score += 1
    else:
        print("Incorrect")

    #Question 3

    answer = input("What is the full name for GPU?  ").strip()

    if answer.lower() == "graphic processing unit":
        print("Correct Answer !")
        score += 1
    else:
        print("Incorrect")

    #Question 4

    answer = input("What is the full name for LED?  ").strip()

    if answer.lower() == "light-emitting diode":
        print("Correct Answer !")
        score += 1
    else:
        print("Incorrect")

    #Question 5

    answer = input("What is the meant by Binary in terms of CS?  ").strip()

    if answer.lower() == "counting system":
        print("Correct Answer !")
        score += 1
    else:
        print("Incorrect")

    #Question 6

    answer = input("What is the full name for PSU?  ").strip()

    if answer.lower() == "power supply":
        print("Correct Answer !")
        score += 1
    else:
        print("Incorrect")

    #Question 7

    answer = input("What is the full name for VGA?  ").strip()

    if answer.lower() == "video array graphics":
        print("Correct Answer !")
        score += 1
    else:
        print("Incorrect")

    #Question 8

    answer = input("What is the function of the PSU?  ").strip()

    if answer.lower() == "supply power to the pc":
        print("Correct Answer !")
        score += 1
    else:
        print("Incorrect")

    #Question 9

    answer = input("What is the function of the VGA?  ").strip()

    if answer.lower() == "supports video input":
        print("Correct Answer !")
        score += 1
    else:
        print("Incorrect")
    #Question 10

    answer = input("What is the color scheme of pixels on a computer?  ").strip()

    if answer.lower() == "r-g-b":
        print("Correct Answer !")
        score += 1
    else:
        print("Incorrect")

else:
    print("Invalid input.Please enter 'yes' or 'no'.")

print("Awesome!, You managed to score", score,"out of 10")
