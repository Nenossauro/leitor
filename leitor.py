import pyperclip,os,pyttsx3

historico = []
os.system('cls')
motor_tts = pyttsx3.init()
motor_tts.say("Leitor, seu assistente de leitura python.")
motor_tts.runAndWait()

while True:
    devo_limpar = len(historico)

    if devo_limpar > 5: 
        os.system('cls')
        historico.clear()
    texto = pyperclip.waitForNewPaste(timeout=None)
    motor_tts.say(texto)
    motor_tts.runAndWait()
    historico.append(texto)
    print("--------------------------")
    print("Texto:",texto)
    print("Histórico:",historico)
    print("__________________________")
    
