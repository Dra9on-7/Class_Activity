def find_cube_pairs(targ): #mising colon and wrong variable name
    solutions = [];
    max_num = round(targ ** (1/3))  #extra multiply sign

    for a in range(1, max_num + 1): #missing colon & wrong keyword ranges
        for b in range(a, max_num + 1): #missing colon
            if a**3 + b**3 == targ:  #extra multiply sign with a and b, also missing colon
                solutions.append((a, b)); #wrong variable name
    return solutions #wrong variable name

pairs = list(find_cube_pairs(1729)) #removed extra comma and made into list of lists
print("Valid cube pairs for 1729:") #printf instead of print and extra comma removed, updated print statement
for a, b in pairs: #missing colon , wrong variable name pari
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729") #printf instead of print and updated multipler to give correct output and updated print statement
