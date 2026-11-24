import random
import matplotlib.pyplot as plt


one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

total_rolls = 10000

#roll the dice 
for i in range(total_rolls):
    result = random.randint(1, 6)
    if result == 1:
        one += 1
    elif result == 2:
        two += 1
    elif result == 3:
        three += 1
    elif result == 4:
        four += 1
    elif result == 5:
        five += 1
    else:
        six += 1

# print(f"Total Rolls: {total_rolls}")
# print(f"Number of 1s: {one}")
# print(f"Number of 2s: {two}")
# print(f"Number of 3s: {three}")
# print(f"Number of 4s: {four}")
# print(f"Number of 5s: {five}")
# print(f"Number of 6s: {six}")

# print("1:", (one / total_rolls) * 100, "%")
# print("2:", (two / total_rolls) * 100, "%")
# print("3:", (three / total_rolls) * 100, "%")
# print("4:", (four / total_rolls) * 100, "%")
# print("5:", (five / total_rolls) * 100, "%")
# print("6:", (six / total_rolls) * 100, "%")

outcomes = ["1", "2", "3", "4", "5", "6"]

counts = [one, two, three, four, five, six]

plt.bar(outcomes, counts)

plt.title("Dice Roll Distribution")
plt.xlabel("Dice Outcome")
plt.ylabel("Frequency")

plt.show()