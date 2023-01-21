# DiceMaster
![Version](https://img.shields.io/badge/Version-3.4.0-blueviolet?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open%20Source%20%3F-Yes%21-blue?style=for-the-badge&logo=github)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-orange?style=for-the-badge&logo=Python)](https://www.python.org/)
![Love](https://img.shields.io/badge/Made%20with-Love-pink?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+R2l0SHViIFNwb25zb3JzIGljb248L3RpdGxlPjxwYXRoIGQ9Ik0xNy42MjUgMS40OTljLTIuMzIgMC00LjM1NCAxLjIwMy01LjYyNSAzLjAzLTEuMjcxLTEuODI3LTMuMzA1LTMuMDMtNS42MjUtMy4wM0MzLjEyOSAxLjQ5OSAwIDQuMjUzIDAgOC4yNDljMCA0LjI3NSAzLjA2OCA3Ljg0NyA1LjgyOCAxMC4yMjdhMzMuMTQgMzMuMTQgMCAwIDAgNS42MTYgMy44NzZsLjAyOC4wMTcuMDA4LjAwMy0uMDAxLjAwM2MuMTYzLjA4NS4zNDIuMTI2LjUyMS4xMjUuMTc5LjAwMS4zNTgtLjA0MS41MjEtLjEyNWwtLjAwMS0uMDAzLjAwOC0uMDAzLjAyOC0uMDE3YTMzLjE0IDMzLjE0IDAgMCAwIDUuNjE2LTMuODc2QzIwLjkzMiAxNi4wOTYgMjQgMTIuNTI0IDI0IDguMjQ5YzAtMy45OTYtMy4xMjktNi43NS02LjM3NS02Ljc1em0tLjkxOSAxNS4yNzVhMzAuNzY2IDMwLjc2NiAwIDAgMS00LjcwMyAzLjMxNmwtLjAwNC0uMDAyLS4wMDQuMDAyYTMwLjk1NSAzMC45NTUgMCAwIDEtNC43MDMtMy4zMTZjLTIuNjc3LTIuMzA3LTUuMDQ3LTUuMjk4LTUuMDQ3LTguNTIzIDAtMi43NTQgMi4xMjEtNC41IDQuMTI1LTQuNSAyLjA2IDAgMy45MTQgMS40NzkgNC41NDQgMy42ODQuMTQzLjQ5NS41OTYuNzk3IDEuMDg2Ljc5Ni40OS4wMDEuOTQzLS4zMDIgMS4wODUtLjc5Ni42My0yLjIwNSAyLjQ4NC0zLjY4NCA0LjU0NC0zLjY4NCAyLjAwNCAwIDQuMTI1IDEuNzQ2IDQuMTI1IDQuNSAwIDMuMjI1LTIuMzcgNi4yMTYtNS4wNDggOC41MjN6Ii8+PC9zdmc+)
![Smyles](https://img.shields.io/badge/Makes%20people-Smyle-cyan?style=for-the-badge)

Copyright (C) 2023 - Luis Miguel Isea

DiceMaster is a Python project that can be used for **rolling any number of dice of any number of faces.**
It is also my first Python project by the way :D

The amazing thing about this project is that **it has a basic menu**, allowing the user to read the instructions as many times as desired.
Also DiceMaster can do as many rollings as the user wants without having to reinitialize or exit the program.

Python Version I used: **Python 3.10.4**

## HOW TO RUN?
It's really easy: first, clone the repository, then make sure the ***sshkeyboard*** library is installed and, finally, run [***run.py***](https://github.com/lmisea/dicemaster/blob/main/run.py).

### Step 1: Clone the dicemaster repository
Open a terminal in the directory where you want to install the program and then clone this repository by typing this command:
```sh
git clone https://github.com/lmisea/dicemaster.git
```
### Step 2: Install the requirements
A third-party Python library called ***sshkeyboard*** under the [MIT License](https://github.com/ollipal/sshkeyboard/blob/main/LICENSE) is required for running DiceMaster.

GitHub Repository of the Library: [Sshkeyboard-Repository](https://github.com/ollipal/sshkeyboard).

**How to Install sshkeyboard?** Make sure the terminal is open in the directory where the repository was clone and the execute this command in the terminal:
```sh
pip3 install -r requirements.txt
```
This will install the exact same library version I used for my project and therefore there will not be any issue.

### Step 3: Run the DiceMaster program with python 3
Make sure the terminal is open in the directory where the repository was clone and run [***run.py***](https://github.com/lmisea/dicemaster/blob/main/run.py) with Python 3:
```sh
python3 run.py
```
## HOW TO ROLL?
You can now roll any kind of die you want, as many times as you desire.

The standard syntax for rolling is: `[num_dice]d[num_faces]+/-[modifier]`.

Where `[num_dice]` is an integer who specifies how many dice to roll.

And `[num_faces]` is an integer who specifies how many faces each die has.

**For example:**

If you write `2d6`, this will roll **2 dice of 6 faces**.

If you write `100 d 20`, this will roll **100 dice of 20 faces**.

Note that is okay to add a space before and/or after the `d`.

### HOW TO ADD A MODIFIER?
After `[num_faces]` add: `+/-[modifier]`. Where `[modifier]` is an integer.

For a bonus modifier use `+[modifier]` and use `-[modifier]` for a penalty modifier.
This will increase or decrease the total sum of the dice rolled by the `[modifier]` value.

For example:

If you write `1d8+2`, this will roll **1 die of 8 adding a modifier of +2**.

If you write `8d12 - 5`, this will roll **8 dice of 12 faces adding a modifier of -5**.

Note that it is okay to add a space before and/or after the '+' or '-'.

## LICENSE
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
[GNU General Public License](/license) for more details.
