# class Car:
#     color = "red"
#     transmisson = "manual"
#     gear_position = 'N'

#     def __init__(self, color, transmission, gear_position):
#         self.color = color
#         self.transmission = transmission
#         self.gear_position = gear_position
#         print("Car created")

#     def drive(self):
#         self.gear_position = 'D'
#         print("Car is driving")

#     def reverse(self):
#         self.gear_position = 'N'
#         print("Car is reversing")

#     def change_gears(self, gear_position):
#         self.gear_position = gear_position
#         print("Gear changed to " + self.gear_position)

#     def change_color(self, color):
#         self.color = color
#         print("Color changed to " + self.color)

#     def change_transmission(self, transmission):
#         self.transmission = transmission
#         print("Transmission changed to " + self.transmission)

#     def __str__(self):
#         return "Color: " + self.color + " Transmission: " + self.transmission + " Gear Position: " + self.gear_position + " "

# car1 = Car("red", "manual", "N")        
# car1.change_gears('D-1')
# car1.change_color("blue")
# car1.change_transmission("automatic")

# import random
# import time

# computerwins = 0
# playerwins = 0
# ties = 0
# end = 0

# while True:

#     choices = ["rock",
#                "paper",
#                "scissors"]

#     userChoice = input("Choose rock, paper, or scissors: ")

#     computerChoice = (random.choice(choices))
#     print(computerChoice)

#     if userChoice == computerChoice:
#         time.sleep(0.5)
#         print("Tie!\n")
#         ties += 1
#         end += 1

#     elif userChoice == "rock":
#         if computerChoice == "paper":
#             time.sleep(0.5)
#             print("Computer Win!\n")
#             computerwins +=1
#             end += 1

#         else:
#             time.sleep(0.5)
#             print("Player win!\n")
#             playerwins += 1
#             end += 1

#     elif userChoice == "paper":
#         if computerChoice == "rock":
#             time.sleep(0.5)
#             print("Player win!\n")
#             playerwins += 1
#             end += 1

#         else:
#             time.sleep(0.5)
#             print("Computer win!\n")
#             computerwins += 1
#             end += 1

#     elif userChoice == "scissors":
#         if computerChoice == "rock":
#             time.sleep(0.5)
#             print("Computer win!\n")
#             computerwins += 1
#             end += 1

#         else:
#             time.sleep(0.5)
#             print("Player win!\n")
#             playerwins += 1
#             end += 1

#     elif userChoice == "end":
#             choices.append("end")
#             print("\nGreat game!\n")
#             print("Total score for computer: ", computerwins, "wins!")
#             print("Total score for player: ", playerwins, "wins!")
#             print("Total ties: ", ties, "ties!")
#             time.sleep(2)
#             break



class Car:
    def fuel(self):
        print("Gass")

class Honda(Car):
   pass

class Toyota(Car):
    def fuel(self):
        print("Hybrid")

class Tesla(Car):
    def fuel(self):
        print("Electric")

def get_fuel(car):
    car.fuel()

get_fuel(Honda())
get_fuel(Tesla())