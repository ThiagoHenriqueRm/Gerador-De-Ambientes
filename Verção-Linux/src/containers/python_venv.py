from imports import *
from Tools import MK_Venv, PythonDep, NomeValido, DirValido, DesktopDir


def Python_Venv():

    def SelecionarDir():
        DirInicial = DesktopDir()

        pasta = filedialog.askdirectory(title="Escolha a pasta", initialdir=DirInicial)
        if pasta:
            DIR.configure(state="normal")
            DIR.delete(0, "end")
            DIR.insert(0, pasta)
            DIR.configure(state="readonly")

    def CriarProjeto(): 
        statusLabel.configure(text="🛠 Criando projeto...", text_color="#E9C226")
        statusLabel.update()

        # Verifidando dependencias
        Ver = PythonDep()
        if Ver[0] == False:
            statusLabel.configure(text=Ver[1], text_color="#F44336")
            return
        
        # Tente Criar o Projeto
        else:
            nome = Nome.get()
            dir  = DIR.get()

            openPasta =  checkbox_pasta.get()
            openCode  =  checkbox_vscode.get()


            # Validações 
            nomeOK = NomeValido(nome)
            dirOK, msg = DirValido(dir, nome)
            
            if not nomeOK and not dirOK:
                statusLabel.configure(
                    text="❌ Nome do projeto inválido\n❌ " + msg,
                    text_color="#F44336"
                )
                return
            if not nomeOK:
                statusLabel.configure(text="❌ Nome inválido para o projeto.", text_color="#F44336")
                return
            if not dirOK:
                statusLabel.configure(text=msg, text_color="#F44336")
                return


            # Criação do projeto
            DirProjeto = MK_Venv(nome, dir)
            statusLabel.configure(
                    text       = " \n Projeto Criado! \n" + f"{DirProjeto}",
                    text_color = "#138D19"
                )

            # Executa a opção de abrir no VSCode
            if openCode:
                subprocess.run(["code", DirProjeto])

            # Executa a opção de abrir a pasta no gerenciador de arquivos
            if openPasta:
                if platform.startswith("linux"):
                    subprocess.run(["open", DirProjeto])
                elif platform == "win32":
                    os.startfile(DirProjeto)
                elif platform == "darwin":
                    subprocess.run(["open", DirProjeto])


    CTK.set_appearance_mode("dark")
    CTK.set_default_color_theme("dark-blue")

    app = CTK.CTk()
    app.title(" PYTHON VENV ")
    app.geometry("460x320")
    app.resizable(False, False)
    app.configure(fg_color="#1e1e2e")
    FONTE = CTK.CTkFont(family="Arial", size=13, weight="bold")


    # Entrada pro nome do projeto
    Nome = CTK.CTkEntry(
        master           = app, 
        placeholder_text = "NOME DO PROJETO",
        width            = 400,
        font             = FONTE,
        fg_color         = "#161624",
        border_width     = 0
    );Nome.pack(pady=(20, 4))


    # Entrada pro diretorio do projeto
    frame_dir = CTK.CTkFrame(app, fg_color="#1e1e2e")
    frame_dir.pack(pady=3)
    DIR = CTK.CTkEntry(
        master           = frame_dir,
        width            = 310,
        fg_color         = "#161624",
        border_width     = 0
    );DIR.pack(side="left", padx=5)
    DIR.insert(0, "Diretorio do projeto")
    DIR.configure(state="readonly", font=FONTE,)


    # Botão pra selecionar o diretorio
    btn_selecionar = CTK.CTkButton(frame_dir, text="📂", width=85, command=SelecionarDir)
    btn_selecionar.pack(side="right")


    # Frame para as Checkboxs
    ChecFrame = CTK.CTkFrame(
        border_width = 14,
        master       = app,
        fg_color     = "#181824",
        border_color = "#181824"
    );ChecFrame.pack(pady=5, padx=10)


    # Checkbox: VSCode
    checkbox_vscode = CTK.CTkCheckBox(
        checkbox_width  = 18,
        checkbox_height = 18,
        master          = ChecFrame,
        text            = "ABRIR NO VSCODE APÓS CRIAR?",
        font            = FONTE,
        border_width    = 2,
        corner_radius   = 5
    );checkbox_vscode.pack(pady=(10, 1), anchor="w", padx=10)

    VerCode = shutil.which("code")
    if not VerCode:
        checkbox_vscode.deselect()
        checkbox_vscode.configure(state="disabled")


    # Checkbox: Abrir pasta
    checkbox_pasta = CTK.CTkCheckBox(
        checkbox_width  = 18,
        checkbox_height = 18,
        master          = ChecFrame,
        text            = "ABRIR A PASTA APÓS CRIAR?",
        font            = FONTE,
        border_width    = 2,
        corner_radius   = 5
    );checkbox_pasta.pack(pady=(0, 10), anchor="w", padx=10)


    # Status 
    statusLabel = CTK.CTkLabel(app, text=" - - -", text_color="#CCCCCC", font=FONTE)
    statusLabel.pack(pady=5)

 
    # Botão criar projeto
    btn_criar = CTK.CTkButton(
        master   = app, 
        text     = " CRIAR PROJETO ",
        font     = FONTE,
        height   = 35,
        command  = CriarProjeto
    );btn_criar.pack(pady=20)

    app.mainloop()
