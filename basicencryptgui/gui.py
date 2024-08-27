import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from encrypt import encrypt,decrypt
class MyApp(App):  
        def build(self):
            gombok = FloatLayout()
            validate = Button(text = "encrypt", size_hint= [.2,None],pos_hint ={'right': .24})
            untitkosit = Button(text= "decrypt", size_hint = [.2,None],pos_hint ={'right': .48})
            cls = Button(text= "clear", size_hint = [.2,None],pos_hint ={'right': .72})
            write = Button(text="save",size_hint=[.2,None],pos_hint = {'right':.96})

            base = FloatLayout()
            Text = Label(text="text:" ,pos_hint ={"right":.3333,"top":.7},size_hint = [.2,None])
            Encypted = Label(text = "encrypt:",pos_hint ={"right":.3333,"top":.5},size_hint = [.2,None])
            titkos = TextInput(pos_hint ={"right":.6666,"top":.5},size_hint = [.3333,None])
            textinput = TextInput(text = "",pos_hint ={'right': 0.666666,"top":.7},size_hint = [.3333,None])

            def on_enter(instance):
                titkos.text = encrypt(textinput.text)
            def titkosit(instance):
                textinput.text = decrypt(titkos.text)
            def kilepes(instance):
                textinput.text= ""
                titkos.text = ""
            def mentes(instance):
                on_enter(Text)
                with open("file.txt","r+") as f:
                     f.writelines(f"\n{titkos.text}")
            validate.bind(on_press = on_enter)
            cls.bind(on_press= kilepes)
            untitkosit.bind(on_press= titkosit)
            write.bind(on_press = mentes)

            gombok.add_widget(validate)
            gombok.add_widget(untitkosit)
            gombok.add_widget(cls)
            gombok.add_widget(write)

            base.add_widget(Text)
            base.add_widget(Encypted)
            base.add_widget(textinput)
            base.add_widget(titkos)
            base.add_widget(gombok)

            return(base)
if __name__ == '__main__':
    MyApp().run()