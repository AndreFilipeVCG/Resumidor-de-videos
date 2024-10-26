import ai
import threading
import time

isrunning = True
content=""
class Process():
    def __init__(self):
        global isrunning ,content
        def checar():
            global isrunning, content
            while isrunning: 
                if content == "":
                    print("processando")
                else:
                    print(content)
                    isrunning = False  
                time.sleep(0.5) 

        thread = threading.Thread(target=checar) 
        thread.start()


    def resultado():
        return content


    def VideoUrl(url):
        content = ai.resumo.gerar(url)
        return content
