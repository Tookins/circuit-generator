#TODO
#add in rpe calculation and apply to exercise selection
#add ability to add exercises to the table
import sys
import os
import pandas as pd
import numpy as np
from numpy.random import default_rng

exercises = pd.read_csv("exercises.csv")
rng = default_rng()

def build_circuit(rounds, round_time, rpe):
    circuit = np.array(exercises['name'].tolist())
    rng.shuffle(circuit)
    return circuit[:rounds]

def main():

    print("Welcome to the circuit generator, a program that generates workouts for circuit training")

    if (len(argv) == 1 or argv[1]=="custom"):
        rounds = int(input("How many rounds per circuit? "))
        round_time = int(input("How long are the rounds (seconds)? "))
        duration = int(input("How long is the training session (minutes)? "))
        rpe = int(input("How hard is the training? "))
        circuit = build_circuit(rounds, round_time, rpe)
        print("Circuit:")
        print(circuit)
        print("perform each exercise for " + str(round_time) + " seconds, rest " + str(round_time / 3) + " seconds between rounds")
        print("repeat the circuit " + str(duration / (4/3*round_time/60*rounds)) + " times")

    elif (arg=="add"):
        repeat = "y"
        while(repeat.lower()=="y"):
            print("Add an exercise")
            name = input("Name: ")
            pattern = input("Movement Pattern: ")
            difficulty = int(input("Difficulty (1-10): "))
            
            repeat = input("Add another exercise?(y/n)") 
if (__name__=="__main__"):
    main()
