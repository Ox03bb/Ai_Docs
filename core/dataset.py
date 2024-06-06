import numpy as np
import pandas as pd

# Define the function
def func(x):
    return 461.97489593439417 * x + 2387308.4765028944

# Define the range for x
x_values = np.arange(8001, 14000)

# Calculate the function values
function_values = func(x_values)

# Apply random errors between 5% and 20%
np.random.seed(0)  # For reproducibility
error_percentages = np.random.uniform(0.05, 0.20, size=function_values.shape)
errors = function_values * error_percentages

# Randomly decide to add or subtract the error
signs = np.random.choice([-1, 1], size=function_values.shape)
function_values_with_error = function_values + signs * errors

# Create a DataFrame
data = {
    'x': x_values,
    'f(x)': function_values,
    'Error Percentage': error_percentages,
    'Error': signs * errors,
    'f(x) with Error': function_values_with_error
}

df = pd.DataFrame(data)

# Export to CSV
output_file = './functio.csv'
df.to_csv(output_file, index=False)
