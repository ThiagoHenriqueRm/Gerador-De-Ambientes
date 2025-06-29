from Tools import *
from containers import *

CTK.set_appearance_mode("dark")
CTK.set_default_color_theme("blue")

app = CTK.CTk()
app.title("Criador de Projeto")
app.geometry("400x250")
app.resizable(False, False)
app.configure(fg_color="#1e1e2e")
FONTE = CTK.CTkFont(family="Arial", size=13, weight="bold")

# Frama Titulo
FRM_TITULO = CTK.CTkFrame(
    master        = app,
    fg_color      = "#181824",
    border_color  = "#181824",
    height        = 30,
);FRM_TITULO.pack(pady=(20, 0))
TITULO_FONTE = CTK.CTkFont(family="Arial", size=20, weight="bold")
TITULO = CTK.CTkLabel(
    master = FRM_TITULO,
    text   = "CRIADOR DE PROJETOS",
    font   = TITULO_FONTE,
    width  = 327,
);TITULO.pack()


# Frama Conteiner 
Conteriner = CTK.CTkFrame(
    master   = app,
    fg_color = "#1e1e2e"
);Conteriner.pack(pady=(5, 0))


# Frame Python:
FramePython = CTK.CTkFrame(
    master        = Conteriner,
    fg_color      = "#181824",
    border_color  = "#181824",
    border_width  = 20,
);FramePython.pack(side="left", padx=(5, 0), pady=(1, 1))

PyTitulo = CTK.CTkLabel(
    master = FramePython,
    text   = "PYTHON"
);PyTitulo.pack()

Python_venv = CTK.CTkButton(
    master  = FramePython, 
    command = Python_Venv,
    text    = "PYTHON VENV", 
    font    = FONTE,
    height  = 35,
);Python_venv.pack(pady=10, padx=10)


# Frame JavaScript :
FrameJavaScript = CTK.CTkFrame(
    master        = Conteriner,
    fg_color      = "#181824",
    border_color  = "#181824",
    border_width  = 20,
);FrameJavaScript.pack(side="left", padx=5, pady=(1, 1))

JsTitulo = CTK.CTkLabel(
    master = FrameJavaScript,
    text   = "JAVASCRIPT"
);JsTitulo.pack()

JavaScript_react = CTK.CTkButton(
    master  = FrameJavaScript,
    command = Javascript_React,
    text    = "JAVASCRIPT REACT", 
    font    = FONTE,
    height  = 35,
);JavaScript_react.pack(pady=10, padx=10)


app.mainloop()
