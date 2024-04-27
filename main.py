#!/usr/bin/python
import sys
import subprocess as sp


def create_file(file_to_create):
    """ Creates a file containing a list of orphaned packages using pacman. """
    try:
        sp.run(f"pacman -Qdt > {file_to_create}", shell=True)
        sys.exit(f"File {file_to_create} created.")
    except Exception as e:
        print("Couldn't create file.")
        print(e)

        
def delete_program(file_to_del, dep):
    """ Deletes programs listed in the given file. """
    try:
        with open(file_to_del, "r") as f:
            programs = []
            for line in f:
                if line.strip():
                    program_name = line.split()[0]
                    programs.append(program_name)
        
        if len(programs) == 0:
            sys.exit("No programs to remove.")

        print("Packages to remove (dep not shown)")
        print(" ".join(programs) + "\n")


        confirm = input("Do you wish to continue? (y/N): ")

        if confirm.lower() == "y":
        
            if dep == True:
                sp.run(f"sudo pacman -Rns {' '.join(programs)}", shell=True)    
                print("Programs have been removed.")
            
            elif dep == False:
                sp.run(f"sudo pacman -R {' '.join(programs)}", shell=True)    
                print("Programs have been removed.")       

        else:
            print("Operation cancelled.")
            
            
    except FileNotFoundError:
        sys.exit(f"File {file_to_del} not found.")
    except subprocess.CalledProcessError as e:
        sys.exit(f"Failed to remove programs: {e}")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")
        

def display_help():
    """Displays help information about how to use this script."""
    help_text = """
Usage: script.py [OPTION] [FILE]
Manage orphaned packages with pacman.

Options:
  -c FILE      Create a file with a list of orphaned packages.
  -r FILE      Remove the orphaned packages listed in the specified file.
  --rd FILE     Remove the orphaned packages and their unneeded dependencies listed in the specified file.
  -h, --help   Display this help and exit.

Examples:
  script.py -c orphans.txt     # Writes a list of orphaned packages to orphans.txt
  script.py -r orphans.txt     # Removes all packages listed in orphans.txt without removing dependencies
  script.py --r orphans.txt    # Removes all packages listed in orphans.txt along with their unneeded dependencies
    """
    print(help_text)
    

def spell_errors(option):
    if option == "-rd":
        print(f"Invalid option {option}. Did you mean --rd?")
        return True
    else:
        return False

    
def main():

    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        sys.exit(display_help())
    
    if len(sys.argv) != 3:
        sys.exit("Usage: ./script.py -c|-r <filename>. Use -h or --help for help.")
        
    option, filename = sys.argv[1], sys.argv[2]

    if spell_errors(option) == True:
        sys.exit()
    else:
        pass
    
    if option == "-c":
        create_file(filename)
    elif option == "-r":
        delete_program(filename, False)
    elif option == "--rd":
        delete_program(filename, True)
    
    else:
        sys.exit(f"Invalid option {option}. Use -h or --help for help. ")


if __name__ == "__main__":
    main()
