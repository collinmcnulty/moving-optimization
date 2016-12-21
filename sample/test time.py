import matplotlib.pyplot as plt


def calculate_commute(move_date):
    days_in_new_crib = 183 - move_date
    time = 0
    for i in range(int(days_in_new_crib - days_in_new_crib % 1)):
        weekday = i % 7
        if weekday in [0, 1, 5, 6]:  # Thursday, Fri, Tues, Wed
            time -= 20
        elif weekday in [2, 3]:
            time -= 25
        else:
            time += 25
    return time

value = []
for i in range(183):
    value.append(calculate_commute(i))

plt.plot(range(183),value)

plt.show()
