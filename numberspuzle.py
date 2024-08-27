import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import random
import time
start_time = time.time()
n = -1
runtime = 0
class MyApp(App):  
        def build(self):
            def adjasent(i,j):
                if abs(i-j) == 1:
                    return(True)
                elif abs(i-j) == 4:
                    return(True)
                else:
                    return(False)
            def callback(instance):
                globals()["n"] = n+1 
                id = self.buttons.index(instance)
                ids = numbers.index("")
                if adjasent(numbers.index(""),(id)):
                   numbers[id],numbers[ids] = "",numbers[id]
                   self.buttons[id].text, self.buttons[ids].text = "", self.buttons[id].text
                   if num == numbers:
                        end_time = time.time()
                        globals()["n"] = n+1
                        globals()["runtime"] = end_time-start_time
                        endbutton.text =  f"{round(runtime, 2)} másodperc alatt fejezte be a feladatot, {n} lépéssel"
            bottom = GridLayout(rows = 2, cols= 1)
            base = GridLayout(rows= 4, cols = 4)   
            self.buttons = []
            endbutton = Button(pos_hint ={"right":.6666,"top":.5},size_hint = [.3333,None])
            numbers = []
            num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,""]
            while len(numbers) <16:
                i = random.randint(0,15)
                if num[i] not in numbers:
                    try:
                        numbers.append(int(num[i]))
                    except ValueError:
                        numbers.append(num[i])
            """numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,""] test line for timer and move counter""" 
            for i in numbers:
                button = Button(text = f"{i}",on_press = callback,background_color = [0,0,0,1])
                self.buttons.append(button)
            for i in self.buttons:
                base.add_widget(i)
            bottom.add_widget(endbutton)
            bottom.add_widget(base)
            return(bottom)
if __name__ == '__main__':
    MyApp().run()
print(n, runtime)