'''
What's on the menu?
 Report a typo
Description
In this stage, you need to put up the main menu for the game.
Think about the video games you like. They may be different, but they have one thing in common — the main menu. It may contain the game title and some options like "start a new game" or "load game". And of course, it should have the option to exit the game.
Objectives
In this stage, your program should:
1. Show a welcome message with the game title. The message should include the phrase Welcome to followed by the title. To make it stand out as a title, you need to surround it with three asterisks (***) on each end.
2. Show different options to start a new game or load a saved one. You may use options shown in the Examples below or use your own, but make sure to include its number and appropriate substring (Start a new game and Load your progress respectively).
3. Take the user input. If it is incorrect, show a message and wait for the correct one. (Unknown input! Please enter a valid one.)
4. Print temporary placeholder messages like in the example, when a player starts a new game (Starting a new game) or loads an existing one (No saved data found).
5. Implement the exit feature for your game. Print a goodbye message. (Goodbye)
Your program should be able to process inputs of different letter cases.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.
Example 1: Input "1".
***Welcome to the Journey to Mount Qaf***
1. Start a new game (START)
2. Load your progress (LOAD)
3. Quit the game (QUIT)
> 1
Starting a new game...
Example 2: Input "start'". Your program must be able to process letters of different cases.
***Welcome to the Journey to Mount Qaf***
1. Start a new game (START)
2. Load your progress (LOAD)
3. Quit the game (QUIT)
> StaRt
Starting a new game...
Example 3: Input "2".
***Welcome to the Journey to Mount Qaf***
1. Start a new game (START)
2. Load your progress (LOAD)
3. Quit the game (QUIT)
> 2
No save data found!
Example 4: Unknown input.
***Welcome to the Journey to Mount Qaf***
1. Start a new game (START)
2. Load your progress (LOAD)
3. Quit the game (QUIT)
> 5
Unknown input! Please enter a valid one.
> smile
Unknown input! Please enter a valid one.
>
Example 5: Exit the program.
***Welcome to the Journey to Mount Qaf***
1. Start a new game (START)
2. Load your progress (LOAD)
3. Quit the game (QUIT)
> 3
Goodbye!

Write a program

Z <https://hyperskill.org/projects/161/stages/834/implement> 
'''
# write your code here
from enum import Enum

class MENU_ELEMENTS(Enum):
    MENU = {'MAIN MENU' : {1:['Start a new game (START)', 'start'], 2: ['Load your progress (LOAD)', 'load'], 3: ['Quit the game (QUIT)', 'quit']}}


class Main_Logic():
    def __init__(self):
        self.program_status = 'MAIN MENU'
        self.main_loop()

    def print_actual_menu(self, menu_type):
        # print(menu_type)
        for key, menu_text in MENU_ELEMENTS.MENU.value[menu_type].items():
            print(f'{key}. {menu_text[0]}')

    def parse_command_input(self, input_string):
        for i in range(1, len(MENU_ELEMENTS.MENU.value[self.program_status]) + 1):
            if input_string == str(i) or input_string.lower() == MENU_ELEMENTS.MENU.value[self.program_status][i][1]:
                return str(i)
        return None

    def main_loop(self):
        print('***Welcome to the Trap Door***')
        while True:
            self.print_actual_menu(self.program_status)
            # print('\nEnter an option:')
            # ni = 'Not implemented!'
            unk_inp = 'Unknown input! Please enter a valid one.'
            command = self.parse_command_input(input())
            match self.program_status, command:
                case 'MAIN MENU', '1':
                    print('Starting a new game...')
                    # self.program_status = 'CRUD MENU'
                    continue
                case 'MAIN MENU', '2':
                    print('No saved data found')
                    # self.program_status = 'TOP TEN MENU'
                    continue
                case 'MAIN MENU', '3':
                    print('Goodbye!')
                    break
                case 'MAIN MENU', _:
                    print(unk_inp)
                    continue

if __name__ == '__main__':
    main_logic = Main_Logic()

