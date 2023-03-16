import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------------------- Data Loading and Preprocessing ----------------------------

def load_and_preprocess_data():
    # Load the data from the CSV file
    df = pd.read_csv('moviesData.csv')

    # Replace 'Not Available' values in box_office column with NaN
    df['box_office'] = df['box_office'].replace('Not Available', pd.NaT)

    # Convert box_office to integer
    df['box_office'] = pd.to_numeric(df['box_office'], errors='coerce').astype('Int64')

    # Sort the dataframe by box_office in descending order
    df = df.sort_values('box_office', ascending=False)

    return df

# ---------------------------- Functions for Genre Analysis ----------------------------

# Define a function to get the top genres by the number of movies
def get_top_genres_by_num_movies(df, num_genres=10):
    # Count the occurrences of each genre and select the top num_genres
    genre_counts = df['genre'].value_counts()[:num_genres]
    return genre_counts

# Define a function to plot the number of movies by genre
def plot_num_movies_by_genre(tab, genre_counts):
    fig, ax = plt.subplots()
    barplot = sns.barplot(x=genre_counts.index, y=genre_counts.values, ax=ax)
    ax.set_title('Number of Movies by Genre')
    ax.set_xlabel('Genre')
    ax.set_ylabel('Number of Movies')
    ax.set_xticklabels([])  # Remove x-axis labels

    # Create custom legend
    import matplotlib.patches as mpatches
    legend_patches = []
    for index, genre in enumerate(genre_counts.index):
        color = barplot.patches[index].get_facecolor()
        legend_patch = mpatches.Patch(color=color, label=genre)
        legend_patches.append(legend_patch)

    ax.legend(handles=legend_patches, loc='upper right', bbox_to_anchor=(1.15, 1))

    # Add the plot to the GUI tab
    canvas = FigureCanvasTkAgg(fig, master=tab)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True, anchor=tk.CENTER)

# ---------------------------- Functions for Director Analysis ----------------------------

# Define a function to get the top directors by box office revenue
def get_top_directors_by_box_office(df, num_directors=10):
    director_revenues = {}

    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        # Split the directors by comma and get the box_office value
        directors = row['directors'].split(',')
        box_office = row['box_office']

        # If the box_office value is not NaN, add the revenue to the director's total
        if pd.notna(box_office):
            for director in directors:
                director = director.strip()
                if director in director_revenues:
                    director_revenues[director] += box_office
                else:
                    director_revenues[director] = box_office

    # Sort the directors by their total revenue and select the top num_directors
    top_directors = sorted(director_revenues.items(), key=lambda x: x[1], reverse=True)[:num_directors]
    return top_directors

# Define a function to plot the top directors by box office revenue
# Define a function to plot the top directors by box office revenue
def plot_top_directors_by_box_office(tab, top_directors):
    fig, ax = plt.subplots()
    directors, revenues = zip(*top_directors)

    # Use a custom color palette for the bars
    color_palette = sns.color_palette("hls", len(directors))

    barplot = sns.barplot(x=list(directors), y=list(revenues), palette=color_palette, ax=ax)
    ax.set_title('Top Directors by Box Office Revenue')
    ax.set_xlabel('Director')
    ax.set_ylabel('Box Office Revenue (USD)')
    ax.set_xticklabels([])  # Remove x-axis labels

    # Create custom legend
    import matplotlib.patches as mpatches
    legend_patches = []
    for index, director in enumerate(directors):
        color = barplot.patches[index].get_facecolor()
        legend_patch = mpatches.Patch(color=color, label=director)
        legend_patches.append(legend_patch)

    ax.legend(handles=legend_patches, loc='upper right', bbox_to_anchor=(1.15, 1))

    # Add the plot to the GUI tab
    canvas = FigureCanvasTkAgg(fig, master=tab)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True, anchor=tk.CENTER)

# ---------------------------- Functions for Year-based Search ----------------------------

# Define a function to search for movies by year
def search_movies():
    year = search_entry.get()
    try:
        # Convert the input to an integer
        year = int(year)

        # Filter the DataFrame by the specified year
        movies = df[df['year'] == year]
        movies = movies[['rank', 'name', 'year', 'rating']]

        # Display the search results in the output text box
        output.delete('1.0', tk.END)  # Clear previous output
        output.insert(tk.END, movies.to_string(index=False))

    except ValueError:
        # Display an error message if the input is not a valid year
        output.delete('1.0', tk.END)  # Clear previous output
        output.insert(tk.END, "Please enter a valid year")

# ---------------------------- Main GUI Window and Tabs ----------------------------

# Create the main window
window = tk.Tk()
window.title("IMDB-Top-250-movies-Analyse")

# Create tabs
tab_parent = ttk.Notebook(window)

# Create home tab that explains the project and each tab
# Create home tab that explains the project and each tab
home_tab = ttk.Frame(tab_parent)
tab_parent.add(home_tab, text="Home")

home_label = tk.Label(home_tab, text="Welcome to IMDB-Top-250-movies-Analyse!", font=('Arial', 18, 'bold'))
home_label.pack(pady=20)

description_label = tk.Label(home_tab, text="This project analyzes data on top 250 movies from IMDb and provides insights through visualization.", font=('Arial', 14))
description_label.pack(pady=20)

genre_label = tk.Label(home_tab, text="Number of Movies by Genre", font=('Arial', 16, 'bold'))
genre_label.pack(pady=10, anchor="w")

genre_desc_label = tk.Label(home_tab, text="This tab displays the number of movies by genre!", font=('Arial', 12))
genre_desc_label.pack(pady=10, anchor="w")

director_label = tk.Label(home_tab, text="Top Directors by Box Office Revenue", font=('Arial', 16, 'bold'))
director_label.pack(pady=10, anchor="w")

director_desc_label = tk.Label(home_tab, text="This tab displays the top directors by box office revenue.", font=('Arial', 12))
director_desc_label.pack(pady=10, anchor="w")

search_label = tk.Label(home_tab, text="Search By Year", font=('Arial', 16, 'bold'))
search_label.pack(pady=10, anchor="w")

search_desc_label = tk.Label(home_tab, text="This tab allows the user to filter the movies by year.", font=('Arial', 12))
search_desc_label.pack(pady=10, anchor="w")

# Create first tab for number of movies by genre
genre_tab = ttk.Frame(tab_parent)
tab_parent.add(genre_tab, text="Number of Movies by Genre")

# Create second tab for top directors by box office revenue
director_tab = ttk.Frame(tab_parent)
tab_parent.add(director_tab, text="Top Directors by Box Office Revenue")

# Create third tab for filtering movies by year
search_tab = ttk.Frame(tab_parent)
tab_parent.add(search_tab, text="Search By Year")

# Add search widgets and output text box to the search_tab
search_label = tk.Label(search_tab, text="Search by Year")
search_label.pack()
search_entry = tk.Entry(search_tab)
search_entry.pack()
search_button = tk.Button(search_tab, text="Search", command=search_movies)
search_button.pack()
output_label = tk.Label(search_tab, text="Search Results:")
output_label.pack()
output = tk.Text(search_tab)
output.pack()

# Load and preprocess data
df = load_and_preprocess_data()

# Get the top genres by the number of movies and plot the results in the genre_tab
genre_counts = get_top_genres_by_num_movies(df)
plot_num_movies_by_genre(genre_tab, genre_counts)

# Get the top directors by box office revenue and plot the results in the director_tab
top_directors = get_top_directors_by_box_office(df)
plot_top_directors_by_box_office(director_tab, top_directors)

# Pack the tab container and display the main window
tab_parent.pack(expand=1, fill="both")
window.mainloop()
