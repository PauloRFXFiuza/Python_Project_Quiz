'''Quiz Project By Paulo Fiuza - 12/29/2024
Projeto Quiz'''

import tkinter as tk
import random

# Main function / Função principal
def main():
    # Create the main window / Cria a janela principal
    root = tk.Tk()
    root.title("Quiz App")  # Window title / Título da janela
    root.attributes('-fullscreen', True)  # Fullscreen mode / Modo tela cheia
    root.configure(bg="black")  # Set background color to black / Define o fundo como preto

    # Questions, options, and answers / Perguntas, opções e respostas
    questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome", "Madrid", "Athens", "Lisbon"], "answer": "Paris"},
        {"question": "What is the largest planet in the Solar System?", "options": ["Earth", "Mars", "Jupiter", "Venus", "Saturn", "Neptune", "Uranus"], "answer": "Jupiter"},
        {"question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Dickens", "Hemingway", "Tolkien", "Rowling", "Austen", "Orwell"], "answer": "Shakespeare"},
        {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "N2", "He", "C", "Na"], "answer": "H2O"},
        {"question": "How many continents are there on Earth?", "options": ["6", "7", "5", "4", "8", "3", "9"], "answer": "7"},
        {"question": "Which country is known as the Land of the Rising Sun?", "options": ["Japan", "China", "Thailand", "India", "South Korea", "Vietnam", "Malaysia"], "answer": "Japan"},
        {"question": "What is the smallest prime number?", "options": ["2", "1", "3", "5", "7", "11", "13"], "answer": "2"},
        {"question": "Which ocean is the largest?", "options": ["Pacific", "Atlantic", "Indian", "Arctic", "Southern", "Mediterranean", "Black Sea"], "answer": "Pacific"},
        {"question": "Who painted the Mona Lisa?", "options": ["Da Vinci", "Van Gogh", "Picasso", "Monet", "Michelangelo", "Rembrandt", "Raphael"], "answer": "Da Vinci"},
        {"question": "What is the speed of light?", "options": ["299,792 km/s", "300,000 km/s", "150,000 km/s", "200,000 km/s", "100,000 km/s", "250,000 km/s", "350,000 km/s"], "answer": "299,792 km/s"}
    ]

    # Shuffle questions / Embaralha as perguntas
    random.shuffle(questions)

    # Score and question index / Pontuação e índice da pergunta
    score = [0]  # Using a list to allow modification within nested functions / Usando lista para modificar dentro de funções aninhadas
    current_question_index = [0]

    # Global result label / Rótulo global para exibir resultado
    global result_label
    result_label = None

    # Function to display the next question / Função para exibir a próxima pergunta
    def display_question():
        global result_label

        # Clear the screen / Limpa a tela
        for widget in root.winfo_children():
            widget.destroy()

        # Get the current question / Obtém a pergunta atual
        question_data = questions[current_question_index[0]]

        # Shuffle options / Embaralha as opções
        random.shuffle(question_data["options"])

        # Display the question / Exibe a pergunta
        question_label = tk.Label(
            root,
            text=question_data["question"],
            font=("Arial", 30, "bold"),
            fg="white",
            bg="black",
            wraplength=1000
        )
        question_label.pack(pady=50)

        # Variable to store the selected option / Variável para armazenar a opção selecionada
        selected_option = tk.StringVar(value="")

        # Display the options / Exibe as opções
        for option in question_data["options"]:
            rb = tk.Radiobutton(
                root,
                text=option,
                variable=selected_option,
                value=option,
                font=("Arial", 30),
                fg="white",
                bg="black",
                selectcolor="gray",
                wraplength=800,
                indicatoron=0,  # Remove the default radio button indicator / Remove o indicador padrão
                height=1,  # Increase the height of the button / Aumenta a altura do botão
                width=20  # Increase the width of the button / Aumenta a largura do botão
            )
            rb.pack(anchor="w", padx=50)

        # Function to submit the answer / Função para enviar a resposta
        def submit_answer():
            answer = selected_option.get()
            if answer == question_data["answer"]:
                result_label.config(text="Correct answer!", fg="green")  # Resposta correta
                score[0] += 1
            else:
                result_label.config(text="Wrong answer!", fg="red")  # Resposta errada

            # Proceed to the next question / Avança para a próxima pergunta
            current_question_index[0] += 1
            if current_question_index[0] < len(questions):
                root.after(2000, display_question)  # Delay before showing the next question / Atraso antes de exibir a próxima pergunta
            else:
                root.after(2000, display_score)  # Show the final score / Exibe a pontuação final

        # Button to submit the answer / Botão para enviar a resposta
        submit_button = tk.Button(
            root,
            text="Submit Answer",
            command=submit_answer,
            font=("Arial", 30),
            bg="white",
            fg="black"
        )
        submit_button.pack(pady=50)

        # Label to display the result / Rótulo para exibir o resultado
        result_label = tk.Label(
            root,
            text="",
            font=("Arial", 30),
            fg="white",
            bg="black"
        )
        result_label.pack()

    # Function to display the final score / Função para exibir a pontuação final
    def display_score():
        # Clear the screen / Limpa a tela
        for widget in root.winfo_children():
            widget.destroy()

        # Display the final score / Exibe a pontuação final
        score_label = tk.Label(
            root,
            text=f"Your final score is: {score[0]} / {len(questions)}",
            font=("Arial", 30, "bold"),
            fg="white",
            bg="black"
        )
        score_label.pack(pady=50)

        # Exit button / Botão para sair
        exit_button = tk.Button(
            root,
            text="Exit",
            command=root.destroy,
            font=("Arial", 30),
            bg="white",
            fg="black"
        )
        exit_button.pack(pady=50)

    # Start with the first question / Inicia com a primeira pergunta
    display_question()

    # Main loop / Loop principal
    root.mainloop()

# Execute the main function / Executa a função principal
if __name__ == "__main__":
    main()