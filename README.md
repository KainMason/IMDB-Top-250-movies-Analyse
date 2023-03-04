# IMDB-Top-250-movies-Analyse

This Python script creates a graphical user interface (GUI) using the tkinter and ttk libraries to search for movies and visualize movie data.

## Getting Started

1. Clone the repository or download the `moviesData.csv` and `MovieAnaylize.py` files. You can clone the repository by running the following command in your terminal:
git clone <https://github.com/KainMason/IMDB-Top-250-movies-Analyse.git>
Alternatively, you can download the files by clicking the "Code" button on the repository page and selecting "Download ZIP".
2. Install the required libraries: pandas, matplotlib, seaborn, and tkinter. You can install them by running the following command in your terminal:

3. Open a terminal or command prompt and navigate to the directory where the `MovieAnaylize.py` script is located.
4. Run the `MovieAnaylize.py` script by typing the following command:
python MovieAnaylize.py
Alternatively, you can run the script in an integrated development environment (IDE) such as PyCharm or VSCode by opening the `movie_search_gui.py` file and clicking the "Run" button.

## Requirements

- Python 3.9.13 or later
- pip install pandas matplotlib seaborn tkinter

## Features

The GUI has four tabs:

1. **Number of Movies by Genre:** This tab shows a bar chart of the number of movies by genre. The user can explore the most popular genres and see which ones have the most movies. The bar chart is created using the seaborn and matplotlib libraries.

2. **Top Directors by Box Office Revenue:** This tab shows a bar chart of the top directors by box office revenue. The user can explore which directors have been the most successful in terms of box office revenue. The bar chart is created using the matplotlib library.

3. **Search By Year:** This tab has a search box where the user can enter a year and click a button to search for movies released in that year. The search results are displayed in a text box below the search box. The user can explore movies released in a specific year and see their rankings, names, years, and ratings. The search functionality is implemented using the pandas library.

4. **Search By Name:** This tab has a search box where the user can enter a movie name and click a button to search for movies that contain that name in their titles. The search results are displayed in a text box below the search box. The user can explore movies that match a specific name and see their rankings, names, years, and ratings. The search functionality is implemented using the pandas library.

5. **Interactive Plots:** All the plots in the GUI are interactive, meaning the user can zoom in/out and pan the plot to explore the data in detail. The plots are implemented using the matplotlib library and the FigureCanvasTkAgg class.

6. **User-friendly interface:** The GUI has a simple and user-friendly interface that allows users to easily explore movie data without having to write any code.

## Data

The dataset used in this script is `moviesData.csv`, which contains information about movies such as the name, genre, rating, and box office revenue. The data was scraped from the IMDB website. The dataset has 5000 records with 28 attributes. The pandas library is used to load and manipulate the data.

## Acknowledgements

This script was inspired by a tutorial on [Real Python](https://realpython.com/python-gui-tkinter/) and uses the `moviesData.csv` dataset from [Kaggle](https://www.kaggle.com/PromptCloud
