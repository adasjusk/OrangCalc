import customtkinter as ctk
import tkinter as tk
import os

class OrangCalc(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._setup_window()
        self._create_entry()
        self._create_buttons()
        self._configure_grid()
        self.mode_var = ctk.StringVar(value="Dec")
        self.theme_var = ctk.StringVar(value="Dark")
    def _setup_window(self):
        self.title("OrangCalculator")
        self.geometry("300x400")
        ctk.set_appearance_mode("Dark")
        icon_path = "orange.ico"
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass
    def _create_entry(self):
        self.entry = ctk.CTkEntry(
            self,
            font=("Arial", 20),
            width=280,
            justify="right"
        )
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)
    def _create_button(self, button_text, row_index, col_index):
        button_configs = {
            "=": {
                "command": self.calculate,
                "fg_color": "orange",
                "text_color": "black",
                "hover_color": "#FF8C00"
            },
            "i": {
                "command": self.show_info,
                "fg_color": "grey",
                "hover_color": "darkgrey"
            }
        }
        config = button_configs.get(button_text, {
            "command": lambda t=button_text: self.button_click(t),
            "fg_color": "grey",
            "hover_color": "darkgrey"
        })
        button = ctk.CTkButton(
            self,
            text=button_text,
            font=("Arial", 18),
            width=70,
            height=50,
            **config
        )
        button.grid(row=row_index + 1, column=col_index, padx=5, pady=5, sticky="nsew")
    def _create_buttons(self):
        self.buttons = [
            ["CE", "C", "⌫", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["i", "0", ".", "="]
        ]
        for row_index, row in enumerate(self.buttons):
            for col_index, button_text in enumerate(row):
                self._create_button(button_text, row_index, col_index)
    def _configure_grid(self):
        for i in range(6):
            self.rowconfigure(i, weight=1)
        for i in range(4):
            self.columnconfigure(i, weight=1)
    def button_click(self, text):
        current_text = self.entry.get()
        self.entry.delete(0, ctk.END)
        if text == "C":
            self.entry.insert(0, "")
        elif text == "CE":
            self.entry.insert(0, current_text[:-1])
        elif text == "⌫":
            self.entry.insert(0, current_text[:-1])
        else:
            self.entry.insert(0, current_text + text)
    def calculate(self):
        expr = self.entry.get()
        mode = self.mode_var.get()
        try:
            if mode == "Dec":
                result = eval(expr)
            elif mode == "Hex":
                expr = expr.replace("0x", "")
                result = eval(expr, {"__builtins__": None}, {})
                result = hex(int(result))
            elif mode == "Oct":
                expr = expr.replace("0o", "")
                result = eval(expr, {"__builtins__": None}, {})
                result = oct(int(result))
            elif mode == "Bin":
                expr = expr.replace("0b", "")
                result = eval(expr, {"__builtins__": None}, {})
                result = bin(int(result))
            else:
                result = "Error"
            self.entry.delete(0, ctk.END)
            self.entry.insert(0, str(result))
        except Exception:
            self.entry.delete(0, ctk.END)
            self.entry.insert(0, "Error")
    def show_info(self):
        info_window = tk.Toplevel(self)
        info_window.title("About The OrangCalc")
        info_window.geometry("300x270")
        info_window.attributes("-topmost", True)
        icon_path = "orange.ico"
        if os.path.exists(icon_path):
            try:
                info_window.iconbitmap(icon_path)
            except Exception:
                pass
        bg_color = "#242424" if self.theme_var.get() == "Dark" else "#f0f6fc"
        info_window.configure(bg=bg_color)
        content = ctk.CTkFrame(info_window, fg_color=bg_color)
        content.pack(fill='both', expand=True)
        theme_label = ctk.CTkLabel(content, text="Select Theme:", text_color=("white" if self.theme_var.get() == "Dark" else "black"))
        theme_label.pack(pady=10)
        theme_options = ["Light", "Dark"]
        theme_menu = ctk.CTkOptionMenu(
            content,
            values=theme_options,
            variable=self.theme_var,
            command=lambda t: [self.set_theme(t), info_window.configure(bg=("#242424" if t=="Dark" else "#f0f6fc")), content.configure(fg_color=("#242424" if t=="Dark" else "#f0f6fc")), theme_label.configure(text_color=("white" if t=="Dark" else "black")), mode_label.configure(text_color=("white" if t=="Dark" else "black")), version_label.configure(text_color=("white" if t=="Dark" else "black"))],
            fg_color="orange",
            button_color="orange",
            button_hover_color="#FF8C00"
        )
        theme_menu.pack(pady=10)
        mode_label = ctk.CTkLabel(content, text="Select Mode:", text_color=("white" if self.theme_var.get() == "Dark" else "black"))
        mode_label.pack(pady=5)
        mode_menu = ctk.CTkOptionMenu(
            content,
            values=["Dec", "Hex", "Oct", "Bin"],
            variable=self.mode_var,
            command=self._on_mode_change,
            fg_color="orange",
            button_color="orange",
            button_hover_color="#FF8C00"
        )
        mode_menu.pack(pady=5)
        version_label = ctk.CTkLabel(
            content,
            text="OrangCalc v2.0\nCreated by InterJava's Studios",
            text_color=("white" if self.theme_var.get() == "Dark" else "black")
        )
        version_label.pack(pady=10)
        close_button = ctk.CTkButton(
            content,
            text="Close",
            command=info_window.destroy,
            font=("Arial", 14),
            fg_color="red",
            text_color="white",
            width=100,
            height=40,
            hover_color="#FF4C4C"
        )
        close_button.pack(pady=10)
    def _on_mode_change(self, mode):
        self.entry.delete(0, ctk.END)
    def set_theme(self, theme):
        ctk.set_appearance_mode(theme)
if __name__ == "__main__":
    app = OrangCalc()
    app.mainloop()
