'''
Start a new game
 Report a typo
Description
In this stage, you will implement the new game function and the game stats.
You need to store important variables when creating a new game such as:
• The username. You will need it in a later stage for the save file path.
• The character attributes: Name, Species, and the Gender.
• The inventory: Snack, Weapon, and Tool.
• The difficulty level: 1. Easy, 2. Medium and 3. Hard. The user should be able to select the difficulty level either by the word or the index. Difficulty selection should be case-insensitive.
• The remaining lives: 5 for an easy difficulty level, 3 for a medium one, and 1 for a hard one. You don't need to take the number of lives as input, it should be calculated on the basis of the level that the user chooses.
You might want to divide variables into sections to make the output more pleasing to the player, that won't be tested.
Output highlighted substrings from a list before corresponding input, so that player can determine what data he/she is entering. You should get the game variables in the same order as in the Examples section.
When all the variables have been entered your program should output the game stats. You can use the following formatting:
Good luck on your journey, {username}!
Your character: {name}, {species}, {gender}
Your inventory: {snack}, {weapon}, {tool}
Difficulty: {difficulty}
Number of lives: {lives}
Note, that difficulty level should be printed as a word (Easy, Medium or Hard)
Also, a player can make a mistake by choosing to create a new game, so give them an option to go back to the main menu: Enter a username ('/b' to go back):.
Don't forget to handle incorrect input of difficulty the same way as before with option selection!
Objectives
In this stage, your program should:
1. Create and store the game state with variables such as the inventory, character attributes, difficulty, remaining lives, and the username.
2. Have the option to go back to the menu with /b command before creating a new game.
3. Before the new game starts, output the message Good luck on your journey, {username}! with the game stats below such as the character traits, inventory, difficulty, and the number of lives.
4. Handle incorrect input of difficulty.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.
Example 1: creating a new game.
***Welcome to the Journey to Mount Qaf***
1. Start a new game (START)
2. Load your progress (LOAD)
3. Quit the game (QUIT)
> 1
Starting a new game...
Enter a username ('/b' to go back): > new_user
Create your character:
	Name: > john
	Species: > human
	Gender: > male
Pack your bag for the journey:
	Snack: > apple
	Weapon: > sword
	Tool: > rope
Choose your difficulty:
	1. Easy
	2. Medium
	3. Hard
> 1
Good luck on your journey, new_user!
Your character: john, human, male
Your inventory: apple, sword, rope
Difficulty: easy
Number of lives: 5
Example 2: unknown input.
...
Choose your difficulty:
	1. Easy
	2. Medium
	3. Hard
> insane
Unknown input! Please enter a valid one.
> easy
...
Example 3: going back to the menu.
***Welcome to the Journey to Mount Qaf***
1. Start a new game (START)
2. Load your progress (LOAD)
3. Quit the game (QUIT)
> 1
Starting a new game...
Enter a username ('/b' to go back): > /b
***Welcome to the Journey to Mount Qaf***
1. Start a new game (START)
2. Load your progress (LOAD)
3. Quit the game (QUIT)
...

Write a program

Z <https://hyperskill.org/projects/161/stages/835/implement> 
'''





# write your code here
from enum import Enum

class MENU_ELEMENTS(Enum):
    MENU = {'MAIN MENU' : {1:['Start a new game (START)', 'start'], 2: ['Load your progress (LOAD)', 'load'], 3: ['Quit the game (QUIT)', 'quit']},
            'level_menu' : {1:['Easy', 'easy'], 2: ['Medium', 'medium'], 3: ['Hard', 'hard']}}

class TBAGame:
    def __init__(self, user_name):
        self.user_name = user_name
        self.game_user = User(user_name)

class User():
    def __init__(self, user_name):
        self.user_name = user_name
        print('Create your character:')
        self.name = input('Name: ')
        self.species = input('Species: ')
        self.gender = input('Gender: ')
        print('Pack your bag for the journey:')
        self.snack = input('Snack: ')
        self.weapon = input('Weapon: ')
        self.tool = input('Tool: ')
        print('Choose your difficulty:')

        while True:
            for key, menu_text in MENU_ELEMENTS.MENU.value['level_menu'].items():
                print(f'{key}. {menu_text[0]}')
            self.diff_lev = None
            self.diff_lev_str = input()
            for key, menu_text in MENU_ELEMENTS.MENU.value['level_menu'].items():
                print (key, menu_text)
                if self.diff_lev_str == str(key) or self.diff_lev_str.lower() == menu_text[1]:
                    self.diff_lev = key
                    self.number_of_lives = 7 - 2 * self.diff_lev
            if self.diff_lev:
                break
            else:
                continue
        self.print_user_data()

    def print_user_data(self):
        print(f'Good luck on your journey, {self.user_name}!')
        print(f'Your character: {self.name}, {self.species}, {self.gender}')
        print(f'Your inventory: {self.snack}, {self.weapon}, {self.tool}')
        print(f'Difficulty: {MENU_ELEMENTS.MENU.value['level_menu'][self.diff_lev][1]}')
        print(f'Number of lives: {self.number_of_lives}')

class Main_Logic():
    def __init__(self):
        self.program_status = 'MAIN MENU'
        self.main_loop()

    def print_actual_menu(self, menu_type):
        # print(menu_type)
        for key, menu_text in MENU_ELEMENTS.MENU.value[menu_type].items():
            print(f'{key}. {menu_text[0]}')

    def parse_command_input(self, input_string, menu_type = 'MAIN MENU'):
        for i in range(1, len(MENU_ELEMENTS.MENU.value[menu_type]) + 1):
            if input_string == str(i) or input_string.lower() == MENU_ELEMENTS.MENU.value[menu_type][i][1]:
                return str(i)
        return None

    def main_loop(self):
        print('***Welcome to the Trap Door***')
        while True:
            self.print_actual_menu(self.program_status)
            # print('\nEnter an option:')
            # ni = 'Not implemented!'
            unk_inp = 'Unknown input! Please enter a valid one.'
            command = self.parse_command_input(input(), self.program_status)
            match self.program_status, command:
                case 'MAIN MENU', '1':
                    print('Starting a new game...')
                    user_name = input("Enter a username ('/b' to go back): ")
                    if user_name != '/b':
                        my_game = TBAGame(user_name)
                        self.program_status = 'MAIN MENU'
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
