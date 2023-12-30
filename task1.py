import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import statistics
# Function to check whether a dart hits within the unit circle
def is_hit(P, Q):
    return (P**2 + Q**2) <= 1
# Function to simulate a dart throw and calculate the probability of hitting within the circle
def simulate_dart_throw(num_darts):
    hits = 0
    for _ in range(num_darts):
        P = random.uniform(-1, 1)
        Q = random.uniform(-1, 1)
        if is_hit(P, Q):
            hits += 1
    prob_hit_circle = hits / num_darts
    return prob_hit_circle
# Accepting user input for both questions
n_values_first_question = [int(n) for n in input("Enter multiple values of N for the first question separated by commas: ").split(',')]
n_values_second_question = [int(n) for n in input("Enter multiple values of N for the second question separated by commas: ").split(',')]
# Running the dart throw simulation for the first question and recording outputs in Excel
results_first_question = []
for num_darts in n_values_first_question:
    prob_hit_circle = simulate_dart_throw(num_darts)
    estimate_value_pi = 4 * prob_hit_circle
    results_first_question.append({'N': num_darts, 'Pi Estimate': estimate_value_pi, 'True Pi': np.pi})
# Creating a DataFrame for the first question
df_first_question = pd.DataFrame(results_first_question)
# Save the DataFrame to an Excel file for the first question
with pd.ExcelWriter('dart_simulation_results6.xlsx', engine='openpyxl') as writer:
    df_first_question.to_excel(writer, sheet_name='Results_First_Question', index=False)
# Plotting the graph for the first question
plt.figure(figsize=(10, 6))
plt.plot(df_first_question['N'], df_first_question['Pi Estimate'], label='Pi Estimate')
plt.axhline(np.pi, color='red', linestyle='--', label='True Pi')
plt.xlabel('Number of Darts (N)')
plt.ylabel('Estimated Pi Value')
plt.title('Estimation of Pi with Increasing Number of Darts (First Question)')
plt.legend()
plt.grid(True)
plt.savefig('pi_estimation_plot_first_question.png')
plt.show()
# Experiment for the second question (10 times) and record in the same Excel file separately
results_second_question = []
for _ in range(10):
    for num_darts in n_values_second_question:
        prob_hit_circle = simulate_dart_throw(num_darts)
        estimate_value_pi = 4 * prob_hit_circle
        results_second_question.append({'N': num_darts, 'Pi Estimate': estimate_value_pi, 'True Pi': np.pi})
# Creating a DataFrame for the second question
df_second_question = pd.DataFrame(results_second_question)
# Calculate mean and mode for each N in the second question and append to the same Excel file
df_second_question['Mean Pi Estimate'] = df_second_question.groupby('N')['Pi Estimate'].transform('mean')
df_second_question['Mode Pi Estimate'] = df_second_question.groupby('N')['Pi Estimate'].transform(lambda x: x.mode().iloc[0])
with pd.ExcelWriter('dart_simulation_results6.xlsx', engine='openpyxl', mode='a') as writer:
    df_second_question.to_excel(writer, sheet_name='Results_Second_Question_Stats', index=False)
# Displaying information
print("Results have been saved to 'dart_simulation_results6.xlsx'")
