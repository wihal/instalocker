import customtkinter as ti
import threading
from PIL import Image
from agent_manager import *
from brain import *

agents_json = resource_path(".vlocker\\agents.json")
settings_json = resource_path(".vlocker\\settings.json")
icon = resource_path(".vlocker\\icon.ico")
agents = agents_list(agents_json) # Get the names of the agents 
background_image = resource_path(".vlocker\\background.jpg") # Hippity hoppity your picture is now my property
color_theme = resource_path(".vlocker\\themes\\red_theme.json")

def root():
    print("root")
    print(color_theme)
    
    ti.set_appearance_mode("dark")
    ti.set_default_color_theme(color_theme)
    
    root = ti.CTk()
    root.geometry("450x330")
    root.title("Valorant Instalocker")
    root.iconbitmap(icon)
    root.resizable(False, False)

    background = ti.CTkImage(Image.open(background_image), size=(450, 330))
    background_label = ti.CTkLabel(root, text=None, image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = ti.CTkFrame(root)
    frame.grid(row=1, column=1, padx=20, pady=20)

    frame2 = ti.CTkFrame(root)
    frame2.grid(row=1, column=2, padx=20, pady=20)

    entry1 = ti.CTkEntry(frame, placeholder_text="start key")
    entry1.grid(row=2, column=1, padx=20, pady=12)

    entry2 = ti.CTkEntry(frame, placeholder_text="end key")
    entry2.grid(row=4, column=1, padx=20, pady=12)

    drop = ti.CTkOptionMenu(frame , values=agents)
    drop.grid(row=5, column=1, padx=20, pady=12)

    button = ti.CTkButton(frame, text="manage agents", command=lambda: agent_manager())
    button.grid(row=6, column=1, padx=25, pady=20)

    button = ti.CTkButton(frame2, text="Start", command=lambda: start(entry1.get(), entry2.get(), drop.get()))
    button.grid(row=2, column=1, padx=25, pady=7)

    label = ti.CTkLabel(frame2, text="made by Willi")
    label.grid(row=3, column=1, padx=25, pady=10)

    button3 = ti.CTkButton(frame2, fg_color="red", text="reset everything", command=lambda: reset_json(agents_json))
    button3.grid(row=4, column=1, padx=25, pady=20)

    root.mainloop()
    
if __name__ == "__main__":
    root()
    