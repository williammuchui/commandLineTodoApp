##a commandline todo / tasks app
'''
use --help to show all the commands for the app
the app trues to access a tasks file in the local directory
if found well and nice, else the file is created
on --add a new task,, the file is written into
on --remove task by its index from the file,, by simply reading through the file and rewriting it without including the remove index task
on --list all tasks ,,the file is read through line by line and the results displayed

*no external libraries required for this basic version of the app unless you wanna expand the scope of its aplications
*I'm also thinking in a later stage to incorporating api data fetching from the web,,, yet to decide the application of this
'''
import os
import argparse

def create_parser():
	parser = argparse.ArgumentParser(description="Command-line Todo List App")
	parser.add_argument("-a", "--add", metavar="", help="Add a new Task")
	parser.add_argument("-l", "--list", action="store_true", help="list all Tasks")
	parser.add_argument("-r", "--remove", metavar="", help="Remove task by index")
	return parser

def add_task(task):
	with open('tasks.txt', 'a') as file:
		file.write(task +"\n")
	print("Task Added Successfully")

def list_tasks():
	if os.path.exists('tasks.txt'):
		with open('tasks.txt', 'r') as file:
			tasks = file.readlines()
			if len(tasks) == 0:
				print("You have no New tasks yet!")
			for index, task in enumerate(tasks, start=1):
				print(f"{index}. {task.strip()}")
	else:
		print("No tasks Found!")

def remove_task(index):
	if os.path.exists('tasks.txt'):
		with open('tasks.txt', 'r') as file:
			tasks = file.readlines()
		with open('tasks.txt', 'w') as file:
			for i, task in enumerate(tasks, start=1):
				if i != index:
					file.write(task)
		print("Task removed Successfully!!")
	else:
		print("No tasks Found!!")

def main():
	parser = create_parser()
	args = parser.parse_args()

	if args.add:
		add_task(args.add)
	elif args.list:
		list_tasks()	
	elif args.remove:
		remove_task(int(args.remove))
	else:
		parser.print_help()
	
if __name__ == "__main__":
	main()

