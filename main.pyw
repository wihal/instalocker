import customtkinter as ti
from brain import *
import os
from time import sleep
import concurrent.futures
import threading


agentsjson = resource_path(".vlocker\\agents.json")
settingsjson = resource_path(".vlocker\\settings.json")
icon = resource_path(".vlocker\\icon.ico")
agents = agents_list(agentsjson) # Get the names of the agents  

def root():
    print("building...")
    ti.set_appearance_mode("dark")
    ti.set_default_color_theme("dark-blue")
    
    root = ti.CTk()
    root.geometry("450x330")
    root.title("Valorant Instalocker")
    root.iconbitmap(icon)


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

    button = ti.CTkButton(frame, text="add agents/", command=lambda: add_frame())
    button.grid(row=6, column=1, padx=25, pady=20)

    button = ti.CTkButton(frame2, text="Start", command=lambda: start(entry1.get(), entry2.get(), drop.get()))
    button.grid(row=2, column=1, padx=25, pady=7)

    label = ti.CTkLabel(frame2, text="made by Willi")
    label.grid(row=3, column=1, padx=25, pady=10)

    button3 = ti.CTkButton(frame2, fg_color="red", text="reset everything", command=lambda: remove_agent(agentsjson))
    button3.grid(row=4, column=1, padx=25, pady=20)

    root.mainloop()

def add_frame():
    print("building...")
    ti.set_appearance_mode("dark")
    ti.set_default_color_theme("dark-blue")

    root = ti.CTk()
    root.geometry("225x180")
    root.title("Add Agents")
    root.iconbitmap(icon)

    frame = ti.CTkFrame(root)
    frame.grid(row=1, column=1, padx=20, pady=20)

    entry = ti.CTkEntry(frame, placeholder_text="Enter Agentname")
    entry.grid(row=1, column=1, padx=25, pady=10)
    
    button = ti.CTkButton(frame, text="add/update agent", command=lambda: add_explanation(entry.get(), agentsjson))
    button.grid(row=2, column=1, padx=25, pady=7)

    button1 = ti.CTkButton(frame, fg_color="green", text="add button", command=lambda: add_explanation("Button", settingsjson))
    button1.grid(row=3, column=1, padx=25, pady=7)
    
    root.mainloop()
def add_explanation(agent, json_file_path):
    print("building...")
    ti.set_appearance_mode("dark")
    ti.set_default_color_theme("dark-blue")

    root = ti.CTk()
    root.geometry("280x150")
    root.title("Add")
    root.iconbitmap(icon)

    frame = ti.CTkFrame(root)
    frame.grid(row=1, column=1, padx=20, pady=20)

    label = ti.CTkLabel(frame, text=f"hover over {agent} and then \n press q. Restart the Software after")
    label.grid(row=1, column=1, padx=25, pady=7)

    button = ti.CTkButton(frame, text="ok", command=lambda: root.destroy())
    button.grid(row=2, column=1, padx=25, pady=20)
    

    threading.Thread(target=add_value, args=(agent, json_file_path)).start()

    root.mainloop()
    
    

if __name__ == "__main__":
    root()
    