import PySimpleGUI as sg3
import speech_recognition as sr
import PySimpleGUIQt as sg

sg.theme('Green')
sg.set_options(font=('Arial',14))
periexomeno=[[sg.Text("speech to text of Rihanna")],
        [sg.Multiline(size=(70,20),key="-horitikotita-")],
        [sg.Button("Record", button_color=("white", "gray"), border_width=18),
         sg.Button("exit", button_color=("white", "red"), border_width=10),
         sg.Button("Hide", button_color=("white", "blue"),border_width=10)]]
window=sg.Window('omilia se keimeno',periexomeno)
while True:
    event,values=window.read()
    if event=="exit" or event==sg.WIN_CLOSED:
        break
    elif event== "Record":
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            window["-horitikotita-"].update(text)
        except sr.UknownValueError:
            window["-horitikotita-"].update('Could not understand')
        except sr.RequestError as e:
            window["-horitikotita-"].update(f'ERROR:{e}')
    elif event== "Hide":
        window.Hide()
window.close()
        
            
