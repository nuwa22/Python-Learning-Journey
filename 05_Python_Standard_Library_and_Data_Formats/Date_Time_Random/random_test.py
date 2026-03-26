import random

lucky_number = random.randint(1, 10)
print("Lucky number:", lucky_number)

colors = ["red", "green", "blue", "yellow", "orange"]
random_color = random.choice(colors)
print("Random color:", random_color)

cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
random.shuffle(cards)
print("Random card:", cards)