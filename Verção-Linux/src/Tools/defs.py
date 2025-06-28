from imports import *

# Verifica se tem internet
def internet():
    try:
        urllib.request.urlopen("https://www.google.com", timeout=5)
        return True
    except:
        return False

def JavaScriptDep():
    
    # Verifica se Node.js está instalado
    VerNode = shutil.which("node")
    if not VerNode:
        return [False, "Node.js não instalado!"]
    
    # Verifica se npm está instalado
    VerNpm = shutil.which("npm")
    if not VerNpm:
        return [False, "npm não instalado!"]

    if not internet():
        return [False, "Sem conexão com a internet!"]

    return [True, "OK"]
def PythonDep():
    # Verifica se o Python esta instalado
    VerPython = shutil.which("python3") or shutil.which("python")
    if not VerPython:
        return [False, "Python não intalado!"]

    return [True, "OK"]

def NomeValido(nome):
    # Caracteres proibidos (qualquer sistema)
    caracteres_invalidos = '<>:"/\\|?*$ #&][)(}{'

    # Nome vazio
    if nome == "":
        return False

    # Verifica se tem caractere inválido
    if re.search(f"[{re.escape(caracteres_invalidos)}]", nome):
        return False

    # Nomes reservados no Windows
    nomes_reservados = {
        "CON", "PRN", "AUX", "NUL",
        *[f"COM{i}" for i in range(1, 10)],
        *[f"LPT{i}" for i in range(1, 10)]
    }

    if nome.upper() in nomes_reservados:
        return False

    # Não pode terminar com espaço ou ponto
    if nome.endswith(" ") or nome.endswith("."):
        return False

    return True

def DirValido(diretorio, nome_projeto):
    if not diretorio:
        return False, "⚠️ Nenhum diretório selecionado."

    if not os.path.exists(diretorio):
        return False, "❌ Diretório não existe."

    if not os.path.isdir(diretorio):
        return False, "❌ O caminho selecionado não é uma pasta."

    if not os.access(diretorio, os.W_OK):
        return False, "❌ Sem permissão de escrita na pasta."

    caminho_final = os.path.join(diretorio, nome_projeto)
    if os.path.exists(caminho_final):
        return False, "⚠️ Já existe um projeto com esse nome na pasta."

    return True, ""

#
def DesktopDir():
    home = os.path.expanduser("~")
        
    # Opções possíveis (em português e inglês)
    opcoes = ["Desktop", "Área de Trabalho", "Escritorio"]
        
    for nome in opcoes:
        caminho = os.path.join(home, nome)
        if os.path.exists(caminho):
            return caminho

    # Se nenhuma pasta padrão for encontrada, volta pro home
    return home

# Def's para crias os ambientes virtuais:
def MK_Venv(nome, dir):

    # Cria a pasta do projeto
    DIR = os.path.join(dir, nome)
    os.makedirs(DIR, exist_ok=True)

    # Cria a venv
    subprocess.run(["python3", "-m", "venv", "venv"], cwd=DIR)


    # Cria a pasta src
    src_path = os.path.join(DIR, "src")
    os.makedirs(src_path, exist_ok=True)


    # Cria o arquivo app.py vazio dentro da pasta src
    app_py_path = os.path.join(src_path, "app.py")
    open(app_py_path, "w").close()

    return DIR

def MK_react(nome, dir, clear):
    PackageName = f"{nome}".lower()
    DIR = os.path.join(dir, PackageName)


    # Cria o ambiente React
    subprocess.run(
        ["npm", "create", "vite@latest", PackageName, nome, "--", "--template", "react"],
        cwd=dir
    )

    # Istalando as dependençias ( Node modulos )
    subprocess.run(
        ["npm", "install"],
        cwd=DIR
    )

    if clear:
        ViteSVG  = os.path.join(DIR, "public", "vite.svg")
        ReactSVG = os.path.join(DIR, "src", "assets", "react.svg")
        IndexCSS = os.path.join(DIR, "src", "index.css")
        AppJSX   = os.path.join(DIR, "src", "App.jsx")
        AppCSS   = os.path.join(DIR, "src", "App.css")

        ClearList = [ ViteSVG, ReactSVG, IndexCSS, AppJSX, AppCSS ]
        for i in ClearList:
            if os.path.exists(i):
                os.remove(i)

        DirMain = os.path.join(DIR, "src", "main.jsx")
        ArquivoMainEditado = """
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    {/* <App /> */}
  </StrictMode>,
)

"""

        with open(DirMain, "w") as f:
            f.write(ArquivoMainEditado)

    return DIR
