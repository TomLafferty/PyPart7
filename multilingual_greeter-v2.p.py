from typing import Dict

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {
    1: 'English',
    2: 'French'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {
    1: 'What is your name?',
    2: 'Quel est ton nom?'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {
    1: 'Hello',
    2: 'Bonjour'
}



def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print("Please choose a language: ")
    for key, value in lang_options.items():
        print(f"{key}: {value}")

def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    return int(input())


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    return lang_choice in lang_options


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    if lang_choice in name_prompt_options:
        return name_prompt_options[lang_choice]
    else:
        print("invalid")


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    name = input(name_prompt)
    return name


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    print(greetings_options[lang_choice], name)



#
# new_key_val = list(lang_dict.keys())[-1] + 1
# print(new_key_val)


if __name__ == '__main__':
    '''add admin mode'''
    mode_selection = input("1: User mode\n2: Admin mode\n")
    if mode_selection == '1':
        print_language_options(lang_dict)
        chosen_lang = language_input()
        while language_choice_is_valid(lang_dict, chosen_lang) is False:
            print("Invalid selection. Try again.")
            chosen_lang = language_input()

        selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
        chosen_name = name_input(selected_prompt)
        greet(chosen_name, greetings_dict, chosen_lang)
    elif mode_selection == '2':
        admin_option = input('1: Add support for additional languages\n2: Update greetings for existing languages\n')
        if admin_option == '1':
            new_lang_name = input('Language to be added:\n')
            new_lang_prompt = input('Prompt for name in new language:\n')
            new_lang_greeting = input('Greeting for new language:\n')
            new_key_val = list(lang_dict.keys())[-1] + 1
            lang_dict[new_key_val] = new_lang_name
            name_prompt_dict[new_key_val] = new_lang_prompt
            greetings_dict[new_key_val] = new_lang_greeting
            print_language_options(lang_dict)
            chosen_lang = language_input()
            while language_choice_is_valid(lang_dict, chosen_lang) is False:
                print("Invalid selection. Try again.")
                chosen_lang = language_input()

            selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
            chosen_name = name_input(selected_prompt)
            greet(chosen_name, greetings_dict, chosen_lang)


        elif admin_option == '2':
            print_language_options(lang_dict)
            lang_to_change = input('Ref # of language to be changed:\n')
            if int(lang_to_change) in lang_dict is True:
                new_greeting = input('Input new greeting:\n')
                greetings_dict[lang_to_change] = new_greeting

            else:
                print('Invalid')
            prompt_change = input('New prompt')
