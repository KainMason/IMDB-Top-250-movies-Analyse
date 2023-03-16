# IMDB-Top-250-movies-Analyse

As a movie enthusiast and data analyst, I always wanted to explore the data behind the movies I love. That's why I decided to create a Python script that uses the IMDB Top 250 movies dataset to visualize movie data in a user-friendly GUI. The GUI has Three tabs that allow me to explore different types of movie data, such as the number of movies by genre, top directors by box office revenue, and movies released in a specific year.
Overall, this project has been a great learning experience for me, as I was able to apply my knowledge of Python and data analysis to a real-world problem that I was passionate about. I hope that others will find this project useful and enjoyable for exploring the fascinating world of movies!

## Code Louisville Project Requirements

1.Read in data from a local csv,
excel file, json, or any other
file type. There are many
ways to do this, but using
Pandas read_ functions is
pretty easy.

* How I'll do it: I will read csv file " moviesData.csv" and use it for the rest of my project.

<https://github.com/KainMason/IMDB-Top-250-movies-Analyse/blob/988eb2dd153dc7109a68653ae6347011eae6a661/MovieAnaylize.py#L8>

2.Use built-in pandas or numpy
functions to do things like
remove 0’s and null values
where they don’t belong in
your dataset.

* How I'll do it:  Replace 'Not Available' values in box_office column with NaN when using the data to chart the top movies by box office sales
<https://github.com/KainMason/IMDB-Top-250-movies-Analyse/blob/988eb2dd153dc7109a68653ae6347011eae6a661/MovieAnaylize.py#L12>
3.Write custom functions to
operate on your data. You
may discover that you want to
find out something particular
about data that just doesn’t
have a built-in Pandas
function that accomplishes
your goal. Maybe you want
your function to read in a
DataFrame, search the
columns for any mention of
“Cars”, then return the
lowest-priced car in the
column along with the
mileage. This category is very
open to interpretation, so any
function operating on your
data will work.
*How I'll do it:
*Define function to search for movies by year
<https://github.com/KainMason/IMDB-Top-250-movies-Analyse/blob/988eb2dd153dc7109a68653ae6347011eae6a661/MovieAnaylize.py#L70>
*Define function to get top directors by box office revenue
<https://github.com/KainMason/IMDB-Top-250-movies-Analyse/blob/988eb2dd153dc7109a68653ae6347011eae6a661/MovieAnaylize.py#L40>
*Define function to get top genres by number of movies
<https://github.com/KainMason/IMDB-Top-250-movies-Analyse/blob/988eb2dd153dc7109a68653ae6347011eae6a661/MovieAnaylize.py#L22>

4.Use a GUI library like tkinter
to make an interactive
visualization. Again, a few
students find this interesting
and it makes for truly unique
projects. This is something
incredible to show off to
employers, but you may not
have time to do it in the class
which is completely okay.

* How I'll do it: Put the entire project in a GUI using tkinter and give charts to visualize Data
<https://github.com/KainMason/IMDB-Top-250-movies-Analyse/blob/988eb2dd153dc7109a68653ae6347011eae6a661/MovieAnaylize.py#L84>
5.If using some format other
than a notebook, make sure
your README explains your
project.

* How I'll do it: Create detailed .README

## Getting Started

1. Clone the repository or download the `moviesData.csv` and `MovieAnaylize.py` files. You can clone the repository by running the following command in your terminal:
git clone <https://github.com/KainMason/IMDB-Top-250-movies-Analyse.git>
Alternatively, you can download the files by clicking the "Code" button on the repository page and selecting "Download ZIP".
2. Install the required libraries: pandas, matplotlib, seaborn, and tkinter. You can install them by running the following command in your terminal:
pip install pandas matplotlib seaborn tkinter

3. Open a terminal or command prompt and navigate to the directory where the `movie_search_gui.py` script is located.
4. Run the `MovieAnaylize.py` script by typing the following command:
python MovieAnaylize.py
Alternatively, you can run the script in an integrated development environment (IDE) such as PyCharm or VSCode by opening the `movie_search_gui.py` file and clicking the "Run" button.

## Features

The GUI has three tabs:

1. **Number of Movies by Genre:** This tab shows a bar chart of the number of movies by genre. The user can explore the most popular genres and see which ones have the most movies. The bar chart is created using the seaborn and matplotlib libraries.

2. **Top Directors by Box Office Revenue:** This tab shows a bar chart of the top directors by box office revenue. The user can explore which directors have been the most successful in terms of box office revenue. The bar chart is created using the matplotlib library.

3. **Search By Year:** This tab has a search box where the user can enter a year and click a button to search for movies released in that year. The search results are displayed in a text box below the search box. The user can explore movies released in a specific year and see their rankings, names, years, and ratings. The search functionality is implemented using the pandas library.

4. **User-friendly interface:** The GUI has a simple and user-friendly interface that allows users to easily explore movie data without having to write any code.

## Data

The dataset used in this script is `moviesData.csv`, which contains information about movies such as the name, genre, rating, and box office revenue. The data was scraped from the IMDB website. The pandas library is used to load and manipulate the data.

## Acknowledgements

This script was inspired by the `moviesData.csv` dataset from [Kaggle](https://www.kaggle.com/PromptCloud
## Disclaimer
After testing in class the program works on windows, not mac
