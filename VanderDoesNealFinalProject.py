"""
Title: Final Project: Game Advisor
Author: Neal Vander Does
Date: 3/8/2024
Class: 01N-Spring 2024-Intro. to Software Development
Important Information: import os is very important to access the folders with PNGs in them,
imports PhotoImage from tkinter, imports EasyFrame from breezypythongui, imports random to help choose a random game.
Description: Recommends top games based on a category(s) picked by the user.

input:

Category of game: Action, Adventure, Strategy, Survival

process:
Click buttons to show a game from that category
Access games in entered category
Print 1 randomized game picture


Shuffle button: Repeats process above.
Exit button: Terminates program.

output:
Two pictures of games according to category entered
"""
# Imports
import os
import random
from tkinter import PhotoImage

from breezypythongui import EasyFrame


class game_advisor(EasyFrame):
    """Creates the GUI and the buttons in it"""

    def __init__(self):
        """
        Sets up the GUI & its buttons & labels.
        Creates textfield for entering game category.
        Creates buttons for Search, Exit, Shuffle Games.
        Puts program logo at the top middle.
        """
        # Both variables access the current working directory to load an image.
        logo_path = os.getcwd() + "/GamePNGs/logo.png"
        blank_path = os.getcwd() + "/GamePNGs/blank.png"

        # Creates the GUI
        EasyFrame.__init__(self, width=800, height=600, title="Game Advisor", background="#0E1543")

        text = "Choose a category below, it will display a random game from that category. " # Text for directions label below

        # Buttons
        self.addButton(text="Action", row=1, column=0, command=self.Action)
        self.addButton(text="Adventure", row=1, column=1, command=self.Adventure)
        self.addButton(text="Strategy", row=1, column=2, command=self.Strategy)
        self.addButton(text="Survival", row=1, column=3, command=self.Survival)
        self.addButton(text="Exit", row=6, column=4, command=self.quit)
        self.addButton(text="Games Information", row=6, column=0, command=self.games_info)

        # Label showing directions for the program
        self.addLabel(text=text, row=1, column=1, sticky="NE", background="#0E1543", foreground="white",
                      font=("", 11, "bold"))

        # Puts the Game Advisor logo in the gui
        logo = self.addLabel(text="", row=0, column=1, sticky="N", background="#0E1543")
        self.logo = PhotoImage(file=(logo_path))
        logo["image"] = self.logo

        # Loads a blank image showing where a game picture will be when a button is clicked
        blank = self.addLabel(text="", row=4, column=1, sticky="NSEW", background="#0E1543")
        self.blank = PhotoImage(file=(blank_path))
        blank["image"] = self.blank


    def Action(self):
        """
        Uses a list and random index to complete the file path,
        then accesses the current working directory to show the picture of a random game in the SurvivalPNGs folder.
        Used by the "Action" button
        """

        # List of all Action game images, used to obtain the file path, then show its image.
        self.action_list = ["Counter-Strike 2.png", "Garry's Mod.png", "Grand Theft Auto V.png", "Left 4 Dead 2.png", "Portal 2.png",
                            "Tom Clancy's Rainbow Six Siege.png", "Red Dead Redemption 2.png", "Warframe.png"]

        # Chooses a random index from the self.action_list and uses it for the file path
        self.game = self.action_list[random.randint(0, 7)]
        action_path = os.getcwd() + "/GamePNGs/ActionPNGs/" + self.game

        # These three lines of code are used to show the game pictures.
        # It creates a blank label, then puts an image there using the final file path
        game_logo = self.addLabel(text="", row=4, column=1, sticky="NSEW", background="#0E1543")
        self.game_logo = PhotoImage(file=(action_path))
        game_logo["image"] = self.game_logo


    def Adventure(self):
        """
        Uses a list and random index to complete the file path,
        then accesses the current working directory to show the picture of a random game in the SurvivalPNGs folder.
        Used by the "Adventure" button
        """

        # List of all Adventure game images, used to obtain the file path, then show its image.
        self.adventure_list = ["Ark Survival Evolved.png", "Baldur's Gate 3.png", "The Forest.png", "Sea of Thieves.png", "Terraria.png",
                               "Tomb Raider.png", "Unturned.png", "The Witcher 3 Wild Hunt.png"]

        # Chooses a random index from the self.adventure_list and uses it for the file path
        self.game = self.adventure_list[random.randint(0, 7)]
        adventure_path = os.getcwd() + "/GamePNGs/AdventurePNGs/" + self.game

        # These three lines of code are used to show the game pictures.
        # It creates a blank label, then puts an image there using the final file path
        game_logo = self.addLabel(text="", row=4, column=1, sticky="NSEW", background="#0E1543")
        self.game_logo = PhotoImage(file=(adventure_path))
        game_logo["image"] = self.game_logo


    def Strategy(self):
        """
        Uses a list and random index to complete the file path,
        then accesses the current working directory to show the picture of a random game in the SurvivalPNGs folder.
        Used by the "Strategy" button
        """

        # List of all Strategy game images, used to obtain the file path, then show its image.
        self.strategy_list = ["Age of Empires II Definitive Edition.png", "Bloons TD 6.png", "Dota 2.png", "Hearts of Iron IV.png",
                              "Divinity Original Sin 2 Definitive Edition.png", "Rimworld.png",
                              "Sid Meier's Civilization VI.png", "Tabletop Simulator.png"]

        # Chooses a random index from the self.strategy_list and uses it for the file path
        self.game = self.strategy_list[random.randint(0, 7)]
        strategy_path = os.getcwd() + "/GamePNGs/StrategyPNGs/" + self.game

        # These three lines of code are used to show the game pictures.
        # It creates a blank label, then puts an image there using the final file path
        game_logo = self.addLabel(text="", row=4, column=1, sticky="NSEW", background="#0E1543")
        self.game_logo = PhotoImage(file=(strategy_path))
        game_logo["image"] = self.game_logo


    def Survival(self):
        """
        Uses a list and random index to complete the file path,
        then accesses the current working directory to show the picture of a random game in the SurvivalPNGs folder.
        Used by the "Survival" button
        """

        # List of all Survival game images, used to obtain the file path, then show its image.
        self.survival_list = ["7 Days to Die.png", "Among Us.png", "Don't Starve Together.png", "Palworld.png",
                              "Raft.png", "Rust.png", "Subnautica.png", "Valheim.png"]

        # Chooses a random index from the self.survival_list and uses it for the file path
        self.game = self.survival_list[random.randint(0, 7)]
        survival_path = os.getcwd() + "/GamePNGs/SurvivalPNGs/" + self.game

        # These three lines of code are used to show the game pictures.
        # It creates a blank label, then puts an image there using the final file path
        game_logo = self.addLabel(text="", row=4, column=1, sticky="NSEW", background="#0E1543")
        self.game_logo = PhotoImage(file=(survival_path))
        game_logo["image"] = self.game_logo


    def games_info(self):
        """Creates a message box containing name and price of all games using a text file"""
        file = os.getcwd() + "/GamePNGs/GameInfo" # Accesses the file path
        with open(file, "r") as file: # Opens the file and reads it below
            file_contents = file.read()
        self.messageBox(title="Games Information", message=file_contents, width=50, height=40) # Creates the messagebox


    def quit(self):
        """Simple function to end the program. Used by the Exit button"""
        exit()


def main():
    """main function used to start the program"""
    game_advisor().mainloop()


if __name__ == "__main__":  # Starts the main function
    main()


