"""main.py
Summary:
    Script to play the Towers of Hanoi game.

Extended Summary:
    This script allows a user to play the Towers of Hanoi game. The game
    involves moving a set of disks from one stack to another, following
    specific rules.
"""

from .utils import *

STACKS = [Stack("Left"), Stack("Middle"), Stack("Right")]


def main():
    """
    Main function to execute the Towers of Hanoi game.

    Initializes the game, plays it, and then displays the results to the user.
    """
    num_discs = setup_game()
    num_opt_moves = 2**num_discs - 1
    print(
        f"\nThe fastest you can solve this game is in {num_opt_moves} moves.")
    num_user_moves = play_game(num_discs)
    print(
        f"\n\nYou completed the game in {num_user_moves} moves, and the optimal"
        f"number of moves is {num_opt_moves}."
    )


def get_input(prompt_message: str) -> Stack:
    """
    Prompt the user for input based on the given message.

    Args:
        prompt_message (str): Message to display to the user.

    Returns:
        Stack: The chosen stack based on user input.
    """
    choices = {stack.get_name()[0]: stack for stack in STACKS}
    options = " / ".join(
        [f"{key} for {value.get_name()}" for key, value in choices.items()]
    )
    while True:
        print(f"{prompt_message} ({options}):")
        user_input = input().upper()
        if user_input in choices:
            return choices[user_input]


def setup_game() -> int:
    """
    Set up the Towers of Hanoi game.

    Prompts the user for the number of disks and initializes the game stacks.

    Returns:
        int: Number of disks chosen by the user.
    """
    num_discs = int(input("\nHow many disks do you want to play with?\n"))
    while num_discs < 3:
        num_discs = int(input("Enter a number greater than or equal to 3\n"))
    for i in range(num_discs, 0, -1):
        STACKS[0].push(i)
    return num_discs


def play_game(num_disks: int) -> int:
    """
    Play the Towers of Hanoi game.

    Args:
        num_disks (int): Number of disks chosen by the user.

    Returns:
        int: Number of moves made by the user.
    """
    num_user_moves = 0
    while STACKS[2].get_size() != num_disks:
        print("\n\n\n...Current Stacks...")
        for stack in STACKS:
            stack.print_items()
        while True:
            from_stack = get_input("\nWhich stack do you want to move from?")
            to_stack = get_input("\nWhich stack do you want to move to?")
            if from_stack.is_empty():
                print("\n\nInvalid Move. Try Again.")
            elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
                disk = from_stack.pop()
                to_stack.push(disk)
                num_user_moves += 1
                break
            else:
                print("\n\nInvalid Move. Try Again.")
    return num_user_moves


if __name__ == "__main__":
    main()
