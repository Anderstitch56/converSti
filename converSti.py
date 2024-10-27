import PySimpleGUI as sg
from PySimpleGUI import Push
from pytubefix import YouTube
from moviepy.editor import *
import os

sg.theme ("Dark")
fontSize = ("Helvica", 12)

link = None



def menu():
    layout = [
        [sg.Text("BEM-VINDO(A) AO CONVERSTI", font=fontSize)],
        [sg.Image(filename="./backGround/alien.png")],
        [sg.Text("O QUE DESEJA BAIXAR ?", font=fontSize)],
        [Push(),sg.Button("MÚSICA", key="mp3", font=fontSize), sg.Button("VÍDEO", key="mp4", font=fontSize), Push()],
        [sg.Text("")],
        [sg.Button("SAIR", key="sair", font=fontSize)],
        [sg.Text("feito por Anderson O. (STITCH)")]
    ]

    return sg.Window("Menu", finalize="True", layout=layout,  size=(600,500), element_justification="c")

def baixaMp4():
    layout = [
        [sg.Text("COLOQUE O LINK DO VÍDEO AQUI", font=fontSize)],
        [sg.Input(key="linkMp4")],
        [sg.Button("BAIXAR", key="baixarMp4", font=fontSize)],
        [sg.Button("VOLTAR", key="voltar", font=fontSize), sg.Button("SAIR", key="sair", font=fontSize)]
    ]

    return sg.Window("Baixar vídeos", layout=layout, finalize="True", size=(500,200), element_justification="c")

def baixaMp3():
    layout = [
        [sg.Text("COLOQUE O LINK DA MÚSICA AQUI", font=fontSize)],
        [sg.Input(key="linkMp3")],
        [sg.Button("BAIXAR", key="baixarMp3", font=fontSize)],
        [sg.Button("VOLTAR", key="voltar",font=fontSize), sg.Button("SAIR", key="sair", font=fontSize)]
    ]

    return sg.Window("Baixar músicas", layout=layout, finalize="True", size=(500,200), element_justification="c")


janela1, janela2, janela3 = menu(), None, None

while True:
    window, event, value = sg.read_all_windows()

    if window == janela1 and event == sg.WIN_CLOSED or event == "sair":
        break
    if window == janela2 and event == sg.WIN_CLOSED or event == "sair":
        break
    if window == janela3 and event == sg.WIN_CLOSED or event == "sair":
        break
    

    if window == janela1 and event == "mp4":
        janela1.close()
        janela2 = baixaMp4()
    
    if window == janela1 and event == "mp3":
        janela1.close()
        janela3 = baixaMp3()
    
    if window == janela2 and event == "voltar":
        janela2.close()
        janela1 = menu()

    if window == janela3 and event == "voltar":
        janela3.close()
        janela1 = menu()
    
        

    if window == janela3 and event == "baixarMp3":
        try:
            link = str(value["linkMp3"])
            yt = YouTube(link)
            stream = yt.streams.filter(only_audio=True).first()
            arquivo_video = stream.download(output_path="./musicasBaixadas")

            # Converter para MP3
            arquivo_mp3 = arquivo_video.replace('.mp4', '.mp3')
            audio_clip = AudioFileClip(arquivo_video)
            sg.Popup("BAIXANDO, NÃO FECHE O PROGRAMA")
            audio_clip.write_audiofile(arquivo_mp3)
            audio_clip.close()

            # Remover o arquivo de vídeo
            os.remove(arquivo_video)

            verificaLink = True
            sg.Popup("DOWNLOAD CONCLUÍDO")
            
        except:
            verificaLink = False
            sg.Popup("POR FAVOR INSIRA O LINK OU ANEXE O LINK CORRETAMENTE")

    if window == janela2 and event == "baixarMp4":
        try:
            link = str(value["linkMp4"])
            yt = YouTube(link)
            stream = yt.streams.get_highest_resolution()
            sg.Popup("BAIXANDO, NÃO FECHE O PROGRAMA")
            stream.download(output_path="./videosBaixados")

            verificaLink = True
            sg.Popup("DOWNLOAD CONCLUÍDO")
        except:
            verificaLink = False
            sg.Popup("POR FAVOR INSIRA O LINK OU ANEXE O LINK CORRETAMENTE")

    