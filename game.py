import random
from chest import Chest
from rich import print


class Game:
    """
    A simple game where the player can take steps to find either nothing 
    or a chest with some gold.

    Attributes:
        finders (dict): Probability weights for finding 'nothing' or a 'chest'.
        nothing (int): Counter for how many times nothing was found.
        chests (int): Counter for chests found.
        gold (int): Total gold collected.
    """
    finders = {
        'nothing': 40,
        'chest': 60
    }

    def __init__(self):
        """Initialize game statistics counters."""

        self.nothing = 0
        self.chests = 0
        self.gold = 0

    def found_something(self):
        """
        Randomly determine what the player finds on a step.

        Returns:
            str: Either 'nothing' or 'chest'.
        """
        item = list(self.finders.keys())
        weights = list(self.finders.values())
        found_object = random.choices(item, weights)[0]
        return found_object

    def chest_found(self):
        """
        Handle the event of finding a chest:
        - Create a Chest instance,
        - Calculate its gold value,
        - Update stats and print a message with chest color and gold received.
        """
        chest = Chest()
        value = chest.find_approx_value()
        self.chests += 1
        self.gold += value
        color = chest.color.upper()
        if color == 'GREEN':
            print(
                f'You found [green]{color}[/green] chest!'
                f'Received {value} gold.\n')
        elif color == 'ORANGE':
            print(
                f'You found [orange1]{color}[/orange1] chest!'
                f'Received {value} gold.\n')
        elif color == 'PURPLE':
            print(
                f'You found [purple]{color}[/purple] chest!'
                f'Received {value} gold.\n')
        else:
            print(
                f'You found [gold1]{color}[/gold1] chest!'
                f'Received {value} gold.\n')

    def nothing_found(self):
        """
        Handle the event of finding nothing:
        - Update stats and print an encouraging message.
        """
        self.nothing += 1
        print('Nothing found, keep trying!\n')

    def run(self):
        """
        Run the main game loop:
        - Ask the player if they want to take a step,
        - Handle outcomes (chest or nothing),
        - On exit, show statistics and optionally save them to a file.
        """
        print(
            'Welcome to my mini game! '
            'Each step you will have a chance to find something.\n'
            "Let's try!")
        step_counter = 0
        while True:
            step = input('Would you like to take a step? y/n\n').lower()
            while step not in ('y', 'n'):
                step = input("Please enter 'y' or 'n': \n").lower()
            if step == 'y':
                step_counter += 1
                if self.found_something() == 'chest':
                    self.chest_found()
                else:
                    self.nothing_found()
            elif step == 'n':
                print('Game statistics: \n'
                      f'You took {step_counter} steps. \n'
                      f'You have found {self.chests} chests and collected {self.gold} gold.\n'
                      f'You have found nothing {self.nothing} times.\n')
                save_file = input(
                    'Would you like to save statistics as a text file? y/n \n'
                ).lower()
                while save_file not in ('y', 'n'):
                    save_file = input("Please enter 'y' or 'n': \n").lower()
                if save_file == 'y':
                    try:
                        with open('statistics.txt', 'w', encoding='UTF-8') as file:
                            file.write(f'Number of steps taken: {step_counter}\n'
                                       f'Number of found chests: {self.chests}\n'
                                       f'Number of collected gold: {self.gold}\n'
                                       f'Number of nothing found: {self.nothing}\n'
                                       )
                        print('File was saved. '
                              'Thank you for playing. See you next time!')
                        break
                    except Exception as e:
                        print(f"Couldn't save file. Error: {e}")
                elif save_file == 'n':
                    print('Thank you for playing. See you next time!')
                    break
