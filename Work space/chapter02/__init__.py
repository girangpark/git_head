data = list(range(1,101))
def outer_func(data):
    dataset = data
    def tot():
        tot_val = sum(dataset)
        return tot_val
    def avg():
        avg_val = tot_val / len(dataset)
        return avg_val
    return tot, avg

tot, avg = outer_func(data)

tot_val = tot()
print('tot = ', tot_val)
avg_val = avg()
print('avg = ', avg_val)