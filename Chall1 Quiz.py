from Question import Question
print("USE A, B, OR C TO ANSWER QUESTIONS!")

question_prompts = [
    "How many legs does an Octopus have?\n(a) 5\n(b) 8\n(c) None\n\n",
    "Is the sky blue?\n(a) Yes\n(b) No\n(c) Maybe\n\n",
    "Is grass green?\n(a) Yes\n(b) No\n(c) Maybe\n\n ",
    "Can penguins fly?\n(a) Yes\n(b) No\n(c) Maybe\n\n",
    "Is mexico a country?\n(a) Yes\n(b) No\n(c) Maybe\n\n",
    "Is the cake a lie?\n(a) Yes\n(b) No\n(c) Maybe\n\n",
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "a"),
]

def run_test(questions):
    """ loops through a list of questions and asks each one"""
    score = 0
    for question in questions:
        valid_input = False
        # ask question until a valid input has come through
        while valid_input == False:
            answer = input(question.prompt)
            # check if answer is correct
            if answer == question.answer:
                score += 1
            # check if answer is valid
            if answer != "a" and answer != "b" and answer != "c":
                print("Not a valid answer. Use a, b, or c to answer the question.")
            else:
                valid_input = True  # if valid answer was given, exit loop
    print("You Got " + str(score) + "/" + str(len(questions)) + " correct!")


run_test(questions)
# CODE FROM https://www.youtube.com/watch?v=SgQhwtIoQ7o&index=32&list=PLLAZ4kZ9dFpMMs5lskzBApYXn0bl7emsW .