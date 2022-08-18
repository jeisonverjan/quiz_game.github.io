from data import get_question, game_introduction
import time


def show_questions():
    score = 0
    for i in range(5):
        question, right_answer, answers_final = get_question(difficulty)
        print(difficulty)
        print(question)
        for element in answers_final:
            print(element, answers_final[element])

        user_answer = answers_final[input('Select your Answer: ' )]

        if user_answer == right_answer:
            print('Correct!')
            score +=10
        else:
            print('Incorrect!')
        time.sleep(3)

    print('Congratulation! your score is: ', score)

if __name__ == __name__:
    
    difficulty = game_introduction()
    show_questions()