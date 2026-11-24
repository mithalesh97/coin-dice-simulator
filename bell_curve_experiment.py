
import random

import numpy as np
import matplotlib.pyplot as plt

# Configuration
total_rolls = 10000
dice_counts = [1, 2, 3, 5, 10]

# Create graph area
plt.figure(figsize=(12, 7))

# Run experiments for different numbers of dice
for number_of_dice in dice_counts:

    # Generate random dice rolls
    dice_rolls = np.random.randint(
        1,
        7,
        size=(total_rolls, number_of_dice)
    )

    # Calculate the sum of each experiment
    results = np.sum(dice_rolls, axis=1)

    # Calculate statistics
    average = np.mean(results)
    standard_deviation = np.std(results)

    print(f"\n--- {number_of_dice} Dice ---")
    print("Average:", round(average, 2))
    print("Standard Deviation:", round(standard_deviation, 2))
    print("Minimum:", np.min(results))
    print("Maximum:", np.max(results))

    # Plot histogram
    plt.hist(
        results,
        bins=np.arange(
            number_of_dice - 0.5,
            6 * number_of_dice + 1.5,
            1
        ),
        alpha=0.45,
        label=f"{number_of_dice} Dice"
    )

# Graph formatting
plt.title("Bell Curve Experiment: Multiple Dice")
plt.xlabel("Sum of Dice")
plt.ylabel("Frequency")
plt.legend()
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
