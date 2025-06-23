import time
import os

def fake_hacking():
    print("Connecting to remote server...")
    time.sleep(1.5)
    print("Bypassing firewall...")
    time.sleep(2)
    print("Access granted!")
    time.sleep(1)

    for i in range(3):
        print(".")
        time.sleep(0.5)

    os.system('cls' if os.name == 'nt' else 'clear')

    hearts_and_love()

def hearts_and_love():
    heart = u"\u2764"
    print("\n" * 3)
    print("     " + heart * 3 + " SURPRISE! " + heart * 3)
    print("\n" * 2)
    print("    love you beyond the words can tell")
    print("\n" * 2)
    print("     " + heart * 9)
    print("\n" * 3)

fake_hacking()
