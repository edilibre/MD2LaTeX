import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from ttkthemes import ThemedTk
import subprocess
import os
import re  # Module pour les expressions régulières

def convert_markdown_to_latex(markdown_file, latex_file, document_class, add_toc, author, bibliography):
    try:
        # Options de Pandoc
        pandoc_options = ["pandoc", markdown_file, "-o", latex_file, "--to", "latex", "--standalone"]
        if add_toc:
            pandoc_options.append("--toc")  # Ajouter une table des matières

        # Convertir Markdown en LaTeX avec Pandoc
        subprocess.run(pandoc_options, check=True)

        # Lire le fichier LaTeX généré
        with open(latex_file, "r") as file:
            content = file.read()

        # Supprimer le préambule (entre documentclass et begin{document})
        content = re.sub(
            r"documentclass\[.*?\]\s*\{.*?\}\n(.*?)begin{document}", 
            f"documentclass{{{document_class}}}\n\\\\addbibresource{{{bibliography}}}\nbegin{{document}}\n\\\\TFEAuthor{{{author}}}", 
            content, 
            flags=re.DOTALL
        )

        # Réécrire le fichier LaTeX modifié
        with open(latex_file, "w") as file:
            file.write(content)

        messagebox.showinfo("Succès", f"Conversion réussie : {latex_file}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
    if file_path:
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".tex", filetypes=[("LaTeX Files", "*.tex")])
    if file_path:
        output_file_entry.delete(0, tk.END)
        output_file_entry.insert(0, file_path)

def select_bibliography_file():
    file_path = filedialog.askopenfilename(filetypes=[("BibTeX Files", "*.bib")])
    if file_path:
        bibliography_entry.delete(0, tk.END)
        bibliography_entry.insert(0, file_path)

def start_conversion():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    document_class = document_class_entry.get()
    add_toc = add_toc_var.get()
    author = author_entry.get()
    bibliography = bibliography_entry.get()

    if input_file and output_file and bibliography:
        convert_markdown_to_latex(input_file, output_file, document_class, add_toc, author, bibliography)
    else:
        messagebox.showwarning("Attention", "Veuillez sélectionner un fichier d'entrée, de sortie et de bibliographie.")

# Créer l'interface graphique avec un thème moderne
root = ThemedTk(theme="arc")  # Choisir un thème moderne (ex: "arc", "equilux", "breeze")
root.title("Convertisseur Markdown vers LaTeX")

# Ajouter une icône à la fenêtre
if os.path.exists("icon.ico"):
    root.iconbitmap("icon.ico")

# Style pour les boutons et les champs
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#ccc")
style.configure("TEntry", padding=6, relief="flat")

# Champ pour le fichier d'entrée
ttk.Label(root, text="Fichier Markdown :").grid(row=0, column=0, padx=5, pady=5)
input_file_entry = ttk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=5, pady=5)
ttk.Button(root, text="Parcourir", command=select_input_file).grid(row=0, column=2, padx=5, pady=5)

# Champ pour le fichier de sortie
ttk.Label(root, text="Fichier LaTeX :").grid(row=1, column=0, padx=5, pady=5)
output_file_entry = ttk.Entry(root, width=50)
output_file_entry.grid(row=1, column=1, padx=5, pady=5)
ttk.Button(root, text="Parcourir", command=select_output_file).grid(row=1, column=2, padx=5, pady=5)

# Champ pour la classe de document
ttk.Label(root, text="Classe de document :").grid(row=2, column=0, padx=5, pady=5)
document_class_entry = ttk.Entry(root, width=50)
document_class_entry.insert(0, "IFSI")  # Valeur par défaut
document_class_entry.grid(row=2, column=1, padx=5, pady=5)

# Champ pour le nom de l'auteur
ttk.Label(root, text="Nom de l'auteur :").grid(row=3, column=0, padx=5, pady=5)
author_entry = ttk.Entry(root, width=50)
author_entry.grid(row=3, column=1, padx=5, pady=5)

# Champ pour le fichier de bibliographie
ttk.Label(root, text="Fichier de bibliographie :").grid(row=4, column=0, padx=5, pady=5)
bibliography_entry = ttk.Entry(root, width=50)
bibliography_entry.grid(row=4, column=1, padx=5, pady=5)
ttk.Button(root, text="Parcourir", command=select_bibliography_file).grid(row=4, column=2, padx=5, pady=5)

# Case à cocher pour la table des matières
add_toc_var = tk.BooleanVar()
add_toc_checkbutton = ttk.Checkbutton(root, text="Ajouter une table des matières", variable=add_toc_var)
add_toc_checkbutton.grid(row=5, column=1, padx=5, pady=5)

# Bouton de conversion
ttk.Button(root, text="Convertir", command=start_conversion).grid(row=6, column=1, pady=10)

# Lancer l'interface
root.mainloop()