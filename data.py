import requests
import time
import random
from googletrans import Translator
from colorama import Fore
import colorama
colorama.init(autoreset=True)


#This function get quiz question from the APi: https://the-trivia-api.com/
#Receive an str to set the difficulty of the questions and an str to set the language
# return a question (str), right_answer (str), answer_final(dict)
def get_question(difficulty, language):

    #connect and get iformation from the API
    parameters = {'limit': 1, 'difficulty': difficulty}
    if difficulty == 'random':
         parameters = {'limit': 1}
    r = requests.get('https://the-trivia-api.com/api/questions', params=parameters)
    data = r.json()

    #Assiginig information getting to local variables.
    question = data[0]['question']
    answers = data[0]['incorrectAnswers']
    right_answer = data[0]['correctAnswer']
    answers.append(data[0]['correctAnswer'])

    #if user chose Spanish the the funcion transalte_to_spanish() is call
    if language == 'es':
        question, right_answer, answers = translate_to_spanish(question, right_answer, answers)

    #Shuffling the array of answers
    random.shuffle(answers)

    #Creating a dict with answers.
    answers_final = {'A':answers[0], 'B':answers[1], 'C':answers[2], 'D':answers[3]}

    return(str(question), str(right_answer), answers_final)


#This function translate the question and answers to Spanish, it use the library googletrans
#Receive the quesion srt, the rignt answer str and answers array.
#return question, right_answer, answers in Spanish
def translate_to_spanish(question, right_answer, answers):
    translator = Translator()
    question = translator.translate(question, src='en', dest='es').text
    right_answer = translator.translate(right_answer, src='en', dest='es').text
    for i, element in enumerate(answers):
        answers[i] = translator.translate(element, src='en', dest='es').text

    return  question, right_answer, answers


#This function greets and requests information about the difficulty and the number of question the user wants to answer
#Receive none
#Return str with the difficulty, int with the number of question
def game_introduction():
    print(f"\n \n {Fore.BLUE}!!!WELCOME TO QUIZ GAME!!! \n \n ")
    difficulty = ['easy', 'medium', 'hard', 'random']
    language = ['es', 'en']
    user_choise_difficulty = ''
    user_choise_questions = 1
    user_choise_language = ''
    while True:
        print('Write one of the following difficulties: \n')
        print(difficulty)
        user_choise_difficulty = input().strip().lower()
        if user_choise_difficulty not in difficulty:            
            print('Write one of the available difficulties: ', difficulty)
            continue
        break
    while True:
        print('Whrite the number of question you want to answer (Number)')
        user_choise_questions = input().strip()
        if user_choise_questions.isdigit():           
            if int(user_choise_questions) <= 0 or int(user_choise_questions) > 500:
                print('Write a number higer than 0 and less than 500')
                continue
        else:
            print('Whrite a number')
        break

    while True:
        print('\n Write your language: Espanish / English \n')
        print(language)
        user_choise_language = input().strip().lower()
        if user_choise_language not in language:
            print('Write one of the available languages: ', language , 'Espanish / English')
            continue
        else:
            break

    return user_choise_difficulty, user_choise_language, int(user_choise_questions)



#This function show the questions and calculate the score
#Recieve none
#Return the score int
def show_questions():
    score = 0
    difficulty, language, number_questions = game_introduction()
    for i in range(number_questions):

        try:        
            question, right_answer, answers_final = get_question(difficulty, language)
        except:
            print('Looking for another question...')
            continue

        print('\n', question, '\n')
        for element in answers_final:
            print(element + ':', answers_final[element])

        answers_choices = list(answers_final.keys())
        user_answer = ''
        while user_answer not in answers_choices:
            user_answer = input('Select your Answer: ' ).strip().capitalize()

        if answers_final[user_answer] == right_answer:
            print(f" \n {Fore.GREEN} Correct!")
            score +=1
        else:
            print(f" \n {Fore.RED} Incorrect!")
       

    show_score(score, number_questions)


#This Function show the score
#Receive the score int and the number of question int
#return none

def show_score(score, number_questions):
    avarage = 100 * score // number_questions
    
    if avarage < 50:
        print(f"\n{Fore.RED} You'll do better next time.")
        print(f"\n{Fore.RED} You got {score} answers out of {number_questions} questions right, which equals: {avarage}% \n")
        time.sleep(1)
    else:
        print(f"\n{Fore.GREEN} Congratulation!!!")
        print(f"\n{Fore.GREEN} You got {score} answers out of {number_questions} questions right, which equals: {avarage}% \n")
        time.sleep(1)