import customtkinter as ctk
from utils.file import load_config
import threading
import time

import os

CONFIG = load_config("src/config.json")
APP_NAME = CONFIG["info"]["name"]

class JudgeGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.ACTIVE = True
        self.protocol("WM_DELETE_WINDOW", self.__on_close)

        self.title(APP_NAME)
        ctk.set_appearance_mode(CONFIG["gui"]["mode"])
        ctk.set_default_color_theme(CONFIG["gui"]["theme"])
        
        self.create_widgets()
        
    def create_widgets(self):
        self.mainFrame = ctk.CTkFrame(self, fg_color="transparent")
        self.mainFrame.grid(row=1, column=1, padx=10, pady=10)
        
        self.create_header()
        self.create_body()
        self.create_footer()
    
    def create_header(self):
        self.headerFrame = ctk.CTkFrame(self.mainFrame, fg_color="transparent")
        self.headerFrame.grid(row=1, column=1, pady=(0,10))
        
        self.headerLabel = ctk.CTkLabel(self.headerFrame, text=f"Welcome to {APP_NAME}!", font=ctk.CTkFont(size=20, weight="bold"))
        self.headerLabel.grid(row=1, column=1)
        
        self._animatedTextFrame = ctk.CTkFrame(self.headerFrame, fg_color="transparent")
        self._animatedTextFrame.grid(row=2, column=1)
        
        ctk.CTkLabel(self._animatedTextFrame, text="Your").grid(row=1, column=1, padx=5)
        ctk.CTkLabel(self._animatedTextFrame, text="stress tester").grid(row=1, column=3, padx=5)
        
        self._animatedSample = ["modern", "simple", "fast", "accurate", "reliable"]
        self._animatedText = ctk.CTkLabel(self._animatedTextFrame, text="test", font=ctk.CTkFont(weight="bold"))
        self._animatedText.grid(row=1, column=2)
        
        self._animatedThread = threading.Thread(target=self._header_animation)
        self._animatedThread.start()
        
    def __on_close(self, force_exit = True):
        self.ACTIVE = False
        self.destroy()
        
        if force_exit:
            os._exit(0)
    
    def _header_animation(self, duration = 0.1, gap = 1):
        curIdx = 0
        try:
            while self.ACTIVE:
                curText = ""
                for i in range(len(self._animatedSample[curIdx])):
                    curText += self._animatedSample[curIdx][i]
                    self._animatedText.configure(text=curText)
                    
                    if not self.ACTIVE:
                        return
                    
                    time.sleep(duration)
                    
                time.sleep(gap)
                
                while curText != "":
                    curText = curText[:-1]
                    self._animatedText.configure(text=curText)   
                    
                    if not self.ACTIVE:
                        return                 
                    
                    time.sleep(duration)
                
                curIdx = (curIdx + 1) % len(self._animatedSample)                    
                time.sleep(gap)
                
        except:
            return
        
    def create_body(self):        
        self.bodyFrame = ctk.CTkFrame(self.mainFrame)
        self.bodyFrame.grid(row=2, column=1)
        
    def create_footer(self):
        self.footerFrame = ctk.CTkFrame(self.mainFrame, fg_color="transparent")
        self.footerFrame.grid(row=3, column=1)
        
        self.authorLabel = ctk.CTkLabel(self.footerFrame, text="Made by " + CONFIG["info"]["author"], font=ctk.CTkFont(size=10))
        self.authorLabel.grid(row=1, column=1, sticky="s")


if __name__ == "__main__":
    app = JudgeGUI()
    app.mainloop()
