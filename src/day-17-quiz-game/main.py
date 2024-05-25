from data import question_data, question_data2
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


# question_bank2 = []
# for question in question_data2:
#     new_question = Question(question["question"], question["correct_answer"])
#     question_bank2.append(new_question)
# quiz2 = QuizBrain(question_bank2)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")