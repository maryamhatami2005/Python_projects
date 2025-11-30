import random

def monty_hall_game(switch_doors):
    doors = ['car'] + ['goat'] * 2
    random.shuffle(doors)

    initial_choice = random.choice(range(3))

    doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] == 'goat']
    door_revealed = random.choice(doors_revealed)

    if switch_doors:
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] =='car'


def simulate_game(num_games):
    num_wins_without_switching = sum(monty_hall_game(False) for _ in range(num_games))
    num_wins_with_switching = sum(monty_hall_game(True) for _ in range(num_games))
    return (num_wins_without_switching / num_games) * 100, (num_wins_with_switching / num_games) * 100

if __name__ == "__main__":
    num_games = 100
    without_switching, with_switching = simulate_game(num_games)
    print(f"Win percent without switching: {without_switching}")
    print(f"Win percent with switching: {with_switching}")