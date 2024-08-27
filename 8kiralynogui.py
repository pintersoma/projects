import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
def modeswap(x):
    if swap:
        globals()['swap'] = False
    else:
        globals()['swap'] = True
swap = False
class MyApp(App):  
        def build(self):
            def ut(pos1, pos2):
                if pos1%10 == pos2%10:
                    return(True)
                elif pos1//10 == pos2//10:
                    return(True)
                elif abs(pos1//10 - pos2//10) == abs(pos1%10 - pos2%10):
                    return(True)
                return(False)
            kulcs = [[11, 25, 38, 46, 53, 67, 72, 84], [11, 26, 38, 43, 57, 64, 72, 85], [11, 27, 34, 46, 58, 62, 75, 83], [11, 27, 35, 48, 52, 64, 76, 83], [12, 24, 36, 48, 53, 61, 77, 85], [12, 25, 37, 41, 53, 68, 76, 84], [12, 25, 37, 44, 51, 68, 76, 83], [12, 26, 31, 47, 54, 68, 73, 85], [12, 26, 38, 43, 51, 64, 77, 85], [12, 27, 33, 46, 58, 65, 71, 84], [12, 27, 35, 48, 51, 64, 76, 83], [12, 28, 36, 41, 53, 65, 77, 84], [13, 21, 37, 45, 58, 62, 74, 86], [13, 25, 32, 48, 51, 67, 74, 86], [13, 25, 32, 48, 56, 64, 77, 81], [13, 25, 37, 41, 54, 62, 78, 86], [13, 25, 38, 44, 51, 67, 72, 86], [13, 26, 32, 45, 58, 61, 77, 84], [13, 26, 32, 47, 51, 64, 78, 85], [13, 26, 32, 47, 55, 61, 78, 84], [13, 26, 34, 41, 58, 65, 77, 82], [13, 26, 34, 42, 58, 65, 77, 81], [13, 26, 38, 41, 54, 67, 75, 82], [13, 26, 38, 41, 55, 67, 72, 84], [13, 26, 38, 42, 54, 61, 77, 85], [13, 27, 32, 48, 55, 61, 74, 86], [13, 27, 32, 48, 56, 64, 71, 85], [13, 28, 34, 47, 51, 66, 72, 85], [14, 21, 35, 48, 52, 67, 73, 86], [14, 21, 35, 48, 56, 63, 77, 82], [14, 22, 35, 48, 56, 61, 73, 87], [14, 22, 37, 43, 56, 68, 71, 85], [14, 22, 37, 43, 56, 68, 75, 81], [14, 22, 37, 45, 51, 68, 76, 83], [14, 22, 38, 45, 57, 61, 73, 86], [14, 22, 38, 46, 51, 63, 75, 87], [14, 26, 31, 45, 52, 68, 73, 87], [14, 26, 38, 42, 57, 61, 73, 85], [14, 26, 38, 43, 51, 67, 75, 82], [14, 27, 31, 48, 55, 62, 76, 83], [14, 27, 33, 48, 52, 65, 71, 86], [14, 27, 35, 42, 56, 61, 73, 88], [14, 27, 35, 43, 51, 66, 78, 82], [14, 28, 31, 43, 56, 62, 77, 85], [14, 28, 31, 45, 57, 62, 76, 83], [14, 28, 35, 43, 51, 67, 72, 86], [15, 21, 34, 46, 58, 62, 77, 83], [15, 21, 38, 44, 52, 67, 73, 86], [15, 21, 38, 46, 53, 67, 72, 84], [15, 22, 34, 46, 58, 63, 71, 87], [15, 22, 34, 47, 53, 68, 76, 81], [15, 22, 36, 41, 57, 64, 78, 83], [15, 22, 38, 41, 54, 67, 73, 86], [15, 23, 31, 46, 58, 62, 74, 87], [15, 23, 31, 47, 52, 68, 76, 84], [15, 23, 38, 44, 57, 61, 76, 82], [15, 27, 31, 43, 58, 66, 74, 82], [15, 27, 31, 44, 52, 68, 76, 83], [15, 27, 32, 44, 58, 61, 73, 86], [15, 27, 32, 46, 53, 61, 74, 88], [15, 27, 32, 46, 53, 61, 78, 84], [15, 27, 34, 41, 53, 68, 76, 82], [15, 28, 34, 41, 53, 66, 72, 87], [15, 28, 34, 41, 57, 62, 76, 83], [16, 21, 35, 42, 58, 63, 77, 84], [16, 22, 37, 41, 53, 65, 78, 84], [16, 22, 37, 41, 54, 68, 75, 83], [16, 23, 31, 47, 55, 68, 72, 84], [16, 23, 31, 48, 54, 62, 77, 85], [16, 23, 31, 48, 55, 62, 74, 87], [16, 23, 35, 47, 51, 64, 72, 88], [16, 23, 35, 48, 51, 64, 72, 87], [16, 23, 37, 42, 54, 68, 71, 85], [16, 23, 37, 42, 58, 65, 71, 84], [16, 23, 37, 44, 51, 68, 72, 85], [16, 24, 31, 45, 58, 62, 77, 83], [16, 24, 32, 48, 55, 67, 71, 83], [16, 24, 37, 41, 53, 65, 72, 88], [16, 24, 37, 41, 58, 62, 75, 83], [16, 28, 32, 44, 51, 67, 75, 83], [17, 21, 33, 48, 56, 64, 72, 85], [17, 22, 34, 41, 58, 65, 73, 86], [17, 22, 36, 43, 51, 64, 78, 85], [17, 23, 31, 46, 58, 65, 72, 84], [17, 23, 38, 42, 55, 61, 76, 84], [17, 24, 32, 45, 58, 61, 73, 86], [17, 24, 32, 48, 56, 61, 73, 85], [17, 25, 33, 41, 56, 68, 72, 84], [18, 22, 34, 41, 57, 65, 73, 86], [18, 22, 35, 43, 51, 67, 74, 86], [18, 23, 31, 46, 52, 65, 77, 84], [18, 24, 31, 43, 56, 62, 77, 85]]
            def colorin(id):
                if id//10%2 == 1 and id%2 == 0:
                    return(0,0,0,1)
                elif id//10%2 == 1 and id%2 == 1:
                    return(0,1,1,1)
                elif id//10%2 == 0 and id%2 == 1:
                    return(0,0,0,1)
                elif id//10%2 == 0 and id%2 == 0:
                    return(0,1,1,1)
            kiralynok = []
            def callback(instance):
                piros = False
                id = int(self.buttons[self.buttons.index(instance)].text)
                if swap:
                    if id in kiralynok:
                        kiralynok.remove(id)
                        self.buttons[self.buttons.index(instance)].background_color = (colorin(id))
                        self.buttons[self.buttons.index(instance)].color = (3,3,3,1)
                        for i in pos:
                                if ut(id,i) and i != id:
                                    self.buttons[(i//10-1)*8+i%10-1].background_color = (colorin(i))
                                for j in kiralynok:
                                    if ut(j,i) and i!=j:
                                        self.buttons[(i//10-1)*8+i%10-1].background_color = (3,1,0,1)
                                    elif j==i:
                                        self.buttons[(i//10-1)*8+i%10-1].background_color = (3,3,3,1)
                                for k in kiralynok:
                                    if ut(id,k) and k != id:
                                        piros = True
                                    if piros:
                                        self.buttons[self.buttons.index(instance)].background_color = (3,1,0,1)
                                        self.buttons[self.buttons.index(instance)].color = (3,3,3,1)
                    else:
                        for i in pos:
                            if ut(id,i) and i != id:
                                self.buttons[(i//10-1)*8+i%10-1].background_color = (3,1,0,1)
                        kiralynok.append(id)
                        self.buttons[self.buttons.index(instance)].background_color = (3,3,3,1)
                        self.buttons[self.buttons.index(instance)].color = (0,0,0,1)
                        for i in kiralynok:
                            if ut(i,id) and i != id:
                                piros = True
                        if piros:
                            self.buttons[self.buttons.index(instance)].background_color = (3,0,0,1)
                            self.buttons[self.buttons.index(instance)].color = (0,0,0,1)
                    textinput.text = str(kiralynok)

                else:
                    if id in kiralynok:
                        kiralynok.remove(id)
                        self.buttons[self.buttons.index(instance)].background_color = (colorin(id))
                        self.buttons[self.buttons.index(instance)].color = (3,3,3,1)
                    else:
                        kiralynok.append(id)
                        self.buttons[self.buttons.index(instance)].background_color = (3,3,3,1)
                        self.buttons[self.buttons.index(instance)].color = (0,0,0,1)
                        for i in kiralynok:
                            if ut(i,id) and i != id:
                                piros = True
                        if piros:
                            self.buttons[self.buttons.index(instance)].background_color = (3,0,0,1)
                            self.buttons[self.buttons.index(instance)].color = (0,0,0,1)
                    textinput.text = str(kiralynok)
            

            def on_enter(instance):
                piros = False
                kiralynok = textinput.text[1:len(textinput.text)-1].strip().split(",")
                for i in kiralynok:
                    i = int(i)
                    piros = False
                    self.buttons[(i//10-1)*8+i%10-1].background_color = (3,3,3,1)
                    self.buttons[(i//10-1)*8+i%10-1].color = (0,0,0,1)
                    for j in kiralynok:
                        if ut(int(j),int(i)) and int(i) != int(j):
                            piros = True
                    if piros:
                        self.buttons[(i//10-1)*8+i%10-1].background_color = (3,0,0,1)
                        self.buttons[(i//10-1)*8+i%10-1].color = (0,0,0,1)
            
            
            base = GridLayout(rows =3,cols=1)
            grid = GridLayout(rows= 8, cols = 8)
            mode = Button(text = "mode swap",on_press = modeswap, pos_hint ={"right":.6666,"top":.5},size_hint = [.3333,None])
            textinput = TextInput(text = "",on_text_validate = on_enter,pos_hint ={"right":.6666,"top":.5},size_hint = [.3333,None],multiline = False)
            self.buttons = []
            pos = [ 11, 12, 13, 14, 15, 16, 17, 18,
                    21, 22, 23, 24, 25, 26, 27, 28,
                    31, 32, 33, 34, 35, 36, 37, 38,
                    41, 42, 43, 44, 45, 46, 47, 48,
                    51, 52, 53, 54, 55, 56, 57, 58,
                    61, 62, 63, 64, 65, 66, 67, 68,
                    71, 72, 73, 74, 75, 76, 77, 78,
                    81, 82, 83, 84, 85, 86, 87, 88]
            

            for i in pos:
                button = Button(text = f"{i}",on_press = callback,background_color = (colorin(i)))
                self.buttons.append(button)
            
            for i in self.buttons:
                 grid.add_widget(i)
            base.add_widget(textinput)
            base.add_widget(grid)
            base.add_widget(mode)
            return(base)

if __name__ == '__main__':
    MyApp().run()