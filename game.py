'''
Load the game
 Report a typo
Description
In this stage, you are going to implement the loading feature in your game. Don't forget to add Level 2! If you wish, you can write the next level by yourself following the requirements from the third stage or by analogy with the first level. Otherwise, replace the previously used story-file with a new one story.json, already formed in advance.
We already included the loading option in our menu. Now it's time to polish it.
First, you need to check how many users are stored in the save folder. Output Choose username (/b - back): message, show the list of the usernames without the %.json% extension and take the user input. If the user input is the /b command, return the player to the main menu in the same way as for the game start option. Otherwise, read the save file, belonging to this username.
Once you loaded the save, you need to bring the game stats back into the game. Print Loading your progress... and Level {n} messages. Show last scene's text with options, so that after loading, the game will resume from where the player left off the last time.
The tests do not check if your program has finished at the end of both levels, so that you can modify the game as you want and add more and more interesting levels.
And again, don't forget that the program must be case-insensitive, and incorrect input must be followed by a Unknown input! Please enter a valid one. message
Good luck on your future journeys, travelers!
Objectives
1. (Optional) Write your own second level, following the requirements mentioned in third stage;
2. Show the list of usernames with saves if user chooses load option;
3. Take the user input to load the game (or /b command to return back to main menu). Use the prompt mentioned earlier to signal the user to start typing;
4. Load the player state from save-file, so that user can resume from where he left off last time. Don't forget to output level and last scene's text with options.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.
Example 1: moving to the second level.
...
> 3
The darkness says 'Correct! You may pass traveller.'
You saw a light coming from the inner cave and you follow it.
------ Level 2 ------
You stand before a narrow, treacherous path that winds along the mountain's edge.
The wind howls, and the path looks perilous. What will you do?
1. Bravely attempt the treacherous path.
2. Search for an alternate route.
...
Example 2: loading the game from save-file.
hyperskill.json:
{
  "character": {
    "name": "John",
    "species": "Human",
    "gender": "male"
  },
  "inventory": {
    "snack_name": "apple",
    "weapon_name": "sword",
    "tool_name": "pickaxe",
    "content": [
      "apple",
      "sword"
    ]
  },
  "progress": {
    "level": "level2",
    "scene": "scene4"
  },
  "lives": 5,
  "difficulty": "easy"
}
***Welcome to the Journey to Mount Qaf***
1. Start a new game (START)
2. Load your progress (LOAD)
3. Quit the game (QUIT)
> 2
Choose username (/b - back):
another_user
hyperskill
> hyperskill
Loading your progress...
------ Level 2 ------
You ascend higher, the air getting thinner as you approach the summit.
The landscape becomes more rugged and desolate.
Suddenly, you stumble upon an injured traveler lying on the ground.
1. Offer your assistance and heal the traveler's wounds.
2. Keep your guard up and cautiously approach the traveler.
Example 3: incorrect input and back command.
Thanks for playing!
***Welcome to the Journey to Mount Qaf***
1. Start a new game (START)
2. Load your progress (LOAD)
3. Quit the game (QUIT)
> 2
Choose username (/b - back):
another_user
hyperskill
> not_existing_username
Unknown input! Please enter a valid one.
> /b
***Welcome to the Journey to Mount Qaf***
1. Start a new game (START)
2. Load your progress (LOAD)
3. Quit the game (QUIT)

Write a program

Z <https://hyperskill.org/projects/161/stages/838/implement> 
'''



# write your code here
from enum import Enum
import json
import os

class MENU_ELEMENTS(Enum):
    MENU = {'MAIN MENU' : {1:['Start a new game (START)', 'start'], 2: ['Load your progress (LOAD)', 'load'], 3: ['Quit the game (QUIT)', 'quit']},
            'level_menu' : {1:['Easy', 'easy'], 2: ['Medium', 'medium'], 3: ['Hard', 'hard']},
            'help_string' : '''Type the number of the option you want to choose.
Commands you can use:
/i => Shows inventory.
/q => Exits the game.
/c => Shows the character traits.
/h => Shows help.
/s => Save the game,'''}

