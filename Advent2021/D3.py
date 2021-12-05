file3 = open('D3_input.txt', 'r')
lines = file3.readlines()
gamma = ''
epsilon = ''
for p in range(0, 12):
    zeros = 0
    ones = 0
    for line in lines:
        if line[p] == '0':
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gamma = gamma + '0'
    else:
        gamma = gamma + '1'
print(f'gamma_string={gamma}')
inverse_dict = {'0':'1', '1':'0'}
for b in gamma:
    epsilon += inverse_dict[b]
print(f'epsilon_string = {epsilon}')
gamma = int(gamma, 2)
print(f'gamma_int={gamma}')
epsilon = int(epsilon, 2)
print(f'epsilon_int = {epsilon}')
print(f'PowerConsumption = {gamma * epsilon}')