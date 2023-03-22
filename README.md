# IMDb Top 250 Movies Analysis

This project is my Code Louisville: Data Analyst Pathway project, which focuses on analyzing and visualizing data from the top 250 movies on IMDb. As a movie enthusiast, my love for movies inspired me to pick this dataset and explore the world of cinema in a more analytical way. The data is loaded from a local CSV file, and the analysis is performed using Pandas, Matplotlib, and Seaborn. The final result is an interactive visualization using the Tkinter GUI library.

## Project Requirements

1. Read in data from a local CSV file.
   - The data is loaded from a local CSV file named "moviesData.csv" using the `pd.read_csv()` function.
2. Use built-in Pandas or NumPy functions to clean and preprocess the dataset.
   - 'Not Available' values in the box_office column are replaced with NaN and the column is converted to integers.
3. Write custom functions to operate on the data.
   - Custom functions are included for:
     - Getting the top genres by the number of movies.
     - Plotting the number of movies by genre.
     - Getting the top directors by box office revenue.
     - Plotting the top directors by box office revenue.
     - Searching for movies by year.
4. Use a GUI library like Tkinter to make an interactive visualization.
   - A Tkinter GUI application is created with multiple tabs for different visualizations and functionalities.
5. Provide a README explaining the project.
   - This README file explains the project, its features, and how to set it up and use it.

## Features

- Loads data from a local CSV file "moviesData.csv".
- Replaces 'Not Available' values in the box_office column with NaN and converts the column to integers.
- Sorts the DataFrame by box_office in descending order.
- Includes custom functions for:
  - Getting the top genres by the number of movies.
  - Plotting the number of movies by genre.
  - Getting the top directors by box office revenue.
  - Plotting the top directors by box office revenue.
  - Searching for movies by year.
- Creates a Tkinter GUI application with multiple tabs for different visualizations and functionalities.

## Installation

1. Clone the repository from GitHub:
  ```
git clone https://github.com/KainMason/IMDB-Top-250-movies-Analyse.git
  ```
2. This project uses a Conda environment with Python 3.9.13.
- Install Anaconda or Miniconda if you haven't already.
- Install the required packages:
  ```
  conda install pandas matplotlib seaborn tk
  ```

## Usage

1. Navigate to the project directory:
```
cd IMDB-Top-250-movies-Analyse
```
2. Run the script using:
```
python main.py
```
3. Explore the different visualizations and functionalities in the GUI application.

## License

This project is open-source and available for use and modification under the terms of the MIT License.

