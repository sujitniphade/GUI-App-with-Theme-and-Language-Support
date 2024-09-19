
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Language dictionaries (unchanged)
languages = {
    "English": {
        "username": "Username:",
        "password": "Password:",
        "option": "Select Option:",
        "login": "Login",
        "status": "Login Button Clicked",
        "title": "Form and Dropdown",
        "graph": "Graph",
        "theme": "Theme:",
        "language": "Language:"
    },
    "Marathi": {
        "username": "वापरकर्तानाव:",
        "password": "पासवर्ड:",
        "option": "पर्याय निवडा:",
        "login": "लॉगिन",
        "status": "लॉगिन बटण क्लिक केले",
        "title": "फॉर्म आणि ड्रॉपडाउन",
        "graph": "आलेख",
        "theme": "थीम:",
        "language": "भाषा:"
    },
    "French": {
        "username": "Nom d'utilisateur:",
        "password": "Mot de passe:",
        "option": "Sélectionnez une option:",
        "login": "Connexion",
        "status": "Bouton de connexion cliqué",
        "title": "Formulaire et Liste déroulante",
        "graph": "Graphique",
        "theme": "Thème:",
        "language": "Langue:"
    }
}

class ImprovedGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Login and Graph Application")
        self.root.geometry("800x600")
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.create_widgets()
        self.layout_widgets()
        
        # Set default language and theme
        self.language_var.set("English")
        self.theme_var.set("Light")
        self.update_language("English")
        self.toggle_theme("Light")

    def create_widgets(self):
        # Notebook
        self.notebook = ttk.Notebook(self.root)
        
        # Tab 1: Form and Dropdown
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Form and Dropdown")
        
        # Login Frame
        self.login_frame = ttk.Frame(self.tab1)
        
        self.label_username = ttk.Label(self.login_frame, text="Username:")
        self.entry_username = ttk.Entry(self.login_frame)
        
        self.label_password = ttk.Label(self.login_frame, text="Password:")
        self.entry_password = ttk.Entry(self.login_frame, show="*")
        
        self.label_dropdown = ttk.Label(self.login_frame, text="Select Option:")
        self.dropdown_var = tk.StringVar()
        self.dropdown_menu = ttk.Combobox(self.login_frame, textvariable=self.dropdown_var)
        self.dropdown_menu['values'] = ("Option 1", "Option 2", "Option 3")
        self.dropdown_menu.current(0)
        
        self.btn_login = ttk.Button(self.login_frame, text="Login", command=self.login_clicked)
        
        self.label_status = ttk.Label(self.login_frame, text="")
        
        # Tab 2: Graph
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Graph")
        
        # Theme and Language selection
        self.settings_frame = ttk.Frame(self.root)
        
        self.theme_label = ttk.Label(self.settings_frame, text="Theme:")
        self.theme_var = tk.StringVar(value="Light")
        self.theme_light = ttk.Radiobutton(self.settings_frame, text="Light", variable=self.theme_var, value="Light",
                                           command=lambda: self.toggle_theme("Light"))
        self.theme_dark = ttk.Radiobutton(self.settings_frame, text="Dark", variable=self.theme_var, value="Dark",
                                          command=lambda: self.toggle_theme("Dark"))
        
        self.language_label = ttk.Label(self.settings_frame, text="Language:")
        self.language_var = tk.StringVar(value="English")
        self.language_dropdown = ttk.Combobox(self.settings_frame, textvariable=self.language_var,
                                              values=("English", "Marathi", "French"))
        self.language_dropdown.bind("<<ComboboxSelected>>", lambda event: self.update_language(self.language_var.get()))

    def layout_widgets(self):
        # Main layout
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        self.settings_frame.pack(fill='x', padx=10, pady=10)
        
        # Login Frame layout
        self.login_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        self.label_username.grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.entry_username.grid(row=0, column=1, sticky='we', padx=5, pady=5)
        
        self.label_password.grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.entry_password.grid(row=1, column=1, sticky='we', padx=5, pady=5)
        
        self.label_dropdown.grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.dropdown_menu.grid(row=2, column=1, sticky='we', padx=5, pady=5)
        
        self.btn_login.grid(row=3, column=0, columnspan=2, pady=20)
        
        self.label_status.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.login_frame.columnconfigure(1, weight=1)
        
        # Graph layout
        self.create_graph()
        
        # Settings layout
        self.theme_label.pack(side='left', padx=(0, 5))
        self.theme_light.pack(side='left', padx=(0, 5))
        self.theme_dark.pack(side='left', padx=(0, 5))
        self.language_label.pack(side='left', padx=(20, 5))
        self.language_dropdown.pack(side='left', padx=(0, 5))

    def create_graph(self):
        x = [1, 2, 3, 4, 5]
        y = [1, 4, 9, 16, 25]

        self.fig, self.ax = plt.subplots(figsize=(6, 4), dpi=100)
        self.ax.plot(x, y, label='Sample Data', color='#1E90FF')
        self.ax.set_title('Graph Example')
        self.ax.set_xlabel('X axis')
        self.ax.set_ylabel('Y axis')
        self.ax.legend()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.tab2)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20, pady=20)

    def update_language(self, selected_language):
        language = languages[selected_language]

        self.label_username.config(text=language["username"])
        self.label_password.config(text=language["password"])
        self.label_dropdown.config(text=language["option"])
        self.btn_login.config(text=language["login"])
        self.notebook.tab(0, text=language["title"])
        self.notebook.tab(1, text=language["graph"])
        self.theme_label.config(text=language["theme"])
        self.language_label.config(text=language["language"])

    def toggle_theme(self, theme):
        if theme == "Dark":
            # Dark theme colors
            bg_color = "black"
            fg_color = "white"
            entry_bg = "gray"
            button_bg = "darkgray"
            button_fg = "white"
            hover_bg = "gray"

            self.style.configure("TFrame", background=bg_color)
            self.style.configure("TLabel", background=bg_color, foreground=fg_color)
            self.style.configure("TButton", background=button_bg, foreground=button_fg)
            self.style.map('TButton', background=[('active', hover_bg)])
            self.style.configure("TRadiobutton", background=bg_color, foreground=fg_color)
            self.style.configure("TCombobox", fieldbackground=entry_bg, background=entry_bg, foreground=fg_color)
            self.style.map('TCombobox', fieldbackground=[('readonly', entry_bg)])
            self.style.configure("TEntry", fieldbackground=entry_bg, foreground=fg_color)
            self.style.configure("TNotebook", background=bg_color)
            self.style.configure("TNotebook.Tab", background=bg_color, foreground=fg_color)
            
            # Update graph colors
            self.fig.patch.set_facecolor(bg_color)
            self.ax.set_facecolor(bg_color)
            self.ax.title.set_color(fg_color)
            self.ax.xaxis.label.set_color(fg_color)
            self.ax.yaxis.label.set_color(fg_color)
            self.ax.tick_params(axis='x', colors=fg_color)
            self.ax.tick_params(axis='y', colors=fg_color)
            self.ax.spines['bottom'].set_color(fg_color)
            self.ax.spines['top'].set_color(fg_color)
            self.ax.spines['right'].set_color(fg_color)
            self.ax.spines['left'].set_color(fg_color)
            
        else:
            # Light theme colors
            bg_color = "#F0F0F0"
            fg_color = "#000000"
            entry_bg = "#FFFFFF"
            button_bg = "#E0E0E0"
            button_fg = "#000000"
            hover_bg = "#D0D0D0"
            
            self.style.configure("TFrame", background=bg_color)
            self.style.configure("TLabel", background=bg_color, foreground=fg_color)
            self.style.configure("TButton", background=button_bg, foreground=button_fg)
            self.style.map('TButton', background=[('active', hover_bg)])
            self.style.configure("TRadiobutton", background=bg_color, foreground=fg_color)
            self.style.configure("TCombobox", fieldbackground=entry_bg, background=entry_bg, foreground=fg_color)
            self.style.map('TCombobox', fieldbackground=[('readonly', entry_bg)])
            self.style.configure("TEntry", fieldbackground=entry_bg, foreground=fg_color)
            self.style.configure("TNotebook", background=bg_color)
            self.style.configure("TNotebook.Tab", background=bg_color, foreground=fg_color)
            
            # Update graph colors
            self.fig.patch.set_facecolor(bg_color)
            self.ax.set_facecolor(bg_color)
            self.ax.title.set_color(fg_color)
            self.ax.xaxis.label.set_color(fg_color)
            self.ax.yaxis.label.set_color(fg_color)
            self.ax.tick_params(axis='x', colors=fg_color)
            self.ax.tick_params(axis='y', colors=fg_color)
            self.ax.spines['bottom'].set_color(fg_color)
            self.ax.spines['top'].set_color(fg_color)
            self.ax.spines['right'].set_color(fg_color)
            self.ax.spines['left'].set_color(fg_color)

        self.canvas.draw()
        self.root.update()


    def login_clicked(self):
        status_text = languages[self.language_var.get()]["status"]
        self.label_status.config(text=status_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImprovedGUI(root)
    root.mainloop()