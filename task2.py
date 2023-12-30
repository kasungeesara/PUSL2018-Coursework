import itertools
import random
def count_ways_to_make_sum(target_sum, num_dice, num_sides):
    ways_to_make_sum = 0
    total_outcomes = 0
    successful_combinations = []
    # Generate all possible outcomes
    outcomes = itertools.product(range(1, num_sides + 1), repeat=num_dice)
    for outcome in outcomes:
        total_outcomes += 1
        if sum(outcome) == target_sum:
            ways_to_make_sum += 1
            successful_combinations.append(outcome)
    return ways_to_make_sum, total_outcomes, successful_combinations
def simulate_dice_throws(num_simulations, num_dice, target_sum):
    successful_outcomes = 0
    for _ in range(num_simulations):
        dice_results = [random.randint(1, 6) for _ in range(num_dice)]
        if sum(dice_results) == target_sum:
            successful_outcomes += 1
    probability_simulation = successful_outcomes / num_simulations
    return probability_simulation
# Parameters
target_sum = 32
num_dice = 10
num_sides = 6
num_simulations = 500
# Calculate exactly
ways_to_make_sum, total_outcomes, successful_combinations = count_ways_to_make_sum(target_sum, num_dice, num_sides)
exact_probability = ways_to_make_sum / total_outcomes
# Simulate and calculate probability
simulated_probability = simulate_dice_throws(num_simulations, num_dice, target_sum)
# Output
print(f"Number of ways to make {target_sum} with {num_dice} dice: {ways_to_make_sum}")
print(f"Total possible outcomes with {num_dice} dice: {total_outcomes}")
print(f"Exact probability: {exact_probability}")
print(f"\nSimulated probability (500 throws): {simulated_probability:.6f}")
# Output all possible ways:
print("\nAll possible ways :")
for combination in successful_combinations:
    print(combination)
