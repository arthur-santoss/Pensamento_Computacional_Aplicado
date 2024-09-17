import tkinter as tk

def verificaTexto():
    texto = entrada.get()  
    if texto.startswith('Olá'):
        label_resultado.config(text="Olá pessoal")
    else:
        label_resultado.config(text=texto)

root = tk.Tk()
root.title("Atividade Prática 6 - Trabalhando com string")
root.geometry("400x300")

label = tk.Label(root, text="Informe a frase")
label.pack(pady=20)

entrada = tk.Entry(root, width=50)
entrada.pack(pady=5)

label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=20)

botao = tk.Button(root, text="Verificar texto", command=verificaTexto)
botao.pack(pady=5)

root.mainloop()
