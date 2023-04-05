from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, font=('Arial', 13), fg='white')
        self.score_label.grid(column=1, row=0)

        self.field = Canvas(height=250, width=300, highlightthickness=0)
        self.question = self.field.create_text(150, 125, text="Question", width=280, font=("Arial", 15, "italic"))
        self.field.grid(column=0, row=1, columnspan=2, pady=40)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, bd=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, bd=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.field.config(bg="white")
        self.true_button.config(state="active")
        self.false_button.config(state="active")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.field.itemconfig(self.question, text=question_text)
        else:
            self.field.itemconfig(self.question, text="You've reached the end of the questions.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.field.config(bg="green")
        else:
            self.field.config(bg="red")

        self.window.after(1000, self.get_next_question)
