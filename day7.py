def fuel_cost(numbers, converge_at):
    return sum(abs(n - converge_at) for n in numbers)

def fuel_cost_2(numbers, converge_at):
    if converge_at == 5:
        for n in numbers:
            d = abs(n - converge_at)
            s = sum(range(d + 1)) 
            print(n, converge_at, d, s)
    return sum(sum(range(abs(n - converge_at) + 1)) for n in numbers)

with open('day7.txt') as in_handle:
    numbers = [int(i) for i in in_handle.read().strip().split(",")]
    # numbers = [16,1,2,0,4,2,7,1,2,14]

    cost = {}
    cost_2 = {}

    for i in range(max(numbers) + 1):
        cost[i] = fuel_cost(numbers, converge_at=i)
        cost_2[i] = fuel_cost_2(numbers, converge_at=i)

    print(list(sorted(cost.items(), key=lambda x:(x[1], x[0])))[0])
    print(list(sorted(cost_2.items(), key=lambda x:(x[1], x[0])))[0])