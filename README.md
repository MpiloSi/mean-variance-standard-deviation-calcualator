# Mean, Variance, and Standard Deviation Calculator

This project is a simple Python-based calculator that computes the mean, variance, and standard deviation of a given set of numbers. It is designed to help users understand basic statistical concepts and perform calculations easily.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Contributing](#contributing)
- [License](#license)

## Features

- Calculate the mean of a list of numbers.
- Compute the variance and standard deviation.
- Handle input validation to ensure correct data types.
- Output results in a structured format.

## Technologies Used

- Python 3.x
- NumPy library for numerical calculations

## Installation

To use this calculator, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

git clone https://github.com/MpiloSi/mean-variance-standard-deviation-calculator.git
cd mean-variance-standard-deviation-calculator


### Step 2: Install Dependencies

You will need to install the NumPy library. You can do this using pip:
pip install numpy


## Usage

To use the calculator, you can run the script directly from the command line or import it into your own Python scripts.

### Example Command Line Usage

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:
   python mean_var_std.py


## Functionality

The `calculate` function takes a list of nine numbers as input and returns a dictionary containing:

- Mean (for rows, columns, and flattened matrix)
- Variance (for rows, columns, and flattened matrix)
- Standard Deviation (for rows, columns, and flattened matrix)
- Maximum value (for rows, columns, and flattened matrix)
- Minimum value (for rows, columns, and flattened matrix)
- Sum (for rows, columns, and flattened matrix)

### Input Validation

The function raises a `ValueError` if the input list does not contain exactly nine numbers.
