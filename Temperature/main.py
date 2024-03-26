#s24435 Maciej Łatosz
import tkinter as tk
from tkinter import ttk
from Sheet import Sheet
import matplotlib.pyplot as plt
from matplotlib import cm


class HeatApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Heat Simulation")
        self.geometry("600x600")

        self.sheet = Sheet()

        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.bind("<Configure>", self.on_canvas_resize)

        self.calc_heat_button = ttk.Button(self, text="Calculate Heat", command=self.calculate_heat)
        self.calc_heat_button.grid(row=1, column=0, pady=10, sticky="ew")

    def on_canvas_resize(self, event):
        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        cell_size = min(width // self.sheet.matrix.shape[1], height // self.sheet.matrix.shape[0])

        norm = plt.Normalize(self.sheet.matrix.min(), self.sheet.matrix.max())
        colors = cm.plasma(norm(self.sheet.matrix))

        for i in range(self.sheet.matrix.shape[0]):
            for j in range(self.sheet.matrix.shape[1]):
                value = self.sheet.matrix[i, j]
                color = self.rgb2hex(colors[i, j][:3])
                self.canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size,
                                             fill=color, outline="")
                self.canvas.create_text(j * cell_size + cell_size // 2, i * cell_size + cell_size // 2,
                                        text="{:.3g}".format(value), font=("Arial_bold", 6))

    def rgb2hex(self, rgb):
        r, g, b = (int(255 * c) for c in rgb)
        return f"#{r:02x}{g:02x}{b:02x}"

    def calculate_heat(self):

        self.sheet.calc_heat()
        self.update_canvas()


if __name__ == "__main__":
    app = HeatApp()
    app.mainloop()
