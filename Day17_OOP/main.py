from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    # Create object from question data list. with text key and answer key.
    new_q = Question(item["question"], item["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
