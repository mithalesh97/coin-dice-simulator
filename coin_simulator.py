import random
import matplotlib.pyplot as plt

total_flips = 10000

heads = 0
tails = 0

for i in range(total_flips):
    result = random.choice(['Heads', 'Tails'])
    if result == 'Heads':
        heads += 1
    else:
        tails += 1

heads_percentage = (heads / total_flips) * 100
tails_percentage = (tails / total_flips) * 100


# print(f"Total Flips: {total_flips}")
# print(f"Number of Heads: {heads}")
# print(f"Number of Tails: {tails}")
# print(f"Percentage of Heads: {heads_percentage:.2f}%")
# print(f"Percentage of Tails: {tails_percentage:.2f}%")

# Plotting the results
outcomes = ['Heads', 'Tails']
counts = [heads, tails]

plt.bar(outcomes,counts)

plt.title('Coin Flip Simulation Results')
plt.xlabel('Outcome')
plt.ylabel('Frequency')

plt.show()
