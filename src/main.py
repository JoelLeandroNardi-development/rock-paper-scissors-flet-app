import flet as ft
import random
import game_engine
import game_data

def main(page: ft.Page):
    page.title = "Rock Paper Scissors"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    total_rounds = 3
    current_round = 1
    player_wins = 0
    computer_wins = 0
    game_active = False

    output = ft.TextField(multiline=True, read_only=True, expand=True, height=300, label="Game log")
    round_label = ft.Text(value="Round: 1 / ?", size=16)

    round_selector = ft.Dropdown(
        label="Select number of rounds",
        options=[ft.dropdown.Option(str(n)) for n in [1, 3, 5, 7]],
        value="3",
    )

    def reset_game(e=None):
        nonlocal current_round, player_wins, computer_wins, game_active, total_rounds
        total_rounds = int(round_selector.value)
        current_round = 1
        player_wins = 0
        computer_wins = 0
        game_active = True
        output.value = ""
        round_label.value = f"Round: {current_round} / {total_rounds}"
        page.update()

    def play(user_choice):
        nonlocal current_round, player_wins, computer_wins, game_active

        if not game_active:
            return

        computer_choice = random.randint(0, 2)
        result_lines = [
            f"You chose {game_data.options[user_choice]} {game_data.images[user_choice]}",
            f"Computer chose {game_data.options[computer_choice]} {game_data.images[computer_choice]}",
        ]

        result = game_engine.calculate_results(user_choice, computer_choice)
        result_lines.append(result)

        if game_data.win_message in result:
            player_wins += 1
        elif game_data.lose_message in result:
            computer_wins += 1

        output.value += "\n".join(result_lines) + "\n\n"
        current_round += 1

        if current_round > total_rounds or player_wins > total_rounds // 2 or computer_wins > total_rounds // 2:
            game_active = False
            if player_wins == computer_wins:
                output.value += "🏁 Match Over! It's a draw!\n\nClick 'Start Game' to play again.\n"
            elif player_wins > computer_wins:
                output.value += f"🏁 Match Over! {game_data.win_message}\n\nClick 'Start Game' to play again.\n"
            else:
                output.value += f"🏁 Match Over! {game_data.lose_message}\n\nClick 'Start Game' to play again.\n"
        else:
            round_label.value = f"Round: {current_round} / {total_rounds}"

        page.update()

    page.add(
        ft.Text("Rock, Paper, Scissors!", size=24, weight="bold", text_align="center"),
        ft.Row(
            [
                round_selector,
                ft.ElevatedButton("▶️ Start Game", on_click=reset_game),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        round_label,
        ft.Row([
            ft.ElevatedButton("🪨 Rock", on_click=lambda e: play(0)),
            ft.ElevatedButton("📄 Paper", on_click=lambda e: play(1)),
            ft.ElevatedButton("✂️ Scissors", on_click=lambda e: play(2)),
        ], alignment=ft.MainAxisAlignment.CENTER),
        output,
    )

ft.app(main)
