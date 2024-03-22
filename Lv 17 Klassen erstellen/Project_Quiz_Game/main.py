from question_model import Question
from data import question_data
from quiz_controller import Quizcontroller

question_bank = []

# Für jedes Dictionary in der Liste
for question in question_data:
    # Key und Value werden mit dieser Syntax separat in jeweils einer Variable gespeichert
    question_text = question["text"]
    question_answer = question["answer"]
    
    # Der Liste wird ein Objekt der Klasse Question hinzugefügt
    question_bank.append(Question(question_text, question_answer))
    
quiz = Quizcontroller(question_bank)

while quiz.still_has_questions():
    quiz.next_question()