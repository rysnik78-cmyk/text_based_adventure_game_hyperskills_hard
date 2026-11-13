'''
Gameplay time!
 Report a typo
Description
In this stage, you are going to add some new commands to a game, implement the core game features and the first level of the game.
Let's start with adding new commands to a game, as this part is much simpler. When the player just reached the game loop after initializing character he should be able to call four possible commands: /h (show the help page with commands available to the player), /q (quit the game), and /i, /c (view inventory contents and information about character respectively). Make sure, that output on each command is formatted like in the examples.
Weapon, tool and snack, that player entered before should be added to inventory before the game loop. Also, there is no need to output anything on /q command.
The second part of this stage is gameplay creation. First, you need to read the contents of the story.json file. Download the file from the link and place it in a new subfolder data in your project directory. In this JSON file, you can see everything related to the story.
Usually games of this genre are divided into several levels, which in turn are divided into multiple scenes. In each scene, the player sees the situation in which he/she finds himself/herself right now and several options that can be performed in order to influence the further continuation of the story. Each chosen option is followed by the result text of that option, the effect on the character and the scene.
The structure of the json file, contains all the elements above as follows (for now second level is an empty object):
1. First level{N} has a next key that contains a string with a next level key, and a scenes key with all the scenes used in level.
2. Each scene{N} has a text key that contains a string with a text, that describes the situation, and an options key with a list of possible options, that can be performed in this scene.
3. Each option has 4 keys:
• option_text - A string that is displayed to the player as an action option
• result_text - A string that is displayed to the player if he selects this option
• actions - A list of outcome effects that are applied to the character on this option. Possible effects: +{item}, -{item} - item is added to or removed from the inventory; hit - character loses one health; heal - character restores one health
• next - A string with a key for next scene. Can take the value 'end', which will mean the end of the level.
Some strings in file may contain '{tool}', '{weapon}' or '{snack}' substrings. As you may have already guessed, instead of them, you should print/use the values entered earlier accordingly.
Let's move on to the core game loop. When player enters any scene print it's text value and options in such format: {n}. {option_text}, where n is a number of option, starting from 1. Also, you need to satisfy the following requirements:
• The game loop should check for the number of lives and if there are no lives remaining, the game should restart from the current level with a You died! message.
• For now if the player reached the 'end' as the next scene output the Level 2 message and end the program.
Feedbacks on each possible outcome effects:
+{item}	Item added: {item}
-{item}	Item removed: {item}
hit/heal	Lives remaining: {number_of_lives}
Don't forget that the program must be case-insensitive, and incorrect input must be followed by a Unknown input! Please enter a valid one. message
(Optional) Additional requirements in case you want to write your own story.
Objectives
1. (Optional) Write your own story, following the requirements mentioned earlier;
2. Add to the program the ability to correctly process commands /h, /q, /i and /c;
3. Read the story content, replacing '{tool}', '{weapon}' or '{snack}' substrings with appropriate ones;
4. Implement a game loop that correctly tells a story based on the file;
5. Correctly process user input in a game loop and give an appropriate feedback.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.
Example 1: the player finishes it's character creation and enters the game loop.
***Welcome to the Journey to Mount Qaf***
1. Start a new game (START)
2. Load your progress (LOAD)
3. Quit the game (QUIT)
> 1
Starting a new game...
Enter a username ('/b' to go back): > Hyperskill
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
> hard
Good luck on your journey, Hyperskill!
Your character: John, Human, male
Your inventory: apple, sword, pickaxe
Difficulty: hard
Number of lives: 1
---------------------------
Once you reach the beginning of the Mount Qaf, you feel amazed by the majestic
mountain that you will conquer, at the end of this climb. You look at the snowy peaks while
thinking of how to start the journey. There is a hill before you.
1. Walk around a bit, maybe you'll find something interesting.
2. Walk up the hill and begin climbing.
3. Enjoy the scenery.
...
Example 2: scene switching.
...
Once you reach the beginning of the Mount Qaf, you feel amazed by the majestic
mountain that you will conquer, at the end of this climb. You look at the snowy peaks while
thinking of how to start the journey. There is a hill before you.
1. Walk around a bit, maybe you'll find something interesting.
2. Walk up the hill and begin climbing.
3. Enjoy the scenery.
> 3
You admired the majestic view of the mountain!
That view was really astounding! But we can't stand here forever, mesmerized by it
1. Walk around a bit, maybe you'll find something interesting.
2. Walk up the hill and begin climbing.
...
Example 3: scene switching with +{item} action.
...
> 1
In a small cave nearby you found a key.
------ Item added: key ------
...
Example 4: scene switching with -{item} action.
...
> 2
You go up the mountain, using the pickaxe
------ Item removed: pickaxe ------
...
Example 5: scene switching with hit action.
...
> 1
Unfortunately, the source of the sound was a large rat that took advantage of your carelessness
and bit your leg.
You've tried to run further up the staircase.
------ Lives remaining: 4 ------
...
Example 6: scene switching with heal and -{item} actions.
...
> 3
When the sword hit the source of the sound, it went silent.
That gave you confidence and you've calmly continued your way up.
------ Item removed: sword ------
------ Lives remaining: 6 ------
...
Example 7: proceeding to the next level.
...
> 3
The darkness says 'Correct! You may pass traveller.'
You saw a light coming from the inner cave and you follow it.
------ Level 2 ------
Example 8: character dies.
...
> 1
Unfortunately, the source of the sound was a large rat that took advantage of your carelessness
and bit your leg.
You've tried to run further up the staircase.
------ You died ------
Once you reach the beginning of the Mount Qaf, you feel amazed by the majestic
mountain that you will conquer, at the end of this climb. You look at the snowy peaks while
thinking of how to start the journey. There is a hill before you.
1. Walk around a bit, maybe you'll find something interesting.
2. Walk up the hill and begin climbing.
3. Enjoy the scenery.
...
Example 9: calling commands.
...
> /h
Type the number of the option you want to choose.
Commands you can use:
/i => Shows inventory.
/q => Exits the game.
/c => Shows the character traits.
/h => Shows help.
> /c
Your character: John, Human, male.
Lives remaining: 1
> /i
Inventory: apple, sword, key
> /q
Thanks for playing!
Example 10: one of scenarios from start to the end


Write a program

Z <https://hyperskill.org/projects/161/stages/836/implement> 
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
/h => Shows help.'''}

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

