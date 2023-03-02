import time

# Setting time limit (in seconds since time.time())

time_limit = int(30)


# Quiz questions using a dictionary to hold them
Questions = {
    "When was the first known use of the word 'quiz'": ["1781" , "1771" , "1871" , "1881"] ,
    "Which built-in function can get information from the user": ["input" , "get" , "print" , "write"] ,
    "Which keyword do you use to loop over a given list of elements": ["for" , "while" , "each" , "loop"]
}

# Iterate over the quiz questions
for question , options in Questions.items():

    # Starting the timer
    start_time = time.time()
    print()

    # Ask the question
    print(f"Question: {question}")
    correct_answer = options[0]
    options = sorted(options)  # Sort the options alphabetically
    for label , option in enumerate(options , 1):
        print(f"{label}: {option}")

    # Check if the answer is correct
    while time.time() < start_time + time_limit:
        answer = input("What is your answer? ")
        if answer == correct_answer:
            print("Nicely done!")
            break
        elif answer not in Questions.values():
            time_left = int(start_time + time_limit - time.time())
            print(f"Invalid Responce, you have {time_left} seconds left, try again:")
            
        else:
             time_left = int(start_time + time_limit - time.time())
             print(f"Incorrect answer. You have {time_left} seconds left to answer this question.")
             print(f"Try again:")
             answer = input("What is your answer? ")
    else:
        time_left = int(start_time + time_limit - time.time())
        print(f"Incorrect answer. You have {time_left} seconds left to answer this question.")

        # Keep asking for an answer until the time limit is reached
        while time.time() < start_time + time_limit:
            answer = input("What is your answer? ")
            if answer == correct_answer:
                print("Nicely done!")
            else:
                time_left = int(start_time + time_limit - time.time())
                print(f"Incorrect answer. You have {time_left} seconds left to answer this question.")
    print()  # Add a blank line between questions
# If timer has expired, end quiz.
else:
    print("Your times up!")

