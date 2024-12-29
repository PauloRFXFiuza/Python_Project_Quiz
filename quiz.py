'''Quiz Project By Paulo Fiuza - 12/29/2024
Projeto Quiz'''

import tkinter as tk

# Função principal
def main():
    # Criar a janela principal
    root = tk.Tk()
    root.title("Quiz App")  # Título da janela
    root.geometry("400x200")  # Define o tamanho da janela (opcional)

    # Adicionar o texto "Welcome to Quiz"
    welcome_label = tk.Label(root, text="Welcome to Quiz", font=("Arial", 24, "bold"))
    welcome_label.pack(pady=50)  # Centraliza o texto e adiciona espaçamento vertical

    # Iniciar o loop principal da interface gráfica
    root.mainloop()

# Executar a função principal
if __name__ == "__main__":
    main()