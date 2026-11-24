
import random
import matplotlib.pyplot as plt

total_rolls = 10000

# Initialize counters
counts = {}

for number in range(2, 13):
    counts[number] = 0

# Simulate two dice
for i in range(total_rolls):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    total = dice1 + dice2

    counts[total] += 1

# Display results
print("Two Dice Simulation")
print("Total rolls:", total_rolls)

for number in counts:
    print(f"Sum {number}: {counts[number]}")


# Calculate percentages
print("\nSum Percentages:")

for number in counts:
    percentage = (counts[number] / total_rolls) * 100
    print(f"Sum {number}: {percentage:.2f}%")

# Visualize results
sums = list(counts.keys())
frequencies = list(counts.values())

plt.bar(sums, frequencies)

plt.title("Two Dice Sum Distribution")
plt.xlabel("Sum of Two Dice")
plt.ylabel("Frequency")
plt.xticks(range(2, 13))

plt.show()
