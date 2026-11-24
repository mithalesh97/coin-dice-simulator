# Coin and Dice Simulator

A Python-based simulation project that explores randomness, probability, and statistical distributions through virtual coin flips and dice rolls.

## Phase 1: Coin Simulator

The coin simulator performs 10,000 virtual coin flips and analyzes the frequency of Heads and Tails.

### Features

- Simulates 10,000 coin flips.
- Randomly generates Heads or Tails.
- Counts the frequency of each outcome.
- Calculates outcome percentages.
- Visualizes results using a Matplotlib bar chart.

### Technologies Used

- Python
- Random module
- Matplotlib

### Installation

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd coin-dice-simulator
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Run the Coin Simulator

```bash
python coin_simulator.py
```

### Mathematical Concepts

- Randomness
- Probability
- Frequency distribution
- Law of Large Numbers

### Project Progress

- [x] Phase 1: Coin Simulator
- [ ] Phase 2: Single Dice Simulator
- [ ] Phase 3: Multiple Dice Simulator
- [ ] Phase 4: Bell Curve Experiment
- [ ] Phase 5: Final Documentation

## Author

Python learning project focused on probability and statistical simulations.

# Coin and Dice Simulator

A Python-based simulation project exploring randomness, probability, and statistical distributions through virtual coin flips and dice rolls.

The project demonstrates how mathematical probability works through practical programming experiments and data visualization.

## Project Phases

### Phase 1: Coin Simulator

Simulates 10,000 virtual coin flips.

**Features**
- Randomly generates Heads or Tails.
- Counts the frequency of each outcome.
- Calculates outcome percentages.
- Visualizes results using a Matplotlib bar chart.
- Demonstrates the Law of Large Numbers.

**File:** `coin_simulator.py`

### Phase 2: Single Dice Simulator

Simulates 10,000 rolls of a six-sided dice.

**Features**
- Generates random numbers from 1 to 6.
- Counts the frequency of each outcome.
- Calculates experimental probabilities.
- Visualizes the distribution using a bar chart.
- Compares experimental and theoretical probabilities.

**File:** `dice_simulator.py`

### Phase 3: Multiple Dice Simulator

Simulates rolling two six-sided dice together 10,000 times.

**Features**
- Rolls two dice in each experiment.
- Calculates the sum of both dice.
- Counts sums from 2 to 12.
- Calculates experimental percentages.
- Visualizes the sum distribution.
- Demonstrates why 7 is the most probable sum.

**File:** `multiple_dice_simulator.py`

### Phase 4: Bell Curve Experiment

Compares the sum distributions of 1, 2, 3, 5, and 10 dice using NumPy.

Each experiment is repeated 10,000 times.

**Features**
- Generates multiple dice rolls using NumPy.
- Calculates the sum of each experiment.
- Calculates mean and standard deviation.
- Finds minimum and maximum observed sums.
- Compares distributions using histograms.
- Demonstrates how sums become increasingly bell-shaped as the number of dice increases.
- Explores the Central Limit Theorem.

**File:** `bell_curve_experiment.py`

## Technologies Used

- Python
- NumPy
- Matplotlib
- Random module

## Project Structure

```text
coin-dice-simulator/
│
├── coin_simulator.py
├── dice_simulator.py
├── multiple_dice_simulator.py
├── bell_curve_experiment.py
│
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd coin-dice-simulator
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

Run each simulator separately:

**Coin Simulator**
```bash
python coin_simulator.py
```

**Single Dice Simulator**
```bash
python dice_simulator.py
```

**Multiple Dice Simulator**
```bash
python multiple_dice_simulator.py
```

**Bell Curve Experiment**
```bash
python bell_curve_experiment.py
```

## Requirements

The project uses the following external libraries:

```text
numpy
matplotlib
```

Python's `random` module is built in and does not require installation.

## Mathematical and Statistical Concepts

- Randomness
- Theoretical probability
- Experimental probability
- Frequency distribution
- Law of Large Numbers
- Mean (Arithmetic Average)
- Standard Deviation
- Probability Distribution
- Central Limit Theorem

## Project Progress

- [x] Phase 1: Coin Simulator
- [x] Phase 2: Single Dice Simulator
- [x] Phase 3: Multiple Dice Simulator
- [x] Phase 4: Bell Curve Experiment
- [ ] Phase 5: Final Documentation and Project Completion

## Learning Objectives

Through this project, I aim to understand how programming can simulate real-world random experiments, how probability distributions form, and how statistical concepts can be explored using Python.

## Author

Python learning project focused on probability, statistics, simulation, and data visualization.