from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []
for data in question_data:
    q = Question(data["question"], data["correct_answer"])
    questions.append(q)

quiz = QuizBrain(questions)
while quiz.still_hat_questions():
    quiz.next_question()

print(f'Your final score is {quiz.score} {quiz.question_number}')
