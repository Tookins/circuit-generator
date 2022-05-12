#TODO
#add in rpe calculation and apply to exercise selection
#add ability to add exercises to the table
#save a log of workout history
#change data format from csv to json
#add support for multiple user profiles
#add support for workout specificity

import sys
import csv
import random


def build_circuit(rounds):
    """generates a list of exercises from some input"""
    exercises = []

    with open('exercises.csv', newline='') as table:
        table_reader = csv.reader(table, delimiter=',')

        for entry in table_reader:
            exercises.append(entry[0])

    return random.sample(exercises, rounds)


def main():
    print("Welcome to the circuit generator, a program that generates workouts")
    print("for circuit training.")

    if (len(sys.argv) == 1 or sys.argv[1]=="custom"):
        rounds = int(input("How many rounds per circuit? "))

        round_time = int(input("How long are the rounds (seconds)? "))

        duration = int(input("How long is the training session (minutes)? "))

        circuit = build_circuit(rounds)

        print("Circuit:")

        print(circuit)

        print("perform each exercise for " + str(round_time) + " seconds, rest " 
        + str(round_time // 3) + " seconds between rounds")

        print("repeat the circuit " + str(int(duration / (4/3*round_time/60*rounds))) + " times")

    elif (sys.argv[1]=="add"):
        
        while("y" == input("add an exercise to the table? (y/n)")):

            with open('exercises.csv', 'a+', newline='') as table:
                table_writer =  csv.writer(table, delimiter = ',')

                print("Add an exercise")

                name = input("Name: ")

                pattern = input("Movement Pattern: ")

                muscles = input("Muscle Group: ")

                equipment = input("Equipment Needed: ")

                table_writer.writerow((name, pattern, muscles, equipment))


if (__name__=="__main__"):
    main()
