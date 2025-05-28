import tkinter as tk
from tkinter import messagebox
import time
import random

# Sample sentences
phrases = [
    "The sun shines on the snowy mountains.",
    "Python is a versatile programming language.",
    "Cats love sleeping near the windows.",
    "A good coffee in the morning makes all the difference.",
    "The algorithm sorts the data efficiently."
]

# Global variables
start_time = None
selected_phrase = random.choice(phrases)

# Start test on first key press
def start_test(event):
    global start_time
    if start_time is None:
        start_time = time.time()

# Calculate typing speed and accuracy
def calculate_speed():
    global start_time
    if start_time is None:
        messagebox.showwarning("Warning", "Start typing before submitting!")
        return

    end_time = time.time()
    typed_text = entry.get("1.0", tk.END).strip()
    time_taken = end_time - start_time

    if time_taken == 0:
        messagebox.showerror("Error", "Invalid time. Please try again.")
        return

    # WPM calculation
    words_typed = typed_text.split()
    word_count = len(words_typed)
    wpm = round((word_count / time_taken) * 60)

    # Character-based accuracy
    correct_chars = 0
    for i in range(min(len(typed_text), len(selected_phrase))):
        if typed_text[i] == selected_phrase[i]:
            correct_chars += 1
    total_chars = len(selected_phrase)
    accuracy = round((correct_chars / total_chars) * 100)

    messagebox.showinfo("Result", f"Time elapsed: {round(time_taken, 2)} sec\n"
                                  f"Speed: {wpm} WPM\n"
                                  f"Accuracy: {correct_chars}/{total_chars} characters ({accuracy}%)")
    reset()

# Reset test
def reset():
    global start_time, selected_phrase
    start_time = None
    selected_phrase = random.choice(phrases)
    label_phrase.config(text=selected_phrase)
    entry.delete("1.0", tk.END)

# Exit application
def quit_app():
    root.destroy()

# GUI
root = tk.Tk()
root.title("⏱️ Typing Speed Test")

label_instruction = tk.Label(root, text="Type the sentence below as fast and accurately as possible:", font=("Arial", 14))
label_instruction.pack(pady=10)

label_phrase = tk.Label(root, text=selected_phrase, wraplength=600, font=("Arial", 16), fg="blue")
label_phrase.pack(pady=10)

entry = tk.Text(root, height=5, width=60, font=("Arial", 14))
entry.pack(pady=10)
entry.bind("<KeyPress>", start_test)

btn_submit = tk.Button(root, text="Submit", command=calculate_speed, font=("Arial", 12))
btn_submit.pack(pady=5)

btn_reset = tk.Button(root, text="Reset", command=reset, font=("Arial", 12))
btn_reset.pack(pady=5)

btn_quit = tk.Button(root, text="Quit", command=quit_app, font=("Arial", 12))
btn_quit.pack(pady=5)

root.mainloop()
