import tkinter as tk
from tkinter import messagebox
import threading
import time

class ClickCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador de Clics")
        
        self.click_count = 0
        self.time_left = 30
        self.running = True
        
        self.label_clicks = tk.Label(root, text="Clics: 0", font=("Helvetica", 16))
        self.label_clicks.pack(pady=10)
        
        self.label_timer = tk.Label(root, text="Tiempo restante: 30 segundos", font=("Helvetica", 16))
        self.label_timer.pack(pady=10)
        
        self.button_click = tk.Button(root, text="Haz clic aquí", command=self.increment_clicks, font=("Helvetica", 16))
        self.button_click.pack(pady=20)
        
        self.timer_thread = threading.Thread(target=self.start_timer)
        self.timer_thread.start()

    def increment_clicks(self):
        if self.running:
            self.click_count += 1
            self.label_clicks.config(text=f"Clics: {self.click_count}")

    def start_timer(self):
        while self.time_left > 0 and self.running:
            time.sleep(1)
            self.time_left -= 1
            self.update_timer_label()
            
        self.end_game()

    def update_timer_label(self):
        self.root.after(0, lambda: self.label_timer.config(text=f"Tiempo restante: {self.time_left} segundos"))

    def end_game(self):
        self.running = False
        self.root.after(0, lambda: self.button_click.config(state=tk.DISABLED))
        self.root.after(0, lambda: messagebox.showinfo("Tiempo terminado", f"Has hecho {self.click_count} clics en 30 segundos"))

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickCounterApp(root)
    root.mainloop()