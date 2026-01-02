from tkinter import messagebox
import customtkinter as ctk
from CTkListbox import *
import tkinter as tk

from utils.file import load_config
from main import Instance

import threading
import time
import os

CONFIG = load_config("src/config.json")
APP_NAME = CONFIG["info"]["name"]

class InstanceGUI(ctk.CTkToplevel):
    def __init__(self, master, name, idx):
        super().__init__(master)
        
        self.name = name
        self.idx = idx
        self.instance = Instance(100)
        
        self.mainFrame = ctk.CTkFrame(self, fg_color="transparent")
        self.mainFrame.grid(row=0, column=0)
        
        self.create_header()
        self.create_body()
        
        self.protocol("WM_DELETE_WINDOW", self.hide)
        self.after(15, self.focus)
        
    def show(self):
        self.deiconify()
        self.lift()
        
        self.after(15, self.focus)
        
    def hide(self):
        self.withdraw()
    
    def create_header(self):
        self.headerFrame = ctk.CTkFrame(self.mainFrame, fg_color="transparent")
        self.headerFrame.pack()
        
        ctk.CTkLabel(self.headerFrame, text=f"Instance #{self.idx}", font=ctk.CTkFont(size=12)).grid(row=1, column=1, sticky="nsew")
        ctk.CTkLabel(self.headerFrame, text=self.name, font=ctk.CTkFont(size=15, weight="bold")).grid(row=2, column=1, sticky="nsew")
    
    def create_body(self):
        self.bodyFrame = ctk.CTkFrame(self.mainFrame)
        self.bodyFrame.pack(pady=10)

class JudgeGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.ACTIVE = True
        self.protocol("WM_DELETE_WINDOW", self.__on_close)

        self.title(APP_NAME)
        self.resizable(False, False)
        ctk.set_appearance_mode(CONFIG["gui"]["mode"])
        ctk.set_default_color_theme(CONFIG["gui"]["theme"])
        
        self.Instances: list[InstanceGUI] = []
        
        self.create_widgets()
        self.bind("<Button-1>", self.__focus)
        
    @staticmethod
    def is_ancestor(ancestor, descendant):
        ancestor_path = str(ancestor)
        descendant_path = str(descendant)
        
        return descendant_path.startswith(ancestor_path)
    
    def __focus(self, event = None):
        if not JudgeGUI.is_ancestor(self.instancesListbox, event.widget):
            try:
                self.instancesListbox.deactivate("all")
                self.openInstancesButton.configure(state="disabled")
                event.widget.focus()
            except tk.TclError:
                pass
        
    def __on_close(self, force_exit = True):
        if not messagebox.askyesno("Exit app", f"Are you sure to exit {APP_NAME}?", icon="warning"):
            return
        
        self.ACTIVE = False
        self.destroy()
        
        if force_exit:
            os._exit(0)
        
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
                
        self._headBodyFrame = ctk.CTkFrame(self.bodyFrame, fg_color="transparent")
        self._headBodyFrame.grid(row=1, column=1, padx=10, pady=(15, 5))
        
        self._bodyBodyFrame = ctk.CTkFrame(self.bodyFrame, fg_color="transparent")
        self._bodyBodyFrame.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        
        self.addInstanceButton = ctk.CTkButton(self._headBodyFrame, text="Add", width=75,
                                               command=self._addInstance)
        self.addInstanceButton.grid(row=1, column=1, padx=(6, 3))
        
        self.removeInstanceButton = ctk.CTkButton(self._headBodyFrame, text="Remove", fg_color="red",
                                                  hover_color="darkred", width=75, state="disabled",
                                                  text_color_disabled="#8B8B8B",
                                                  command=self._deleteInstance)
        self.removeInstanceButton.grid(row=1, column=2, padx=3)
        
        self.openInstancesButton = ctk.CTkButton(self._headBodyFrame, text="Open", width=40,
                                                  state="disabled",
                                                  text_color_disabled="#7A7A7A",
                                                  command=self._openInstance)
        self.openInstancesButton.grid(row=1, column=3, padx=(3, 6))
        
            
        self.instancesListbox = CTkListbox(self._bodyBodyFrame, multiple_selection=False)
        self.instancesListbox.pack(fill="both")
        
        self.instancesListbox.bind("<Double-Button-1>", self._openInstance)
        self.instancesListbox.bind("<<ListboxSelect>>", self._on_select)
        
    def _on_select(self, _):
        select = self.instancesListbox.curselection() # >= 0 for single selection
        if select is not None or select >= 0:
            self.openInstancesButton.configure(state="normal")
        else:
            self.openInstancesButton.configure(state="disabled")

    def _openInstance(self, _ = None):
        selected = self.instancesListbox.curselection()
        self.Instances[selected].show()
        
        # selected = self.instancesListbox.curselection()        
        # for index in selected:
        #     self.Instances[index].show()
        
    def _addInstance(self):
        inputNameDialog = ctk.CTkInputDialog(text="Instance name:", title="Name")
        
        def post_init():
            inputNameDialog._entry.insert(0, f"Instance #{len(self.Instances) + 1}")
            inputNameDialog._entry.select_range(0, "end")
            inputNameDialog._entry.focus()
        
        inputNameDialog.after(15, post_init)
        
        instanceName = inputNameDialog.get_input()
        if instanceName is None or not instanceName.strip():
            return
        
        for available in self.Instances:
            if instanceName == available.name:
                messagebox.showwarning("Instance existed", "An instance with this name already exists.")
                return
        
        newInstance = InstanceGUI(self, name=instanceName, idx=len(self.Instances) + 1)
        
        self.Instances.append(newInstance)
        self.instancesListbox.insert("end", newInstance.name)
        
        self.removeInstanceButton.configure(state="normal")
        
    def _deleteInstance(self):
        select = self.instancesListbox.curselection()
        if select is None or not select >= 0:
            if messagebox.askyesno("Remove ALL instances", "Do you want to remove ALL instances?"):
                for instance in self.Instances:
                    instance.destroy()
                
                self.instancesListbox.delete(0, "end")
                self.Instances.clear()
        elif messagebox.askyesno("Remove instance(s)", f"Do you want to remove selected instance?"):
            self.instancesListbox.delete(select)
            
            self.Instances[select].destroy()
            self.Instances.pop(select)
               
        if len(self.Instances) == 0:
            self.removeInstanceButton.configure(state="disabled")
        
    def __deleteInstanceMultiselection(self):
        select = self.instancesListbox.curselection()
        if not select:
            if messagebox.askyesno("Remove ALL instances", "Do you want to remove ALL instances?"):
                for instance in self.Instances:
                    instance.destroy()
                
                self.instancesListbox.delete(0, "end")
                self.Instances.clear()
        elif messagebox.askyesno("Remove instance(s)", f"Do you want to remove {len(select)} selected instance(s)?"):
            for index in reversed(select):
               self.instancesListbox.delete(index)
               
               self.Instances[index].destroy()
               self.Instances.pop(index)
               
        if len(self.Instances) == 0:
            self.removeInstanceButton.configure(state="disabled")
        
        
    def create_footer(self):
        self.footerFrame = ctk.CTkFrame(self.mainFrame, fg_color="transparent")
        self.footerFrame.grid(row=3, column=1)
        
        ctk.CTkLabel(self.footerFrame, text="Made by", font=ctk.CTkFont(size=10)).grid(row=1, column=1, padx=3)
                
        self.authorLabel = ctk.CTkLabel(self.footerFrame, text=CONFIG["info"]["author"], font=ctk.CTkFont(size=11, weight="bold"))
        self.authorLabel.grid(row=1, column=2, sticky="s")


if __name__ == "__main__":
    app = JudgeGUI()
    app.mainloop()
