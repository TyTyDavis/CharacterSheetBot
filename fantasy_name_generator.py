from random import randrange

running = False

#first_name_male = []
#first_name_female = []

#last_name = []

welcome_message = "Welcome to Fantasy Name Generator!"
male_or_female_message = "Is your character male or female? Enter M or F.."


first_time = True

def line_appender(file_path, target):
	file = open(file_path, "r")
	splitfile = file.read().splitlines()
	for line in splitfile:
		target.append(line)

def name_selector(target_list):
	selected = target_list[randrange(len(target_list))]
	return selected

def name_builder(first_name_list_path, last_name_list_path):
	first_name_list = []
	last_name_list = []

	line_appender(first_name_list_path, first_name_list)
	line_appender(last_name_list_path, last_name_list)

	first_name_selected = name_selector(first_name_list)
	last_name_selected = name_selector(last_name_list)

	name = first_name_selected+" "+last_name_selected
	return name


while running:

	if first_time:
		print(welcome_message)

	user_input = input(male_or_female_message)

	if user_input == "M" or user_input == "m":

		name = name_builder("first_name_male.txt", "last_name.txt")
		print(name)
		first_time = False

	elif user_input == "F" or user_input == "f":
		name = name_builder("first_name_female.txt", "last_name.txt")
		print(name)
		first_time = False

	else:
		print("please specify gender")
		first_time = False