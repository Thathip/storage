import sys
import urllib.parse
import subprocess

def process_command(argument):
    # Remove cmd:// or cmd:\\ prefix
    if argument.startswith("cmd://"):
        command = argument[len("cmd://"):]
    elif argument.startswith("cmd:%5C%5C"):
        command = argument[len("cmd:%5C%5C"):]
    else:
        raise ValueError("Invalid argument format")

    # Remove trailing slash if it exists
    if command.endswith("/"):
        command = command[:-1]

    # Decode ASCII encoding like %20 to space
    command = urllib.parse.unquote(command)

    # Print the parsed command for debugging
    print(" ")
    print("Parsed command:")
    print(command)
    print(" ")

    # Confirm pass-through
    confirm = input("Confirm pass-through? [y/n]: ").strip().lower()
    if confirm != 'y':
        print("Execution canceled")
        return

    # Execute the parsed command
    try:
        process = subprocess.run(command, shell=True, check=True)
        print("Command executed successfully")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <cmd://command or cmd:\\command>")
        sys.exit(1)

    argument = sys.argv[1]
    try:
        print("Argument passed to parser:")
        print(argument)
        process_command(argument)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()