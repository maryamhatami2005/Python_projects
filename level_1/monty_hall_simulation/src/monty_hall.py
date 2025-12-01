import random

def monty_hall_game(switch_doors: bool) -> bool:
    """ Simulate a single Monty Hall game.

    :param switch_doors: If True, the contestant will switch their choice after a goat door is revealed.
    :type switch_doors: bool
    :return: True if the contestent won the car, False otherwise.
    :rtype: bool
    """
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


def simulate_game(num_games: int = 1000) -> tuple[float, float]:
    """ Simulate a number of Monty Hall games and print the statistics

    :param num_games: The number of games to simulate. Defaults to 1000.
    :return:  The percentages of winning the game when not switching and when switching doors.
    """
    num_wins_without_switching = sum(monty_hall_game(False) for _ in range(num_games))
    num_wins_with_switching = sum(monty_hall_game(True) for _ in range(num_games))
    return (num_wins_without_switching ) , (num_wins_with_switching ) 

if __name__ == "__main__":
    num_games = 100
    without_switching, with_switching = simulate_game(num_games)
    print(f"Win percent without switching: {without_switching}")
    print(f"Win percent with switching: {with_switching}")