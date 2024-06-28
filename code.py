from tkinter import *
from pytube import YouTube
from os import startfile, getcwd
from threading import Thread

#  fazer o threading direito ai vou ser mt pika

def comecar_baixar():
    Thread(target=baixar).start()

def baixar():
    try:
        global botao
        global stats 
        global colocar_url
        Url = str(colocar_url.get()).strip()
        nome = YouTube(Url).title
        

        # comecou download...
        botao.config(state=DISABLED)
        stats.config(text=f'baixando \n{nome}') 
        audio = YouTube(Url).streams.filter(only_audio=True).first()
        audio.download( output_path='./Audios baixados', filename=nome + '.mp3')

        # terminou download
        botao.config(state=NORMAL)
        startfile(getcwd() + '/Audios baixados')
        stats.config(text=f'Finalizado :)', font=("-weight bold", 14))
        colocar_url.delete(0, 'end')
        
        
    except Exception as erro:
        stats.config(text=f'Algo deu errado...\n{erro}')

# parte do tkinter
tela = Tk()

icon =  PhotoImage(file='./icon/iconjojo.png')

tela.title("Baixador by RecantodoJohn")
tela.iconphoto(True,icon)
tela.config(bg=('#78243f'))
tela.geometry("330x300")
tela.resizable(0, 0)

titulo = Label(
    text=f'-=| Baixador de audio |=-',
    font=("-weight bold", 20),
    
    bg='#78243f',
    fg='#24061d',
)
titulo.pack()

quadro = Frame(
    tela,
    width=300,
    pady=15,
    bg='#78243f',
)
quadro.pack()

nome_url = Label(
    quadro,
    text='Coloque o Link do video do Youtube abaixo:',
    font=("Arial", 12),
    bg='#78243f',
    fg='#24061d',
)
nome_url.pack()


colocar_url = Entry(
    quadro,
    font=("Arial", 12),
    width=30,
)
colocar_url.pack(pady=5)


botao = Button(
    quadro,
    text="Baixar",
    command=comecar_baixar,
    font=("Arial", 15),
    bg='#d2632c',
    fg='#24061d',
)
botao.pack()

stats = Label(
    font=("Arial", 12),
    bg='#78243f',
    fg='#24061d',
    wraplength=250
)
stats.pack()

tela.mainloop()