from Question import Question
print("USE A, B, OR C TO ANSWER QUESTIONS!")
# Questions and choices over here.
question_prompts = [
    "How many legs does an Octopus have?\n(a) 5\n(b) 8\n(c) None\n\n",
    "Is the sky blue?\n(a) Yes\n(b) No\n(c) Maybe\n\n",
    "Is grass green?\n(a) Yes\n(b) No\n(c) Maybe\n\n ",
    "Can penguins fly?\n(a) Yes\n(b) No\n(c) Maybe\n\n",
    "Is mexico a country?\n(a) Yes\n(b) No\n(c) Maybe\n\n",
    "Is the cake a lie?\n(a) Yes\n(b) No\n(c) Maybe\n\n",
]
# Creating question objects. Question = object. question_prompts = prompt. "c" = answer.
# Question = Self. question_prompts[0-5] = prompt. "c" = answer.
questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "a"),
]


# Creating function that will run the test. Will ask the questions and will check to see if user got it right.
# (questions) is a list of Question objects I want to ask the user.
def run_test(questions):
    # To keep track of how user did I create a var called score and set it to 0. Everytime user gets question right I-
    #  -will increment the score variable.
    score = 0
    # To loop through all the Questions in the questions array i make a for loop. For each question object inside the-
    # -questions array I want to do something.
    for question in questions:
        # answer represents the users answer to the question.
        answer = input(question.prompt)
        # To check to see if the user got it right i use "if answer == question.answer:" Im checking to see if the-
        # -answer the user gave is equal to the answer of the current question.
        if answer == question.answer:
            score += 1
        # To check if the users answer is a valid answer I use this. (I did not get this from a video.) if the users-
        # -answer is not valid, I give them one more try to answer the question with a valid response.
        if answer != "a" and answer != "b" and answer != "c":
            print("Not a valid answer. Use a, b, or c to answer the question.")
            input(question.prompt)
# printing their score.
    print("You Got " + str(score) + "/" + str(len(questions)) + " correct!")


run_test(questions)
# CODE FROM https://www.youtube.com/watch?v=SgQhwtIoQ7o&index=32&list=PLLAZ4kZ9dFpMMs5lskzBApYXn0bl7emsW .
# I hope all my explaining isn't to messy....................................
