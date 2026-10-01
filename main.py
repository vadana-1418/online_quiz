import tkinter as tk

class QuizApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz Game")
        self.root.geometry("520x450")

        self.questions = [
            {
                "question": "How many continents are there in the world?",
                "options": ["Five", "Six", "Seven", "Eight"],
                "correct": 2
            },
            {
                "question": "Which metal is liquid at room temperature?",
                "options": ["Iron", "Aluminium", "Mercury", "Copper"],
                "correct": 2
            },
            {
                "question": "Which is the smallest prime number?",
                "options": ["0", "1", "2", "3"],
                "correct": 2
            },
            {
                "question": "What is the capital of India?",
                "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
                "correct": 1
            }
        ]

        self.current_question = 0
        self.score = 0
        self.answers = [-1] * len(self.questions)

        self.time_left = 10
        self.timer_id = None

        self.question_label = tk.Label(self.root, font=("Arial", 14), wraplength=450)
        self.question_label.pack(pady=15)

        self.timer_label = tk.Label(self.root, text="Time: 10", font=("Arial", 12))
        self.timer_label.pack()

        self.selected_option = tk.IntVar()

        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=15)

        self.nav_frame = tk.Frame(self.root)
        self.nav_frame.pack(pady=10)

        self.prev_btn = tk.Button(self.nav_frame, text="Previous", command=self.prev_question)
        self.prev_btn.grid(row=0, column=0, padx=10)

        self.next_btn = tk.Button(self.nav_frame, text="Next", command=self.next_question)
        self.next_btn.grid(row=0, column=1, padx=10)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.show_question()

    def show_question(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        self.time_left = 10
        self.update_timer()

        q = self.questions[self.current_question]
        self.question_label.config(text=q["question"])

        self.selected_option.set(self.answers[self.current_question])

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        for i, option in enumerate(q["options"]):
            rb = tk.Radiobutton(
                self.options_frame,
                text=option,
                variable=self.selected_option,
                value=i
            )
            rb.pack(anchor="w")

    def update_timer(self):
        self.timer_label.config(text=f"Time: {self.time_left}")

        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.next_question()

    def save_answer(self):
        self.answers[self.current_question] = self.selected_option.get()

    def next_question(self):
        self.save_answer()

        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.show_question()
        else:
            self.show_result()

    def prev_question(self):
        self.save_answer()

        if self.current_question > 0:
            self.current_question -= 1
            self.show_question()

    def show_result(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        self.score = 0
        for i, ans in enumerate(self.answers):
            if ans == self.questions[i]["correct"]:
                self.score += 1

        for widget in self.root.winfo_children():
            widget.destroy()

        result = tk.Label(
            self.root,
            text=f"Quiz Completed 🎉\nFinal Score: {self.score}/{len(self.questions)}",
            font=("Arial", 16)
        )
        result.pack(pady=50)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = QuizApp()
    app.run()