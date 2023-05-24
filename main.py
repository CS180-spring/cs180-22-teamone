import json
import os
import shutil

# from Functions import *
from login import *

users = load_users()

def main():
    while True:

        displayMenu(users)

# if __name__ == '__main__':
main()