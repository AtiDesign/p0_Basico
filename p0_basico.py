import tkinter as tk
from tkinter import scrolledtext
import re


def extrair():
    texto = entrada.get("1.0", tk.END)

    emails = re.findall(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        texto
    )

    telefones = re.findall(
        r'(?:\+55\s?)?(?:\(\d{2}\)\s?|\d{2}\s?)?\d{4,5}-?\d{4}',
        texto
    )

    urls = re.findall(
        r'https?://[^\s]+|www\.[^\s]+',
        texto
    )

    resultado.delete("1.0", tk.END)

    resultado.insert(tk.END, "E-MAILS\n")
    resultado.insert(tk.END, "-" * 30 + "\n")

    if emails:
        for email in emails:
            resultado.insert(tk.END, email + "\n")
    else:
        resultado.insert(tk.END, "Nenhum encontrado\n")

    resultado.insert(tk.END, "\nTELEFONES\n")
    resultado.insert(tk.END, "-" * 30 + "\n")

    if telefones:
        for telefone in telefones:
            resultado.insert(tk.END, telefone + "\n")
    else:
        resultado.insert(tk.END, "Nenhum encontrado\n")

    resultado.insert(tk.END, "\nURLS\n")
    resultado.insert(tk.END, "-" * 30 + "\n")

    if urls:
        for url in urls:
            resultado.insert(tk.END, url + "\n")
    else:
        resultado.insert(tk.END, "Nenhuma encontrada\n")


janela = tk.Tk()
janela.title("Extrator de Informações")
janela.geometry("700x500")

titulo = tk.Label(
    janela,
    text="Extrator de Informações de Contato",
    font=("Arial", 14, "bold")
)
titulo.pack(pady=10)

entrada = scrolledtext.ScrolledText(janela, height=10)
entrada.pack(fill="both", padx=10, pady=5)

botao = tk.Button(
    janela,
    text="Extrair Informações",
    command=extrair
)
botao.pack(pady=10)

resultado = scrolledtext.ScrolledText(janela, height=12)
resultado.pack(fill="both", padx=10, pady=5)

janela.mainloop()