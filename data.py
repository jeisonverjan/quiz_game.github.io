import requests
import random


#This function get quiz question from the APi: https://the-trivia-api.com/
#Receive an str to set the difficulty of the questions
# return a question (str), right_answer (str), answer_final(dict)
def get_question(difficulty):

    parameters = {'limit': 1, 'difficulty': difficulty}
    if difficulty == 'random':
         parameters = {'limit': 1}
    r = requests.get('https://the-trivia-api.com/api/questions', params=parameters)
    data = r.json()

    question = data[0]['question']
    answers = data[0]['incorrectAnswers']
    right_answer = data[0]['correctAnswer']
    answers.append(data[0]['correctAnswer'])
    random.shuffle(answers)
    answers_final = {'a':answers[0], 'b':answers[1], 'c':answers[2], 'd':answers[3]}

    return(question, right_answer, answers_final)


#This function greets and requests information about the difficulty.
#Receive none
#Return str with the difficulty
def game_introduction():
    print('Select the difficulty')
    print('easy / medium / hard / random')
    difficulty = input()

    return difficulty


