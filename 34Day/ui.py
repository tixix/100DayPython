from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"




class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0

        self.score_label = Label(text=f'Score: {self.score}', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true_image,
                                  highlightthickness=0,
                                  command= self.true_button_clicked)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=false_image,
                                   highlightthickness=0,
                                   command= self.false_button_clicked)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="END")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_clicked(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))


    def false_button_clicked(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))

    def give_feedback(self, param):
        if param:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(800, self.get_next_question())

