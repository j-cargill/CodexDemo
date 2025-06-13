import tkinter as tk
from calculator import calculate

class CalculatorGUI:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        master.title("Calculator")
        self.entry = tk.Entry(master, width=20, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self._make_buttons()

    def _make_buttons(self) -> None:
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
        ]
        for (text, row, col) in buttons:
            action = self._calculate if text == '=' else (
                self._clear if text == 'C' else lambda t=text: self._append(t)
            )
            tk.Button(self.master, text=text, width=5, command=action).grid(row=row, column=col, padx=2, pady=2)

    def _append(self, char: str) -> None:
        self.entry.insert(tk.END, char)

    def _clear(self) -> None:
        self.entry.delete(0, tk.END)

    def _calculate(self) -> None:
        expression = self.entry.get()
        for op in '+-*/':
            if op in expression:
                left, right = expression.split(op, 1)
                try:
                    result = calculate(float(left), op, float(right))
                    self.entry.delete(0, tk.END)
                    self.entry.insert(tk.END, str(result))
                except Exception:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(tk.END, 'Error')
                return
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, 'Error')


def main() -> None:
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
