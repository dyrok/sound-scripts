import winsound
import os

print("################################SCRIPT BY NEEL SINGH################################")

file_path = r"specify\the\file\here\must-be.wav"
try:
    n = int(input("No of Times you want to play: "))  # Number of times to play the sound
except NameError and ValueError:
    print("Please enter an Number")
    exit()

try:
    for i in range(n):
        print("Played This Sound:", i+1,"Times")
        winsound.PlaySound(file_path, winsound.SND_LOOP)

except NameError and ValueError:
    print("Please Convert it to wav")
    exit()

print("################################SCRIPT BY NEEL SINGH################################")

os.system("shutdown -h")
