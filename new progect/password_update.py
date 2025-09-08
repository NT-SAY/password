import secrets
import hashlib
import customtkinter as ctk
from tkinter import messagebox

class PasswordApp:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        self.app = ctk.CTk()
        self.app.title("generate password")
        self.app.geometry("400x400")
        self.create_widgets()
    
    def create_widgets(self):
        ctk.CTkLabel(self.app, text="length password:").pack(pady=5)
        self.length_entry = ctk.CTkEntry(self.app, width=100)
        self.length_entry.pack(pady=5)
        self.length_entry.insert(0, "12")
        
    
        ctk.CTkButton(self.app, text="generate", command=self.generate).pack(pady=10)
                
        self.password_label = ctk.CTkLabel(self.app, text="password")
        self.password_label.pack(pady=10)
                
        ctk.CTkLabel(self.app, text="algoritm:").pack(pady=5)
        self.alg_var = ctk.StringVar(value="sha256")
        alg_menu = ctk.CTkOptionMenu(self.app, variable=self.alg_var, 
                                   values=sorted(list(hashlib.algorithms_available)))
        alg_menu.pack(pady=5)
        
        
        ctk.CTkButton(self.app, text="hashing", command=self.hash).pack(pady=10)
        
        
        self.hash_label = ctk.CTkLabel(self.app, text="hash")
        self.hash_label.pack(pady=10)
    
    def generate(self):
        try:
            length = int(self.length_entry.get())
            if length < 8:
                messagebox.showerror("Error", "length need 8")
                return
            password = secrets.token_urlsafe(length) 
            self.password_label.configure(text=password)
            self.current_password = password
        except:
            messagebox.showerror("Error", "enter integer")
    
    def hash(self):
        if not hasattr(self, 'current_password'):
            messagebox.showwarning("Error", "you need criate password")
            return
        
        algorithm = self.alg_var.get()
        hash_obj = hashlib.new(algorithm)
        hash_obj.update(self.current_password.encode())
        self.hash_label.configure(text=hash_obj.hexdigest())
    
    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    app = PasswordApp()
    app.run()