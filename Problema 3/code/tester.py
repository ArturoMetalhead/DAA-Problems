from TestsGenerator import generator1, generator2, generator3
from Problema3 import first_solution, second_solution, third_solution
from colorama import Fore
import time

algorithm = {"1" : first_solution, "2" : second_solution, "3" : third_solution}
generator = {"1" : generator1, "2" : generator2, "3" : generator3}


print("1: First Aproximation", "2: Second Aproximation", "3: Third Aproximation")
alg1, alg2 = input("Put the 2 algorithm to compare \n").split()

gen = input("Choose the generator algorithm \n")

test_cases_number = int(input("How many test cases you want to generate? \n"))

test_cases = generator[gen](test_cases_number)

if alg1 == alg2:
    for case in test_cases:
        print(f"P: {case[0]}, R: {case[1]}, k: {case[2]}")
        start_time = time.time()
        print(algorithm[alg1](case[0], case[1], case[2]))
        end_time = time.time()
        print(f'time case : {end_time - start_time}')

else:
    wrong_cases = 0

    for case in test_cases:
        start_time1 = time.time()
        answer1 = algorithm[alg1](case[0], case[1], case[2])
        end_time1 = time.time()
        start_time2 = time.time()
        answer2 = algorithm[alg2](case[0], case[1], case[2])
        end_time2 = time.time()
        match = answer1 == answer2
        print(f"P: {case[0]}, R: {case[1]}, k: {case[2]}")

        if match:
            print(Fore.GREEN, f"answer1:{answer1}, answer2:{answer2}, good")
            print(Fore.RESET, "\n")

        else:
            wrong_cases += 1
            print(Fore.RED, f"answer1:{answer1}, answer2:{answer2}, bad")
            print(Fore.RESET, "\n")

        print(f'time case 1: {end_time1 - start_time1}')
        print(f'time case 2: {end_time2 - start_time2}')

    print(f"Number of wrong cases: {wrong_cases} \n")
