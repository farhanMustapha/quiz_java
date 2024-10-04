import flet as ft
import json
from menu import menubar

# Charger le fichier JSON contenant les questions et réponses
def load_quiz_data():
    with open('quiz_data.json', 'r', encoding='utf-8') as file:
        return json.load(file)

counter = 0

def main(page: ft.Page):
    quiz_data = load_quiz_data()
    questions = quiz_data["questions"]
    
    global counter
    page.title = "Quiz Comptable"
    page.window.width = 400
    page.window.left = 860
    page.scroll = 'auto'
    
    def rep_correct(e):
        correction.value = "Correct!"
        reponse_container.bgcolor = ft.colors.GREEN
        page.update()
    
    def rep_fausse(e):
        correction.value = "Fausse!"
        reponse_container.bgcolor = ft.colors.RED
        page.update()

    def next_question(e):
        global counter
        if counter < len(questions) - 1:
            counter += 1
            load_question()
        if counter == len(questions) - 1:
            next_btn.visible = False  # Masquer le bouton "Next" à la dernière question
        back_btn.visible = True  # Afficher le bouton "Back" après la première question
        page.update()

    def previous_question(e):
        global counter
        if counter > 0:
            counter -= 1
            load_question()
        if counter == 0:
            back_btn.visible = False  # Masquer le bouton "Back" à la première question
        next_btn.visible = True  # Réafficher le bouton "Next"
        page.update()

    def load_question():
        reponse_container.bgcolor = ft.colors.WHITE
        if 0 <= counter < len(questions):
            question_data = questions[counter]
            question.value = f"{counter+1} ) {question_data['question']}"
            options = question_data["options"]
            
            # Mettre à jour les réponses
            for idx, rep in enumerate([rep1, rep2, rep3, rep4]):
                if idx < len(options):
                    rep.text = options[idx]["text"]
                    rep.visible = True
                    if options[idx]["is_correct"]:
                        rep.on_click = rep_correct
                    else:
                        rep.on_click = rep_fausse
                else:
                    rep.visible = False

            correction.value = ""
            page.update()
        else:
            question.value = "Quiz terminé!"
            rep1.visible = rep2.visible = rep3.visible = rep4.visible = False
            next_btn.visible = False
            back_btn.visible = False
            page.update()

    question = ft.Text(size=20)
    correction = ft.Text(value="", size=15, color=ft.colors.WHITE)
    
    # Boutons de réponse
    rep1 = ft.ElevatedButton(text="Option 1", visible=False, width=300)
    rep2 = ft.ElevatedButton(text="Option 2", visible=False, width=300)
    rep3 = ft.ElevatedButton(text="Option 3", visible=False, width=300)
    rep4 = ft.ElevatedButton(text="Option 4", visible=False, width=300)
    
    reponse_container = ft.Container(
        content=ft.Column([question, rep1, rep2, rep3, rep4, correction], spacing=10),
        padding=10,
        bgcolor=ft.colors.BLUE_GREY_900,
        height=450
    )
    
    # Bouton pour passer à la prochaine question
    next_btn = ft.ElevatedButton(text="Next", on_click=next_question)

    # Bouton pour revenir à la question précédente
    back_btn = ft.ElevatedButton(text="Back", on_click=previous_question, visible=False)

    page.add(menubar,reponse_container, ft.Row([back_btn, next_btn]))
    load_question()  # Démarrer avec la première question

ft.app(target=main)
