import random 

def generator1(test_cases_number):
    cases = []

    for _ in range(test_cases_number):
        n = random.randint(2, 4)
        P, R = [], []
        T = 10
        k = random.randint(1, 10)

        for i in range(n):
            if T <= 0:
                r1 = 0
            else:
                r1 = random.randint(0, T)

            P.append(r1)
            T-= r1

        for i in range(n):
            if T <= 0:
                r1 = 0
            else:
                r1 = random.randint(0, T)

            R.append(r1)
            T -= r1

        cases.append((P, R, k))

    return cases


def generator2(test_cases_number):
    test_cases = []

    for _ in range(test_cases_number):
        n = random.randint(1, 7)
        P, R= [],[]
        T = 0

        for i in range(n):
            pi = 0    
            ri = 0

            while pi + ri == 0:
                pi = random.randint(0, 20)
                ri = random.randint(0, 20)
            
            T += pi + ri
            P.append(pi)
            R.append(ri)

        k = random.randint(1, T)
        
        test_cases.append((P, R, k))

    return test_cases
    

def generator3(test_cases_number):
    test_cases = []

    for _ in range(test_cases_number):
        n = random.randint(1, 50)
        P, R = [],[]
        T = 0

        for _ in range(n):
            pi = 0    
            ri = 0

            while pi + ri == 0:
                pi = random.randint(0, 100)
                ri = random.randint(0, 100)
            
            T += pi + ri
            P.append(pi)
            R.append(ri)

        k = random.randint(1, T)
        
        test_cases.append((P, R, k))

    return test_cases
