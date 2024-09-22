from TestsGenerator import generator1, generator2, generator3
from Problema3 import first_solution, second_solution, third_solution
from colorama import Fore

algorithm = {"1" : first_solution, "2" : second_solution, "3" : third_solution}
generator = {"1" : generator1, "2" : generator2, "3" : generator3}

print("Solutions:")
print("1: First Aproximation", "2: Second Aproximation", "3: Third Aproximation")
algo1 = input("Choose the first algorithm \n")
algo2 = input("Choose the second algorithm \n")

gen = input("Choose the generator algorithm \n")

test_cases_number = int(input("How many test cases you want to generate? \n"))

test_cases = generator[gen](test_cases_number)

if algo1 == algo2:
    for case in test_cases:
        print(algorithm[algo1](case[0], case[1], case[2]))

else:
    wrong_cases = 0

    for case in test_cases:
        answer1 = algorithm[algo1](case[0], case[1], case[2])
        answer2 = algorithm[algo2](case[0], case[1], case[2])
        match = answer1 == answer2
        print(f"P: {case[0]}, R: {case[1]}, k: {case[2]}")

        if match:
            print(Fore.GREEN, f"answer1:{answer1}, answer2:{answer2}, good")
            print(Fore.RESET, "\n")

        else:
            wrong_cases += 1
            print(Fore.RED, f"answer1:{answer1}, answer2:{answer2}, bad")
            print(Fore.RESET, "\n")

    print(f"Number of wrong cases: {wrong_cases} \n")
