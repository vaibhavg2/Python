from data import question_data
from question_model import Question
import random
from quiz_brain import QuizBrain
print(question_data[2]["question"])

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
# question_number = 0
# score = 0
# while question_number < 10:
#     question = random.choice(question_bank)
#     print(question.text)
#     answer = str(input('True/False\n').lower())
#     if answer == str(question.answer).lower():
#         score += 1
#         print('Correct!')
#     else:
#         print('Wrong!')
#     question_number += 1
#     print(f"Your score is {score}/{question_number}")
#
# print('Thank You!\n Quiz is Over')
#
