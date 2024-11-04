# CS50: WEB CTF Final_Project

This projected was a full-stack web application designed as a educational hacking game, the format is commonly known as Capture The Flag (CTF). The goal is to discover "flags" in the form of strings on the systems to beat the 3 stages of the game. The web application was designed to be deliberately vulnerable to 3 common exploits, specifically bad access control, local-file inclusion and remote code execution.

The web application was built using Flask, SQLite (via SQLAlchemy) and Bootstrap. To play the game, the files must be downloaded on a virtual machine by cloning the repository. Once the repo is cloned, one can install the depedencies via the `python -m pip install -r requirements.txt` command.
