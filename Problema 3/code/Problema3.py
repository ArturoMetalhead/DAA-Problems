from itertools import combinations, permutations
class Student:
    def __init__(self, group, test) -> None:
        self.group = group
        self.test = test

#region First Solution
def first_solution(P, R ,k):
    T = []
    # Join P and R in T
    for i in range(len(P)):
        for _ in range(P[i]):
            T.append(Student(i, "P"))
    
    for i in range(len(R)):
        for _ in range(R[i]):
            T.append(Student(i, "R"))
    
    # Compute all possible permutations
    all_perms = list(permutations(T))
    max_count = 0

    for perm in all_perms:
        actual_count = 0

        # select subgroups size k 
        for i in range(len(perm) // k ):
            list_possible_sets = perm[i*k : (i*k + k)]

            coincident_group = True
            coincident_test = True

            # verify if it satisfies conditions
            for j in range(len(list_possible_sets) - 1):
                if list_possible_sets[j].group != list_possible_sets[j+1].group:
                    coincident_group = False
                    break
                
            for j in range(len(list_possible_sets) - 1):
                if list_possible_sets[j].test != list_possible_sets[j+1].test:
                    coincident_test = False
                    break
                
            if coincident_group or coincident_test:
                actual_count+=1
        
        # take the maximum value til moment
        max_count = max(max_count, actual_count)
                
    return max_count

#endregion

# region Second Solution
def backtrack(cols, index, est_p, est_s, cols_sets, k, P, R):
    total_sets = 0  # initiates total_sets within the function

    if index == len(cols):
        sets = est_p // k + est_s // k + cols_sets
        return sets  # The total number of groups formed returns

    else:
        for j in range(k + 1):
            if j <= P[cols[index]] and k - j <= R[cols[index]]:
                # Recursively call backtrack and sum the results
                total_sets = max(total_sets, backtrack(cols, index + 1, est_p - j, est_s - k + j, cols_sets + 1, k, P, R))
    
    return total_sets  # The maximum number of groups formed returns

def second_solution(P, R, k):
    valid_groups = []
    total_est_p = 0
    total_est_s = 0

    for i in range(len(P)):
        # Verify if it's possible to form a new set
        if P[i] + R[i] >= k: 
            valid_groups.append(i)

        # Total of students for test P and test R
        total_est_p += P[i] 
        total_est_s += R[i]

    if len(valid_groups) == 0: 
        return total_est_p // k + total_est_s // k

    cols_comb = []  # Combinations for columns

    for i in range(len(P) + 1):
        comb = combinations(valid_groups, i)  # Generate all combinations size i
        cols_comb.extend(comb)

    total_sets = 0 

    for cols_group in cols_comb:
        temp_est_p = total_est_p
        temp_est_s = total_est_s

        # Call backtrack and accumulate the result in total_sets
        total_sets = max(total_sets, backtrack(cols_group, 0, temp_est_p, temp_est_s, 0, k, P, R))

    return total_sets
#endregion

#region Third_solution
def third_solution(P,R, k):
    all_est_p = 0
    all_est_r = 0

    for est in P:
        all_est_p += est
    for est in R:
        all_est_r += est

    T = all_est_p + all_est_r
    result = T // k
    rest_p = all_est_p % k 
    rest_r = all_est_r % k

    if rest_p + rest_r < k: return result

    valid_groups = []

    for i in range(len(P)):
        if P[i] + R[i] >= k and P[i] > 0 and R[i]>0:
            temp = []

            # Create S[0,i] wich contains indexes of possible students in P that may form k-sets
            for i in range(max(k - P[i], 1), min(R[i] + 1, k)):
                temp.append(i)

            valid_groups.append(temp)

    if len(valid_groups) == 0:
        return result - 1
    
    # Create an array for each possible combination, containing the index from which a set of size K can be created
    valid_groups_combs = [[0 for _ in range(k-1)] for _ in range(len(valid_groups))]

    # assign 1 to students of P 
    for i in valid_groups[0]:
        valid_groups_combs[0][i-1] = 1

    # assign 1 if it's possible to create a k-set (if valid_groups_combs[i] == 1 then valid_groups_combs[i+1] == 1 )
    for i in range(1, len(valid_groups_combs)):
        for j in valid_groups[i]:
            valid_groups_combs[i][j-1] = 1
            for r in range(len(valid_groups_combs[i-1])):
                if(valid_groups_combs[i-1][r]):
                    valid_groups_combs[i][r] = 1
                    temp = (r+1+j)%k
                    valid_groups_combs[i][temp-1] = 1
    
    # verifiy the range
    range_tests = range(((all_est_p%k) - (T%k) + k) % k, all_est_p%k+ 1)

    for i in range_tests:
        if valid_groups_combs[len(valid_groups_combs)-1][i-1]:
            return result
                
    return result-1
#endregion

