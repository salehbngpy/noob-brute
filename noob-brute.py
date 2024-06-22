import pyautogui
import time
from rich import print as pr

SLEEP_TIME = 1

pr("""[magenta]

███╗░░██╗░█████╗░░█████╗░██████╗░  ██████╗░██████╗░██╗░░░██╗████████╗███████╗
████╗░██║██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝
██╔██╗██║██║░░██║██║░░██║██████╦╝  ██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░
██║╚████║██║░░██║██║░░██║██╔══██╗  ██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░
██║░╚███║╚█████╔╝╚█████╔╝██████╦╝  ██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗
╚═╝░░╚══╝░╚════╝░░╚════╝░╚═════╝░  ╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝[/magenta]""")
print("\n")
pr("[red]""Made by : salehBNG\nTelegram : @SalehBNG0 \n -----------------------""[/red]")
print("\n")
passwords = open(input("Enter your password list (File name): "))

def write_and_clear(password):
    pyautogui.typewrite(password)
    time.sleep(SLEEP_TIME)
    pyautogui.press("backspace", presses=len(password))
    time.sleep(SLEEP_TIME)

def write_passwords_and_enter():
    for password in passwords:
    	write_and_clear(password)
    	pyautogui.press("enter")
def main():
    write_passwords_and_enter()
    pr("[green]""Noob Brute Ran Succesfully""[/green]")

# Used to prevent running from imports
if __name__ == "__main__":
    main()
