# main.py

import os

def main():
    print("Hello from Python inside Jenkins!")
    print("Listing files in the current directory:")
    for filename in os.listdir('.'):
        print(" -", filename)

if __name__ == "__main__":
    main()