class SceneMaker:
    def __init__(self):
        # TODO
        print(os.getcwd())
        # scene_file = open('../data/story2.json', 'r')
        scene_file = open('data/story.json', 'r')
        self.all_scenes_dict = json.load(scene_file)
        scene_file.close()
        self.actual_level = 'level1'
        self.actual_scene_within_level = 'scene1'

    def print_actual_scene_output(self):
        # description

        return self.all_scenes_dict[self.actual_level]['scenes'][self.actual_scene_within_level]['text']
        # options

    def scene_options_dict(self):
        scene_options_list = self.all_scenes_dict[self.actual_level]['scenes'][self.actual_scene_within_level]['options']
        return {str(n + 1): scene_options_list[n] for n in range(len(scene_options_list))}

    def change_scene(self, next_scene):
        if next_scene == 'end':
            if self.actual_level == 'level3':
                self.actual_level = 'end'
            else:
                self.actual_level = self.all_scenes_dict[self.actual_level]['next']
                print(f'------ Level {self.actual_level[-1]} ------')
                self.actual_scene_within_level = 'scene1'
        else:
            self.actual_scene_within_level = next_scene
        # print(self.actual_scene_within_level)

class User():
    def __init__(self, user_name, clean=False):
        self.user_name = user_name
        if not clean:
            print('Create your character:')
            self.name = input('Name: ')
            self.species = input('Species: ')
            self.gender = input('Gender: ')
            self.diff_lev_str = None
            self.diff_lev_int = None
            print('Pack your bag for the journey:')
            self.snack = input('Snack: ')
            self.weapon = input('Weapon: ')
            self.tool = input('Tool: ')
            self.inventory = {'snack': {'state':True, 'text': self.snack},
                              'weapon': {'state': True, 'text': self.weapon},
                              'tool': {'state': True, 'text': self.tool},
                              'key': {'state': False, 'text': 'key'},
                              'amulet': {'state': False, 'text': 'amulet'},
                              'potion': {'state': False, 'text': 'potion'}}
            print('Choose your difficulty:')
            for key, menu_text in MENU_ELEMENTS.MENU.value['level_menu'].items():
                print(f'{key}. {menu_text[0]}')
            while True:
                self.diff_lev_str = input()
                for key, menu_text in MENU_ELEMENTS.MENU.value['level_menu'].items():

                    if self.diff_lev_str == str(key) or self.diff_lev_str.lower() == menu_text[1]:
                        self.diff_lev_int = key
                        self.number_of_lives = 7 - 2 * self.diff_lev_int
                if self.diff_lev_int:
                    break
                else:
                    print('Unknown input! Please enter a valid one.')
                    continue
            self.print_user_data()
        else:
            self.name = None
            self.species = None
            self.gender = None
            self.diff_lev_str = None
            self.diff_lev_int = None
            self.snack = None
            self.weapon = None
            self.tool = None
            self.inventory = None
            self.diff_lev_str = None
            self.number_of_lives = None
            self.diff_lev_int = None

    def print_user_data(self):
        print(f'Good luck on your journey, {self.user_name}!')
        print(f'Your character: {self.name}, {self.species}, {self.gender}')
        print(f'Your inventory: {self.snack}, {self.weapon}, {self.tool}')
        print(f'Difficulty: {MENU_ELEMENTS.MENU.value['level_menu'][self.diff_lev_int][1]}')
        print(f'Number of lives: {self.number_of_lives}')
        print('---------------------------')

    def show_traits(self):
        print(f'Your character: {self.name}, {self.species}, {self.gender}.')
        print(f'Lives remaining: {self.number_of_lives}')

    def show_inventory(self):
        inventory_string = 'Inventory: '
        for key in self.inventory:
            if self.inventory[key]['state']:
                inventory_string = inventory_string + self.inventory[key]['text'] + ', '
        print(inventory_string[:-2])

    def inventory_list(self):
        # ["apple", "sword", "pickaxe"]
        inventory_list = []
        for key in self.inventory:
            if self.inventory[key]['state']:
                inventory_list.append(self.inventory[key]['text'])
        return inventory_list

    def change_inventory(self, item):
        if '-' in item.lower():
            for key in self.inventory.keys():
                if key in item.lower():
                    self.inventory[key]['state'] = False
                    print(f'------ Item removed: {self.inventory[key]['text']} ------')
                    return

        elif '+' in item.lower():
            for key in self.inventory:
                if key in item.lower():
                    self.inventory[key]['state'] = True
                    print(f'------ Item added: {self.inventory[key]['text']} ------')
                    return
        else:
            print('Unknown input! Please enter a valid one.')

    def change_live(self, action):
        if action.lower() == 'heal':
            self.number_of_lives += 1
        if action.lower() == 'hit':
            self.number_of_lives -= 1
        if self.number_of_lives == 0:
            print('------ You died ------')
        else:
            print(f'------ Lives remaining: {self.number_of_lives} ------')

