
def generateTT_1(n):
    res = []
    def recurse(curr):
        if len(curr) == n:
            res.append(curr)
            return 
        recurse([1] + curr.copy())
        recurse([0] + curr.copy())

    recurse([])
    return res

# another longer way to do it (no closure, non-void):
def generateTT_2(n):
    ttable = []

    if n <= 0:
        return [[]]
    
    t_res = generateTT_2(n-1)
    f_res = generateTT_2(n-1)
    for t_sub in t_res:
        t_sub.append(1)
    for f_sub in f_res:
        f_sub.append(0)
    ttable.extend(t_res)
    ttable.extend(f_res)

    return ttable


def driver():
    n = int(input("please give a whole number as input: "))
    truth_table = generateTT_1(n)
    cardinality_is_correct = len(truth_table) == pow(2, n)
    print("Here is the corresponding truth table:\n" + str(truth_table))
    if cardinality_is_correct:
        print(f"Cardinality is {len(truth_table)}, which is correct")
    else:
        print(f"Cardinality is {len(truth_table)}, which is incorrect")

if __name__ == '__main__':
    driver()
