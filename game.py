'''
Save the game
 Report a typo
Description
The next thing we are going to implement is the saving feature.
First, let's add a new command. In addition to /h, /c, /i and /q commands, the player should now have an option to save the game progress via /s command. By saying "the game progress", we mean the game stats player reached. Update the output of /h by adding a new command to a list: /s => Save the game.
In your project directory, make a folder called data with a subfolder named saves. For now, it is empty, but to implement your save functionality, your program should create new JSON files and write the items from the game stats. Each JSON save file will be named with the player's username, such that its filepath looks like: data/saves/{username}.json. This way, each user will have their own save file. If the player saves the game and the save-file is already present - it is necessary to update it according to the current game situation.
Write the following game stats to your save file: the character traits; in-game inventory; namings for {snack}, {weapon} and {tool}; difficulty; remaining lives and the progress player reached (current level and scene). To understand how to write the stats to file you can check this example save JSON file for the user called 'new_user': data/saves/new_user.json. Follow the same structure exactly as you see in this example text file, with the necessary keys and values in the JSON.
In order for the player to realize that saving was successful, it is necessary to display the corresponding message Game saved! after calling /s command.
You can add some color to your text if you want to make it more fun. The Termcolor library can help you with that. Our tests do not check the color of your text.
Objectives
In this stage, your program should be able to:
1. Create save files for each user on /s command call with corresponding save-message.
2. Update the save-file if it is already present in saves folder.
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.
Example 1: saving the game after character creation
***Welcome to the Journey to Mount Qaf***
1. Start a new game (START)
2. Load your progress (LOAD)
3. Quit the game (QUIT)
> 1
Starting a new game...
Enter a username ('/b' to go back): > hyperskill
Create your character:
	Name: > John
	Species: > Human
	Gender: > male
Pack your bag for the journey:
	Snack: > apple
	Weapon: > sword
	Tool: > pickaxe
Choose your difficulty:
	1. Easy
	2. Medium
	3. Hard
> easy
Good luck on your journey, hyperskill!
Your character: John, Human, male
Your inventory: apple, sword, pickaxe
Difficulty: easy
Number of lives: 5
---------------------------
Once you reach the beginning of the Mount Qaf, you feel amazed by the majestic
mountain that you will conquer, at the end of this climb. You look at the snowy peaks while
thinking of how to start the journey. There is a hill before you.
1. Walk around a bit, maybe you'll find something interesting.
2. Walk up the hill and begin climbing.
3. Enjoy the scenery.
> /s
Game saved!
...
Save-file:
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
      "sword",
      "pickaxe"
    ]
  },
  "progress": {
    "level": "level1",
    "scene": "scene1"
  },
  "lives": 5,
  "difficulty": "easy"
}
Example 2: updating the save-file after some actions performed
...
The voice says 'Too bad, I thought you were clever! Should I give you another chance?' as it gets closer to you.
------ Lives remaining: 3 ------
"Of course it was the wrong answer, how could I be so wrong?" you thought.
1. A mosquito.
2. A bumblebee.
> /s
Game saved!
...
Save-file:
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
      "apple"
    ]
  },
  "progress": {
    "level": "level1",
    "scene": "scene9"
  },
  "lives": 3,
  "difficulty": "easy"
}
Write a program

Z <https://hyperskill.org/projects/161/stages/837/implement> 

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

    # def actual_scene_options_dict(self):
    #     scene_options_dict = self.scene_options_dict()
    #     for key in scene_options_dict:
    #         print(f'{key}. {self.brackets_in_text_verified(scene_options_dict[key]['option_text'])}')


    def change_scene(self, next_scene):
        if next_scene == 'end':
            if self.actual_level == 'level2':
                self.actual_level = 'end'
            else:
                self.actual_level = self.all_scenes_dict[self.actual_level]['next']
                print(f'------ Level {self.actual_level[-1]} ------')
                self.actual_scene_within_level = 'scene1'
        else:
            self.actual_scene_within_level = next_scene
        # print(self.actual_scene_within_level)

class User():
    def __init__(self, user_name):
        self.user_name = user_name
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
            for key in self.inventory:
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

    def save_game(self):
        content_list = self.game_user.inventory_list()
        save_dict= {"character": {"name": self.game_user.name, "species": self.game_user.species, "gender": self.game_user.gender},
            "inventory": {"snack_name": self.game_user.snack, "weapon_name": self.game_user.weapon, "tool_name": self.game_user.tool, "content": content_list},
            "progress": {"level": scene_maker.actual_level, "scene": scene_maker.actual_scene_within_level},
            "lives": self.game_user.number_of_lives,
            "difficulty": self.game_user.diff_lev_str}

        save_path = f'data/saves/{self.game_user.user_name}.json'
        print(save_path)
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
                    print('No saved data found')
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
                            # print(scene_options_dict[game_command]['next'])
                            if self.game_user.number_of_lives == 0:
                                scene_maker.change_scene('scene1')
                                self.game_user.change_live('heal')
                            else:
                                scene_maker.change_scene(scene_options_dict[game_command]['next'])
                                if scene_maker.actual_level == 'level2':
                                    self.program_status = 'QUIT'
                                    # print('Thanks for playing!')
                                    return
                            break
                        else:
                            print('Unknown input! Please enter a valid one.')
                            continue

if __name__ == '__main__':
    scene_maker = SceneMaker()
    main_logic = Main_Logic()

