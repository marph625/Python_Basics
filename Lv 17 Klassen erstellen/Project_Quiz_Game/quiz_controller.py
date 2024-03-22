class Quizcontroller:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Frage: {self.question_number} : {current_question.text} True oder False\n")
        
        # Methode check_answer wird hier aufgerufen, um den Zugriff auf die Argumente (für mich) zu erleichtern
        self.check_answer(user_answer, current_question.answer)
        
    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)
    
    # Parameter kann ich nennen wie ich will
    def check_answer(self, x, y) -> bool:
        if x.lower() == y.lower():
            self.score += 1
            print("Richtig! | Score:", self.score)
            return True
        else:
            print("Falsch! | Score:", self.score)
            return False
