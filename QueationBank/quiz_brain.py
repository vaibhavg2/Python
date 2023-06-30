class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        while self.question_number < 10:
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):").lower()
            self.check_answer(user_answer, current_question.answer,self.question_number)

    def check_answer(self, user_answer, correct_answer,question_number):
        if user_answer.lower() == correct_answer.lower():
            print("correct answer!\n")
            self.score += 1
        else:
            print("Wrong answer!\n")
        print(f"Correct answer was: {correct_answer}\n Your score is {self.score}/{question_number}\n")

            # if answer == str(current_question.answer).lower():
            #     print("correct answer!")
            #     self.score +=1
            # else:
            #     print("wrong answer!")
            #
            # print(f"Correct answare was:{current_question.answer}\nYou Scored {self.score}/{self.question_number}")