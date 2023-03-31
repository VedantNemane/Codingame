import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    res = ""
    
    if (light_y > initial_ty):
        res += "S"
        initial_ty += 1
    if (light_y < initial_ty):
        res += "N"
        initial_ty -= 1
    if (light_x > initial_tx):
        res += "E"
        initial_tx += 1
    if (light_x < initial_tx):
        res += "W"
        initial_tx -= 1

    print(res)
{\rtf1}