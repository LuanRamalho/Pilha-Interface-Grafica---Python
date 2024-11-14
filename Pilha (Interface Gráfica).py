import tkinter as tk
from tkinter import messagebox

class StackApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pilha (Stack)")
        self.master.geometry("400x400")
        self.master.config(bg="#f0f8ff")  # Cor de fundo suave

        self.stack = []

        # Estilo de fontes
        label_font = ("Helvetica", 12, "bold")
        button_font = ("Arial", 10, "bold")

        # Elemento de instrução
        self.label = tk.Label(master, text="Insira um elemento:", bg="#f0f8ff", font=label_font)
        self.label.pack(pady=10)

        # Caixa de entrada
        self.entry = tk.Entry(master, font=("Arial", 12), bg="#e0f7fa", bd=2, relief="solid")
        self.entry.pack(pady=5)

        # Botões
        self.push_button = tk.Button(master, text="Inserir", command=self.push, font=button_font, bg="#4CAF50", fg="white", relief="raised", width=15)
        self.push_button.pack(pady=5)

        self.pop_button = tk.Button(master, text="Remover", command=self.pop, font=button_font, bg="#f44336", fg="white", relief="raised", width=15)
        self.pop_button.pack(pady=5)

        # Exibição dos elementos da pilha
        self.display_label = tk.Label(master, text="Elementos da Pilha:", bg="#f0f8ff", font=label_font)
        self.display_label.pack(pady=10)

        self.stack_display = tk.Text(master, height=10, width=30, font=("Courier New", 12), bg="#ffffff", fg="#333333", bd=2, relief="sunken")
        self.stack_display.pack(pady=5)

    def push(self):
        element = self.entry.get()
        if element:
            self.stack.append(element)
            self.update_stack_display()
            messagebox.showinfo("Sucesso", f"Elemento '{element}' inserido na pilha.")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Por favor, insira um elemento.")

    def pop(self):
        if self.stack:
            element = self.stack.pop()
            self.update_stack_display()
            messagebox.showinfo("Sucesso", f"Elemento '{element}' removido da pilha.")
        else:
            messagebox.showwarning("Atenção", "A pilha está vazia.")

    def update_stack_display(self):
        self.stack_display.delete(1.0, tk.END)  # Limpa o texto anterior
        for element in reversed(self.stack):  # Mostra os elementos em ordem
            self.stack_display.insert(tk.END, f"{element}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = StackApp(root)
    root.mainloop()
