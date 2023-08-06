import tkinter as tk
from tkinter import messagebox

# Example quiz questions
quiz_questions = [
    {
        "question": "1. What is the capital of France?",
        "choices": ["a) London", "b) Paris", "c) Berlin", "d) Rome"],
        "correct_answer": "b",
        "hint": "The capital city is famous for the Eiffel Tower.",
    },
    {
        "question": "2. Who is the author of 'Romeo and Juliet'?",
        "choices": ["a) William Shakespeare", "b) Jane Austen", "c) Charles Dickens", "d) Mark Twain"],
        "correct_answer": "a",
        "hint": "He is considered one of the greatest playwrights in the English language.",
    },
    # Add eight more questions here
    {
        "question": "3. Which planet is known as the 'Red Planet'?",
        "choices": ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
        "correct_answer": "b",
        "hint": "It is named after the Roman god of war.",
    },
    {
        "question": "4. What is the largest mammal on Earth?",
        "choices": ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Polar Bear"],
        "correct_answer": "b",
        "hint": "It is a marine mammal and the largest animal ever known to have existed.",
    },
    {
        "question": "5. Who painted the Mona Lisa?",
        "choices": ["a) Vincent van Gogh", "b) Leonardo da Vinci", "c) Pablo Picasso", "d) Michelangelo"],
        "correct_answer": "b",
        "hint": "The artist was a Renaissance polymath known for his scientific inventions and artistic masterpieces.",
    },
    {
        "question": "6. What is the chemical symbol for gold?",
        "choices": ["a) Go", "b) Au", "c) Ag", "d) Hg"],
        "correct_answer": "b",
        "hint": "Its symbol comes from the Latin word 'aurum'.",
    },
    {
        "question": "7. In which country would you find the Great Barrier Reef?",
        "choices": ["a) Australia", "b) Brazil", "c) India", "d) South Africa"],
        "correct_answer": "a",
        "hint": "It is located in the Coral Sea, off the coast of a country known for kangaroos and koalas.",
    },
    {
        "question": "8. What is the capital of Japan?",
        "choices": ["a) Tokyo", "b) Beijing", "c) Seoul", "d) Bangkok"],
        "correct_answer": "a",
        "hint": "It is a bustling metropolis known for its technological innovations and rich culture.",
    },
    {
        "question": "9. Which planet is known as the 'Blue Planet'?",
        "choices": ["a) Earth", "b) Mars", "c) Saturn", "d) Neptune"],
        "correct_answer": "a",
        "hint": "It is the only planet in the solar system known to support life.",
    },
    {
        "question": "10. Who wrote the play 'Hamlet'?",
        "choices": ["a) William Shakespeare", "b) Charles Dickens", "c) Jane Austen", "d) Mark Twain"],
        "correct_answer": "a",
        "hint": "The playwright is often referred to as the 'Bard of Avon'.",
    },
]

class QuizGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("400x700")
        
        self.score = 0
        self.question_idx = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.selected_answer = tk.StringVar()
        
        self.question_label = tk.Label(self, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)
        
        self.choices_buttons = []
        for i in range(4):
            button = tk.Radiobutton(self, text="", font=("Arial", 12), value="", variable=self.selected_answer)
            self.choices_buttons.append(button)
            button.pack(pady=5)
        
        self.hint_button = tk.Button(self, text="Hint", font=("Arial", 12), command=self.display_hint, state=tk.DISABLED)
        self.hint_button.pack(pady=5)
        
        self.submit_button = tk.Button(self, text="Submit", font=("Arial", 12), command=self.check_answer, state=tk.DISABLED)
        self.submit_button.pack(pady=5)

        self.clear_button = tk.Button(self, text="Clear", font=("Arial", 12), command=self.clear_selection, state=tk.DISABLED)
        self.clear_button.pack(pady=5)

        self.display_next_question()

    def display_next_question(self):
        if self.question_idx < len(quiz_questions):
            question_data = quiz_questions[self.question_idx]
            self.question_label.config(text=question_data["question"])
            
            choices = question_data["choices"]
            for i in range(len(choices)):
                self.choices_buttons[i].config(text=choices[i], value=choices[i][0].lower())
            
            self.selected_answer.set("")
            self.hint_button.config(state=tk.NORMAL)
            self.submit_button.config(state=tk.NORMAL)
            self.clear_button.config(state=tk.NORMAL)
        else:
            self.show_results_window()

    def check_answer(self):
        question_data = quiz_questions[self.question_idx]
        user_answer = self.selected_answer.get()
        correct_answer = question_data["correct_answer"].lower()
        
        if user_answer == correct_answer:
            self.score += 1
            self.correct_answers += 1
        else:
            self.wrong_answers += 1
        
        self.next_question()

    def next_question(self):
        self.question_idx += 1
        self.display_next_question()

    def clear_selection(self):
        self.selected_answer.set("")

    def display_hint(self):
        question_data = quiz_questions[self.question_idx]
        hint = question_data["hint"]
        messagebox.showinfo("Hint", hint)

    def show_results_window(self):
        results_window = tk.Toplevel(self)
        results_window.title("Quiz Results")
        results_window.geometry("300x200")
        
        tk.Label(results_window, text=f"Your final score: {self.score}/{len(quiz_questions)}").pack(pady=10)
        tk.Label(results_window, text=f"Correct Answers: {self.correct_answers}").pack(pady=5)
        tk.Label(results_window, text=f"Wrong Answers: {self.wrong_answers}").pack(pady=5)
        
        tk.Button(results_window, text="Close", font=("Arial", 12), command=results_window.destroy).pack(pady=10)

        # Reset quiz for another playthrough
        self.score = 0
        self.question_idx = 0
        self.correct_answers = 0
        self.wrong_answers = 0

        # Start the quiz again
        self.display_next_question()

if __name__ == "__main__":
    app = QuizGameApp()
    app.mainloop()
