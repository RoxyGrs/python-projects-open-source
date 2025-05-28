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
    typed_text = entry.get("1.0", tk.END).strip()
    time_taken = end_time - start_time

    if time_taken == 0:
        messagebox.showerror("Error", "Invalid time. Please try again.")
        return

    words_typed = typed_text.split()
    word_count = len(words_typed)
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
    entry.delete("1.0", tk.END)

def quit_app():
    root.destroy()

# ---------- GUI ----------
root = tk.Tk()
root.title("⏱️ Typing Speed Test")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

font_main = ("Segoe UI", 12)
font_title = ("Segoe UI", 16, "bold")

frame = tk.Frame(root, bg="#f0f4f8", padx=20, pady=20)
frame.pack()

label_instruction = tk.Label(frame, text="Type the sentence below as fast and accurately as possible:",
                             font=font_main, bg="#f0f4f8")
label_instruction.pack(pady=(0, 10))

label_phrase = tk.Label(frame, text=selected_phrase, wraplength=500,
                        font=("Segoe UI", 14), fg="#2c3e50", bg="#dfe6e9",
                        bd=2, relief="solid", padx=10, pady=10)
label_phrase.pack(pady=(0, 10))

entry = tk.Text(frame, height=4, width=60, font=font_main, wrap="word", bd=2, relief="sunken")
entry.pack(pady=(0, 10))
entry.bind("<KeyPress>", start_test)
entry.bind("<Return>", on_enter_press)

button_frame = tk.Frame(frame, bg="#f0f4f8")
button_frame.pack(pady=5)

btn_style = {"font": ("Segoe UI", 11), "padx": 10, "pady": 4, "bd": 0, "width": 10}

btn_submit = tk.Button(button_frame, text="Submit", command=calculate_speed, bg="#74b9ff", fg="white", **btn_style)
btn_submit.grid(row=0, column=0, padx=4)

btn_reset = tk.Button(button_frame, text="Reset", command=reset, bg="#55efc4", fg="black", **btn_style)
btn_reset.grid(row=0, column=1, padx=4)

btn_quit = tk.Button(button_frame, text="Quit", command=quit_app, bg="#fab1a0", fg="black", **btn_style)
btn_quit.grid(row=0, column=2, padx=4)

for btn in [btn_submit, btn_reset, btn_quit]:
    btn.bind("<Enter>", lambda e, b=btn: b.config(relief="groove"))
    btn.bind("<Leave>", lambda e, b=btn: b.config(relief="flat"))

# Auto-size the window to fit contents
root.update_idletasks()
root.geometry(f"{frame.winfo_reqwidth() + 40}x{frame.winfo_reqheight() + 40}")

root.mainloop()
