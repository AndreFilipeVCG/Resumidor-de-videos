import google.generativeai as ai
from pytubefix import YouTube
import os   
import whisper
import warnings

warnings.filterwarnings("ignore")
key= "AIzaSyBD31qKusoQhZqUi1Fbo_6DN41s7EuRj0c"

class resumo():
    def gerar(urlescolhida):
        ai.configure(api_key=key)
        model= ai.GenerativeModel("gemini-pro")
        chat = model.start_chat()
        url = urlescolhida
        yt = YouTube(url)
        # Seleciona e baixa o áudio
        audio = yt.streams.get_audio_only()
        audio_file = audio.download(filename="audio.mp3") 
        # Verifique se o arquivo foi baixado
        if not os.path.exists(audio_file):
            print(f"O arquivo {audio_file} não foi encontrado. Verifique o caminho.")
        else:
            # Carregue o modelo e faça a transcrição
            model = whisper.load_model("base")
            transcricao = model.transcribe(audio_file)
            texto= transcricao["text"]
            os.remove(audio_file)

        prompt="A seguir voce tem um script de um vídeo resuma ele e o explique"
        message=texto
        response = chat.send_message(prompt + message)
        return response.text 



