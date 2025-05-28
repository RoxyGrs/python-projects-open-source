import time
import random
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Sample sentences
phrases = [
    "The sun shines on the snowy mountains.",
    "Python is a versatile programming language.",
    "Cats love sleeping near the windows.",
    "A good coffee in the morning makes all the difference.",
    "The algorithm sorts the data efficiently."
]

start_time = None
selected_phrase = random.choice(phrases)

def start_test(event):
    global start_time
    if start_time is None:
        start_time = time.time()

def calculate_speed():
    global start_time
    if start_time is None:
        messagebox.showwarning("Warning", "Start typing before submitting!")
        return

    end_time = time.time()
    typed_text = entry.get("1.0", "end").strip()
    time_taken = end_time - start_time

    if time_taken == 0:
        messagebox.showerror("Error", "Invalid time. Please try again.")
        return

    word_count = len(typed_text.split())
    wpm = round((word_count / time_taken) * 60)

    correct_chars = sum(1 for i in range(min(len(typed_text), len(selected_phrase))) if typed_text[i] == selected_phrase[i])
    total_chars = len(selected_phrase)
    accuracy = round((correct_chars / total_chars) * 100)

    messagebox.showinfo("Result", f"Time elapsed: {round(time_taken, 2)} sec\n"
                                  f"Speed: {wpm} WPM\n"
                                  f"Accuracy: {correct_chars}/{total_chars} characters ({accuracy}%)")
    reset()

def on_enter_press(event):
    calculate_speed()
    return "break"

def reset():
    global start_time, selected_phrase
    start_time = None
    selected_phrase = random.choice(phrases)
    label_phrase.config(text=selected_phrase)
    entry.delete("1.0", "end")

# --- UI Setup ---
app = ttk.Window(themename="flatly")
app.title("Typing Speed Test")
app.geometry("600x400")
app.resizable(False, False)

main_frame = ttk.Frame(app, padding=20)
main_frame.pack(fill=BOTH, expand=True)

ttk.Label(main_frame, text="Type the sentence below as fast and accurately as possible:",
          font=("Segoe UI", 12)).pack(pady=(0, 10))

label_phrase = ttk.Label(main_frame, text=selected_phrase, wraplength=560,
                         font=("Segoe UI", 14), style="info.TLabel", padding=10)
label_phrase.pack(pady=(0, 10))

entry = ttk.Text(main_frame, height=4, width=70, font=("Segoe UI", 12), wrap="word")
entry.pack(pady=(0, 10))
entry.bind("<KeyPress>", start_test)
entry.bind("<Return>", on_enter_press)

btn_frame = ttk.Frame(main_frame)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="Submit", bootstyle=PRIMARY, command=calculate_speed).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="Reset", bootstyle=SUCCESS, command=reset).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="Quit", bootstyle=DANGER, command=app.destroy).grid(row=0, column=2, padx=5)

app.mainloop()
