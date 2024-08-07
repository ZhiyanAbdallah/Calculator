from tkinter import Tk, Button, Entry, StringVar, font

class Calculator(Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("300x400")
        self.configure(bg="#282828")

        # Create variables
        self.result_var = StringVar()
        self.current_number = StringVar()
        self.current_number.set("")

        # Create display
        self.create_display()

        # Create buttons
        self.create_buttons()

        # Bind events
        self.bind("<Key>", self.on_key_press)

    def create_display(self):
        entry_font = font.Font(family="Arial", size=24)
        entry = Entry(self, textvariable=self.result_var, font=entry_font, bd=0, bg="#282828", fg="white", justify="right")
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=(10, 0))

    def create_buttons(self):
        button_font = font.Font(family="Arial", size=14)
        buttons = [
            ("C", 1, 0, self.clear_button),
            ("/", 1, 1, lambda: self.on_operation_click("/")),
            ("*", 1, 2, lambda: self.on_operation_click("*")),
            ("-", 1, 3, lambda: self.on_operation_click("-")),
            ("7", 2, 0, lambda: self.on_number_click("7")),
            ("8", 2, 1, lambda: self.on_number_click("8")),
            ("9", 2, 2, lambda: self.on_number_click("9")),
            ("+", 2, 3, lambda: self.on_operation_click("+")),
            ("4", 3, 0, lambda: self.on_number_click("4")),
            ("5", 3, 1, lambda: self.on_number_click("5")),
            ("6", 3, 2, lambda: self.on_number_click("6")),
            ("🔄️", 3, 3, self.on_decimal_click),

            ("1", 4, 0, lambda: self.on_number_click("1")),
            ("2", 4, 1, lambda: self.on_number_click("2")),
            ("3", 4, 2, lambda: self.on_number_click("3")),
            (".", 4, 3, self.on_decimal_click),
            ("0", 5, 0, lambda: self.on_number_click("0")),
            ("=", 5, 1, self.on_equal_click)
        ]

        for (text, row, column, command) in buttons:
            button = Button(self, text=text, font=button_font, bd=0, bg="#444444", fg="white", command=command)
            button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)

    def on_number_click(self, number):
        current_value = self.result_var.get()
        self.result_var.set(current_value + number)

    def on_decimal_click(self):
        current_value = self.result_var.get()
        if "." not in current_value:
            self.result_var.set(current_value + ".")

    def on_operation_click(self, operation):
        current_value = self.result_var.get()
        self.result_var.set(current_value + " " + operation + " ")

    def on_equal_click(self):
        try:
            expression = self.result_var.get().replace("×", "*").replace("÷", "/")
            result = eval(expression)
            self.result_var.set(result)
        except ZeroDivisionError:
            self.result_var.set("Error: Division by zero")
        except Exception as e:
            self.result_var.set(f"Error: {str(e)}")

    def clear_button(self):
        self.result_var.set("")

    def on_key_press(self, event):
        if event.char.isdigit():
            self.on_number_click(event.char)
        elif event.char in "+-*/.=":
            if event.char == ".":
                self.on_decimal_click()
            elif event.char == "=":
                self.on_equal_click()
            else:
                self.on_operation_click(event.char)
        elif event.char.lower() == "c":
            self.clear_button()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()