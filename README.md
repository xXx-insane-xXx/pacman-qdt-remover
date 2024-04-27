# Python script to remove unwanted arch linux packages

## What this script does?
This script removes orphan packages in Arch Linux.
Orphan packages can be seen using ```pacman -Qdt``` command. This script aims to delete all the packages shown by ```pacman -Qdt``` command at once.

## Usage
```
script.py -c orphans.txt      # Writes a list of orphaned packages to orphans.txt
script.py -r orphans.txt      # Removes all packages listed in orphans.txt without removing dependencies
script.py --rd orphans.txt    # Removes all packages listed in orphans.txt along with their unneeded dependencies
```

## Note
Currently the code is in beta version, so it contains some security flaws, which will be eventually fixed.

## Future plans
Call the python script using a bash executable file which can then be placed in $PATH to be used hassle-free.
