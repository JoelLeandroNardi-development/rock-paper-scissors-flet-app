import flet as ft
import random
import game_engine
import game_data

def main(page: ft.Page):
    page.title = "Rock Paper Scissors"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    output = ft.TextField(
        multiline=True,
        read_only=True,
        expand=True,
        height=300,
        label="Game log",
    )

    def play(user_choice):
        computer_choice = random.randint(0, 2)

        result_lines = [
            f"You chose {game_data.options[user_choice]} {game_data.images[user_choice]}",
            f"Computer chose {game_data.options[computer_choice]} {game_data.images[computer_choice]}",
            game_engine.calculate_results(user_choice, computer_choice)
        ]

        output.value += "\n".join(result_lines) + "\n\n"
        page.update()

    page.add(
        ft.Text("Choose your move:", size=20, weight="bold"),
        ft.Row([
            ft.ElevatedButton("🪨 Rock", on_click=lambda e: play(0)),
            ft.ElevatedButton("📄 Paper", on_click=lambda e: play(1)),
            ft.ElevatedButton("✂️ Scissors", on_click=lambda e: play(2)),
        ], alignment=ft.MainAxisAlignment.CENTER),
        output,
    )

ft.app(target=main)
