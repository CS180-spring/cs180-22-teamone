import json
import os
from Functions import *

users = load_users()

def main():
    while True:
        displayMenu(users)
        

if __name__ == '__main__':
    main()