class Main_Logic():
    def __init__(self):
        self.game_user = None
        self.program_status = 'MAIN MENU'
        self.main_loop()

    def load_game(self):
        file_list = os.listdir('data/saves')
        saved_game_files_list = [x[:-5] for x in file_list if x.endswith('.json')]
        if not saved_game_files_list:
            print('No saved data found')
            return
        else:
            # saved_game_files_dict = {str(i): saved_game_files_list[i - 1] for i in range(1, len(saved_game_files_list) + 1)}
            for save in saved_game_files_list:
                print(save)
            print('Choose username (/b - back):')
            while True:
                save_choice = input()
                if save_choice in saved_game_files_list:
                    print('Loading your progress...')
                    break
                elif save_choice.lower() == '/b':
                    return
                else:
                    print('Unknown input! Please enter a valid one.')
                    continue
        save_path = f'data/saves/{save_choice}.json'
        with open(save_path, 'r') as json_file:
            save_dict = json.load(json_file)
        self.game_user = User(save_choice, clean=True)
        self.game_user.name = save_dict['character']['name']
        self.game_user.species = save_dict['character']['species']
        self.game_user.gender = save_dict['character']['gender']
        self.game_user.snack = save_dict['inventory']['snack_name']
        self.game_user.weapon = save_dict['inventory']['weapon_name']
        self.game_user.tool = save_dict['inventory']['tool_name']
        self.game_user.inventory = {'snack': {'state': False, 'text': self.game_user.snack},
                                'weapon': {'state': False, 'text': self.game_user.weapon},
                                'tool': {'state': False, 'text': self.game_user.tool},
                                'key': {'state': False, 'text': 'key'},
                                'amulet': {'state': False, 'text': 'amulet'},
                                'potion': {'state': False, 'text': 'potion'}}
        # print(save_dict['inventory']['content'])
        for element in save_dict['inventory']['content']:
            # print(element)
            if element == self.game_user.snack:
                self.game_user.inventory['snack']['state'] = True
            if element == self.game_user.weapon:
                self.game_user.inventory['weapon']['state'] = True
            if element == self.game_user.tool:
                self.game_user.inventory['tool']['state'] = True
            elif element in self.game_user.inventory.keys():
                 print(element, self.game_user.inventory[element])
                 self.game_user.inventory[element]['state'] = True
        # print(self.game_user.inventory)
        scene_maker.actual_level = save_dict['progress']['level']
        print(f'------ Level {scene_maker.actual_level[-1]} ------')
        scene_maker.actual_scene_within_level = save_dict['progress']['scene']
        self.game_user.number_of_lives = save_dict['lives']
        self.game_user.diff_lev_str = save_dict['difficulty']
        for key, menu_text in MENU_ELEMENTS.MENU.value['level_menu'].items():
            if self.game_user.diff_lev_str == str(key) or self.game_user.diff_lev_str.lower() == menu_text[1]:
                self.game_user.diff_lev_int = key

    def save_game(self):
        content_list = self.game_user.inventory_list()
        # print(content_list)
        save_dict= {"character": {"name": self.game_user.name, "species": self.game_user.species, "gender": self.game_user.gender},
            "inventory": {"snack_name": self.game_user.snack, "weapon_name": self.game_user.weapon, "tool_name": self.game_user.tool, "content": content_list},
            "progress": {"level": scene_maker.actual_level, "scene": scene_maker.actual_scene_within_level},
            "lives": self.game_user.number_of_lives,
            "difficulty": self.game_user.diff_lev_str}
        save_path = f'data/saves/{self.game_user.user_name}.json'
        # print(save_path)
        with open(save_path, 'w') as json_file:
            json.dump(save_dict, json_file)
        print('Game saved!')

    def brackets_in_text_verified(self, text):
        if '{tool}' in text:
            text = text.replace('{tool}', self.game_user.tool)
        if '{weapon}' in text:
            text = text.replace('{weapon}', self.game_user.weapon)
        if '{snack}' in text:
            text = text.replace('{snack}', self.game_user.snack)
        return text

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
        while self.program_status != 'QUIT':
            print('***Welcome to the Trap Door***')
            self.print_actual_menu(self.program_status)
            # print('\nEnter an option:')
            # ni = 'Not implemented!'
            unk_inp = 'Unknown input! Please enter a valid one.'
            command = self.parse_command_input(input(), self.program_status)
            match self.program_status, command:
                case 'MAIN MENU', '1':
                    print('Starting a new game...')
                    user_name = input("Enter a username ('/b' to go back): ")
                    if user_name.lower() != '/b':
                        self.game_user = User(user_name)
                        self.game_loop()
                    continue
                case 'MAIN MENU', '2':
                    self.load_game()
                    if self.game_user:
                        self.game_loop()
                    # self.program_status = 'TOP TEN MENU'
                    continue
                case 'MAIN MENU', '3':
                    print('Goodbye!')
                    break
                case 'MAIN MENU', _:
                    print(unk_inp)
                    continue

    def game_loop(self):
        while True:
            print(self.brackets_in_text_verified(scene_maker.print_actual_scene_output()))
            scene_options_dict = scene_maker.scene_options_dict()
            for key in scene_options_dict:
                print(f'{key}. {self.brackets_in_text_verified(scene_options_dict[key]['option_text'])}')
            while True:
                game_command = input()
                match game_command.lower():
                    case '/h':
                        print(MENU_ELEMENTS.MENU.value['help_string'])
                        continue
                    case '/i': # => Shows inventory.'
                        self.game_user.show_inventory()
                        continue
                    case '/q':  # => Exits the game.
                        self.program_status = 'QUIT'
                        # print('Thanks for playing!')
                        return
                    case '/c': # => Shows the character traits.
                        self.game_user.show_traits()
                        continue
                    case '/s': # => Save the game
                        self.save_game()
                        continue
                    case _:
                        if game_command in scene_options_dict:
                            print(self.brackets_in_text_verified(scene_options_dict[game_command]['result_text']))
                            # process actions
                            for action in scene_options_dict[game_command]['actions']:
                                if '+' in action or '-' in action:
                                    self.game_user.change_inventory(action)
                                if 'hit' in action.lower() or 'heal' in action.lower():
                                    self.game_user.change_live(action)
                            print(self.game_user.inventory)
                            # print(scene_options_dict[game_command]['next'])
                            if self.game_user.number_of_lives == 0:
                                scene_maker.change_scene('scene1')
                                self.game_user.change_live('heal')
                            else:
                                scene_maker.change_scene(scene_options_dict[game_command]['next'])
                                if scene_maker.actual_level == 'end':
                                    self.program_status = 'QUIT'
                                    print('Thanks for playing!')
                                    return
                            break
                        else:
                            print('Unknown input! Please enter a valid one.')
                            continue

if __name__ == '__main__':
    scene_maker = SceneMaker()
    main_logic = Main_Logic()

