import random 

def generator1(test_cases_number):
    cases = []

    for i in range(test_cases_number):
        n = random.randint(2, 4)
        prueba1 = []
        prueba2 = []
        students_available = 8
        k = random.randint(1, 8)

        for i in range(n):
            if students_available <= 0:
                r1 = 0
            else:
                r1 = random.randint(0, students_available)

            prueba1.append(r1)
            students_available -= r1

        for i in range(n):
            if students_available <= 0:
                r1 = 0
            else:
                r1 = random.randint(0, students_available)

            prueba2.append(r1)
            students_available -= r1

        cases.append((prueba1, prueba2, k))

    return cases


def generator2(test_cases_number):
    test_cases = []

    for i in range(test_cases_number):
        n = random.randint(1, 7)
        prueba1 = []
        prueba2 = []
        total = 0

        for i in range(n):
            mi = 0    
            fi = 0

            while mi + fi == 0:
                mi = random.randint(0, 20)
                fi = random.randint(0, 20)
            
            total += mi + fi
            prueba1.append(mi)
            prueba2.append(fi)

        k = random.randint(1, 10)
        
        test_cases.append((prueba1, prueba2, k))

    return test_cases
    

def generator3(test_cases_number):
    test_cases = []

    for i in range(test_cases_number):
        n = random.randint(1, 50)
        prueba1 = []
        prueba2 = []
        total = 0

        for i in range(n):
            mi = 0    
            fi = 0

            while mi + fi == 0:
                mi = random.randint(0, 100)
                fi = random.randint(0, 100)
            
            total += mi + fi
            prueba1.append(mi)
            prueba2.append(fi)

        k = random.randint(1, total)
        
        test_cases.append((prueba1, prueba2, k))

    return test_cases