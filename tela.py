import customtkinter as ctk
import threading
from process import Process

texto = ""
url = ""
root = ctk.CTk()
resp = ""

root.title("Resumidor de videos com ia")
root.geometry("900x600")

# função do botão
def confirm():
    global url ,resp
    url = txt.get()
    thread.start()
    #resumo.configure(text=url)
    pag1.pack_forget()

def result(texto):
    pag2.pack(pady=20, padx=20, fill="both", expand=True)
    resumo.configure(text=texto)

# primeira página
pag1 = ctk.CTkFrame(root)
pag1.pack(pady=20, padx=20, fill="both", expand=True)
label = ctk.CTkLabel(pag1, text="Insira a URL do vídeo abaixo")
label.pack(pady=5)

txt = ctk.CTkEntry(pag1, placeholder_text="URL")
txt.pack(pady=5)

conf_button = ctk.CTkButton(pag1, text="Confirm", command=confirm)
conf_button.pack(pady=5)

# segunda página
pag2 = ctk.CTkFrame(root)

resumo = ctk.CTkLabel(pag2)
resumo.pack(pady=5)

def geracao():
    #pegar a url
    resumo=""
    url_video = url
    #processar ela
    print("vai processar em")
    resumo = Process.VideoUrl(url_video)
    #Mostar na label
    result(resumo)

thread = threading.Thread(target=geracao) 


root.mainloop()        


