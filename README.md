# Python script to remove unwanted arch linux packages

## What this script does?
This script orphan packages in Arch Linux.
Orphan packages can be seen using ```pacman -Qdt``` command. This script aims to delete all the packages shown by ```pacman -Qdt``` command at once.

## Usage
```
script.py -c orphans.txt      # Writes a list of orphaned packages to orphans.txt
script.py -r orphans.txt      # Removes all packages listed in orphans.txt without removing dependencies
script.py --rd orphans.txt    # Removes all packages listed in orphans.txt along with their unneeded dependencies
```
