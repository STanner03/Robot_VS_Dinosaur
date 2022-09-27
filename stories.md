Main Stories
 
    <!-- (5 points): As a developer, I want to make at least 7 commits with good, descriptive messages.  -->
    <!-- (5 points): As a developer, I want to make a class for each of the following: Robot, Dinosaur, Weapon, Battlefield.  -->
    <!-- (10 points): As a developer, I want a Dinosaur to have a name, health, and attack_power.   -->
    <!-- (10 points): As a developer, I want a Robot to have a name, health, and active_weapon.  -->
    <!-- (10 points): As a developer, I want a Weapon to have a name and attack_power.  -->
    <!-- (10 points): As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power.  -->
    <!-- (10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon.  -->
    <!-- (10 points): As a developer, I want the battle to conclude once either the Robot or the Dinosaur has its health points reduced to zero. -->
 
Bonus Stories
    (5 points): As a developer, I want to choose from a List of 3 possible weapons before a robot makes an attack. 
    (5 points): As a developer, I want to create Fleet and Herd classes, allowing for a list of 3 Robots to battle against a list of 3 Dinosaurs.

Checklist

    Run through the Setup Setups and get your project ready to begin work.
    Review the Resources outlined below - be sure to have relevant documentation and references open while you develop!
    Create your project (including setting up your GitHub repository for source control)
    Create all of the classes for the project based off of the UML 
    Starting with the smallest class, write the methods for your classes. 
    Work through the user stories as you write methods, testing each method before moving on!
 
Setup Steps
    1) Create a folder for your project, then create a GitHub repository for the project.
    2) Clone down the repository to your computer and put the invisible .git folder inside your project folder (as well as the .gitignore and README). Make an initial commit.
    3) Create a new file for each class on the UML, as well as a main.py file that will serve as the entry point of your application.
    4) Begin working on the user stories by filling in your classes from smallest to large. Begin with the Weapon class, then move on to the Dinosaur class, then the Robot class. 
    5) Finally, fill out the methods for your battle logic in the Battlefield class. You will only need to import the Dinosaur and Robot classes into the Battlefield class.
    6) You will run the game by creating an object from the Battlefield class inside of main.py and calling the run_game method!
