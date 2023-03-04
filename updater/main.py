from rich.console import Console
from rich.markdown import Markdown
from os import system
from os.path import isfile

console = Console()
h1 = Markdown('''
# Welcome to arnix-updater

> Select options:-
- [c] upgrade core packages
- [r] upgrade aur packages
- [a] upgrade all
- [e] exit
''')

commands = ["sudo pacman -Sy" , "sudo pacman -Syu" , "yay -Syu"]

def check_tools():
    pacman_path = "/usr/bin/pacman"
    yay_path = "/usr/bin/yay"
    if isfile(pacman_path) and isfile(yay_path) == True:
        console.print("found [blue]/usr/bin/pacman[/blue]")
        console.print("found [blue]/usr/bin/yay[/blue]")
        console.print("[green]sucess:-[/green] dependency check passed")
        system("clear")
        pass
    else:
        console.print("[red]error:-[/red] dependency check failed")
        exit(1)

class UpgradeOperations():
    def upgrade_core():
        console.log(f"[cyan]info:-[/cyan] executing {commands[0]}")
        prsc1 = system(commands[0])
        if prsc1 != 0:
            console.log(f"[yellow]warning:-[/yellow] {commands[0]} was unsuccesful so do you want to try again?")
            yn = str(input("enter y/n:- "))
            if yn == "y":
                UpgradeOperations.upgrade_core()
            else:
                console.log(f"[red]error:-[/red] {commands[0]} exited with {prsc1}")
        else:
            console.log("[green]sucess:-[/green] sucess repo synced succesfully")
            console.log(f"[cyan]info:-[/cyan] now executing {commands[1]}")
            prcs2 = system(commands[1])
            if prsc1 != 0:
                console.log(f"[yellow]warning:-[/yellow] {commands[1]} was unsuccesful so do you want to try again?")
                yn = str(input("enter y/n:- "))
                if yn == "y":
                    UpgradeOperations.upgrade_core()
                else:
                    console.log(f"[red]error:-[/red] {commands[1]} exited with {prcs2}")
            else:
                console.log("[green]sucess:-[/green] upgrade passed")

    def aur_upgrade():
        console.log(f"[cyan]info:-[/cyan] executing {commands[2]}")
        prsc1 = system(commands[2])
        if prsc1 != 0:
            console.log(f"[yellow]warning:-[/yellow] {commands[2]} was unsuccesful so do you want to try again?")
            yn = str(input("enter y/n:- "))
            if yn == "y":
                UpgradeOperations.aur_upgrade()
            else:
                console.log(f"[red]error:-[/red] {commands[2]} exited with {prsc1}")
        else:
            console.log(f"[green]sucess:-[/green] AUR packages updated")


if __name__ == "__main__":
    check_tools()
    console.print(h1)
    choice = str(input("enter your option:- "))
    if choice == "c":
        UpgradeOperations.upgrade_core()
    elif choice == "r":
        UpgradeOperations.aur_upgrade()
    elif choice == "a":
        UpgradeOperations.upgrade_core()
        UpgradeOperations.aur_upgrade()
    elif choice == "e":
        console.log("[red]exit detected[/red]")
        exit(0)
