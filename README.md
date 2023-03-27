# IMDb Top 250 Movies Analysis

This project is my Code Louisville: Data Analyst Pathway project, which focuses on analyzing and visualizing data from the top 250 movies on IMDb. As a movie enthusiast, my love for movies inspired me to pick this dataset and explore the world of cinema in a more analytical way. The data is loaded from a local CSV file, and the analysis is performed using Pandas, Matplotlib, and Seaborn. The final result is an interactive visualization using the Tkinter GUI library.

## Conclusion

Based on the analysis, it seems that box office sales are a major factor in the success of a movie. Anthony Russo emerged as the top director in terms of box office revenue, indicating that his movies are generally more successful at the box office. The analysis of genres showed that the top 10 combinations of genres with the highest box office sales include Drama, which is not surprising given its broad appeal. The analysis of movie title word count showed that 3-word movie titles had the highest box office sales, suggesting that shorter titles may be more appealing to audiences.

The search by year option provides users with the ability to see what year had the most top 250 IMBD films and what they were, allowing them to explore the trends and patterns in the data over time. Overall, these analyses provide insights into the factors that contribute to the success of movies, which could be useful for filmmakers, studios, and other industry professionals.
## Installation

1. Clone the repository from GitHub:
  ```
git clone https://github.com/KainMason/IMDB-Top-250-movies-Analyse.git
  ```
2. Navigate to the project directory:
- Open the project directory
3. This project uses Python 3.10.10 which is recommended to use when running this project.
- Install the required packages: You can run the requirements.txt file or 
  ```
  pip install pandas matplotlib seaborn tk
  ```

## Usage

1. Navigate to the project directory:
- Open the project directory
2. Run the script using:
```
python main.py
```
3. Explore the different visualizations and functionalities in the GUI application.
- Home Tab : lists what the project is supposed to be interpreting
- Genre Tab : shows what the the top 10 listed genres are based on box office sales
-Director Tab : shows the top 10 directors based on box office sales
-Search by Year tab :  Enter the year you want to look at in the designated area and hit enter. the result will display the movies listed in the data set for that year
- Top 10 length of movie title tab : shows you what number of words in a movie title has the highest box office sales.
-Conclusion tab : This tab shows you my conclusion based on what I have found
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
     - Getting the top 10 movies by number of words in title.
     - Plotting the top 10 movies by number of words in title.
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
  - Getting the top 10 movies by number of words in title.
  - Plotting the top 10 movies by number of words in title.
- Creates a Tkinter GUI application with multiple tabs for different visualizations and functionalities.

## License

This project is open-source and available for use and modification under the terms of the MIT License.

