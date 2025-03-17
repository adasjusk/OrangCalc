import customtkinter as ctk
class OrangCalc(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("OrangCalculator")
        self.geometry("300x400")
        ctk.set_appearance_mode("Dark")
        self.theme_var = ctk.StringVar(value="Dark")
        self.iconbitmap("orange.ico")
        self.entry = ctk.CTkEntry(self, font=("Arial", 20), width=280, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)
        self.buttons = [
            ["CE", "C", "⌫", ":"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["i", "0", ".", "="],
        ]
        for row_index, row in enumerate(self.buttons):
            for col_index, button_text in enumerate(row):
                if button_text == "=":
                    button = ctk.CTkButton(
                        self, text=button_text, command=self.calculate,
                        font=("Arial", 18), fg_color="orange", text_color="black",
                        width=70, height=50, hover_color="2"
                    )
                elif button_text == "i":
                    button = ctk.CTkButton(
                        self, text=button_text, command=self.show_info,
                        font=("Arial", 18), fg_color="grey", width=70, height=50,
                        hover_color="darkgrey"
                    )
                else:
                    button = ctk.CTkButton(
                        self, text=button_text, command=lambda text=button_text: self.button_click(text),
                        font=("Arial", 18), fg_color="grey", width=70, height=50,
                        hover_color="darkgrey"
                    )
                button.grid(row=row_index + 1, column=col_index, padx=5, pady=5, sticky="nsew")
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
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, ctk.END)
            self.entry.insert(0, str(result))
        except Exception:
            self.entry.delete(0, ctk.END)
            self.entry.insert(0, "Error")
    def show_info(self):
        info_window = ctk.CTkToplevel(self)
        info_window.title("About The OrangCalc")
        info_window.geometry("300x220")
        info_window.iconbitmap("orange.ico")
        info_window.attributes("-topmost", True)
        theme_label = ctk.CTkLabel(info_window, text="Select Theme:")
        theme_label.pack(pady=10)
        theme_options = ["Light", "Dark"]
        theme_menu = ctk.CTkOptionMenu(
            info_window, values=theme_options, variable=self.theme_var,
            command=self.set_theme, fg_color="orange", button_color="orange", button_hover_color="#FF8C00"
        )
        theme_menu.pack(pady=10)
        version_label = ctk.CTkLabel(info_window, text="OrangCalc v1.0\nCreated by InterJava's Studios")
        version_label.pack(pady=10)
        close_button = ctk.CTkButton(
            info_window, text="Close", command=info_window.destroy,
            font=("Arial", 14), fg_color="red", text_color="white",
            width=100, height=40, hover_color="#FF4C4C"
        )
        close_button.pack(pady=10)
    def set_theme(self, theme):
        ctk.set_appearance_mode(theme)
if __name__ == "__main__":
    app = OrangCalc()
    app.mainloop()
