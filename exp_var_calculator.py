# Random_vars = []
# prob_of_random_vars = []
# expectation = 0
# step = None
# while step == None:
#     sample_space = input('input the sample space:\n ...')
#     try:
#         sample_space = int(sample_space)
#         if sample_space < 0:
#             print('Please Your Sample space should be a positive Whole Number!')
#             continue

#     except (TypeError, NameError) as err:
#         print("Please Enter a positive Whole number!")
#         print(err)
#         continue
#     step = 1
#     for var in range(sample_space):
#         while step == 1:
#             Random_var = input("enter the random variable:\n ...")
#             try:
#                 Random_var = float(Random_var)
#             except (NameError, TypeError, ValueError) as err:
#                 print('\n\nPlease Your Random variable should be a number! ')
#                 continue
#             Random_vars.append(Random_var)
#             prob_of_random_var = input(
#                 f"enter the likelyhood of the {var + 1} random variable:\n ...")
#             try:
#                 prob_of_random_var = float(prob_of_random_var)
#                 if 0 > prob_of_random_var > 1:
#                     print('\n\nPlease Probability CANNOT Negative or greater than 1.0')
#                     continue
#             except (ValueError, TypeError, NameError) as err:
#                 print("\n\n Please Input a decimal or percentage as your Probability!!")
#                 print(err)
#             prob_of_random_vars.append(prob_of_random_var)
#             prod = Random_var * prob_of_random_var
#             expectation = expectation + prod
#             step = 2

# print(expectation)


# vRandom_vars = []
# vprob_of_random_vars = []
# expectation = float(input("enter the expectation here: "))
# variance = 0
# sample_space = int(input('input the sample space: '))
# for var in range(sample_space):
#     vRandom_var = float(input("enter the random variable: "))
#     vRandom_vars.append(vRandom_var**2)
#     vprob_of_random_var = float(
#         input(f"enter the likelyhood of the {var + 1} random variable: "))
#     vprob_of_random_vars.append(vprob_of_random_var**2)
#     vprod = (vRandom_var ** 2) * vprob_of_random_var
#     variance = variance + vprod
# variance = variance - expectation**2
# print(variance)


def expectation(*args):
    exp = 0
    random_vars = []
    prob_of_random_vars = []
    for index, num in enumerate(args):
        if index % 2 == 0:
            random_var = num
            random_var = float(random_var)
            random_vars.append(random_var)
        if index % 2 != 0:
            prob_of_random_var = num
            prob_of_random_var = float(prob_of_random_var)
            prob_of_random_vars.append(prob_of_random_var)
    prod = [random_vars[i]*prob_of_random_vars[i]
            for i in range(len(random_vars))]

    exp = sum(prod)
    return(exp)


def variance(*args, expect=0):
    var = 0
    nums = []
    random_vars = []
    prob_of_random_vars = []
    for index, num in enumerate(args):
        if index % 2 == 0:
            random_var = num
            random_var = float(random_var)
            random_vars.append(random_var)
        if index % 2 != 0:
            prob_of_random_var = num
            prob_of_random_var = float(prob_of_random_var)
            prob_of_random_vars.append(prob_of_random_var)
    prod = [(random_vars[i]**2)*(prob_of_random_vars[i])
            for i in range(len(random_vars))]
    if expect == 0:

        expect = expectation(*args)
    else:
        expect = float(expect)

    var = sum(prod)-(expect**2)
    return(var)


print(expectation(2, 0.1, 5, 0.2, 6, 0.2, 8, 0.5))
print(variance(2, 0.1, 5, 0.2, 6, 0.2, 8, 0.5))
