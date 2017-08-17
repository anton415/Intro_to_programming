# First test string.
test_string1 = "Python's a drop-in ___1___ for BASIC " \
               "in the sense that Optimus Prime is a drop-in ___1___ for a truck. - Cory Dodt"

# Answers for first test.
answers1 = ["replacement"]

# Second test string.
test_string2 = "Always ___1___ as if the guy who ends up maintaining your ___1___ " \
               "will be a violent ___2___ who knows where you live. - Martin Golding"

# Answers for secod test.
answers2 = ["code", "psychopath"]

# Third test string.
test_string3 = "Most good ___1___ do programming not because they expect to get ___2___" \
               " or get adulation by the public, but because it is ___3___ to program. - Linus Torvalds"

# Answers for third test.
answers3 = ["programmers", "paid", "fun"]

# User chose level: easy, medium or hard. This function start function "game".
def chose_level(user_level):
    if user_level == "easy":
        game(test_string1, answers1, 1)
    if user_level == "medium":
        game(test_string2, answers2, 2)
    if user_level == "hard":
        game(test_string3, answers3, 3)

# Insert correct answer in test string.
def insert_answer(test_string, answers, answers_number):
    for index, string in enumerate(test_string):
        empty_string = "___" + str(answers_number) + "___"
        if (string == empty_string):
            test_string[index] = answers[answers_number - 1]

# In this function is countings attempts and check if answer correct.
def game(test_string, answers, empty_string_count):
    test_string = test_string.split()
    answers_number = 1
    attempts_count = 5
    while (empty_string_count + 1 > answers_number):
        while attempts_count > 0:
            print " ".join(test_string)
            word = raw_input("Type " + str(answers_number) + " word: ")
            if word in answers:
                print "correct :)"
                insert_answer(test_string, answers, answers_number)
                answers_number += 1
                break
            else:
                print "try again :("
                attempts_count -= 1
                print "You have " + str(attempts_count) + " attempts."
    print " ".join(test_string)

chose_level(raw_input("Type in difficulty level: "))
