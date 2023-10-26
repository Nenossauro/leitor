import pyperclip,os,pyttsx3

history = []
os.system('cls')
engine = pyttsx3.init()
engine.say("Leitor, seu assistente de leitura python.")
engine.runAndWait()

while True:
    should_clear = len(history)

    if should_clear > 5: 
        os.system('cls')
        history.clear()
    text = pyperclip.waitForNewPaste(timeout=None)
    engine.say(text)
    engine.runAndWait()
    history.append(text)
    print("--------------------------")
    print("Texto:",text)
    print("Histórico:",history)
    print("__________________________")
    
