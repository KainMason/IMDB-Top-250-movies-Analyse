import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load the data from CSV file
df = pd.read_csv('moviesData.csv')

# Replace 'Not Available' values in box_office column with NaN
df['box_office'] = df['box_office'].replace('Not Available', pd.NaT)

# Convert box_office to integer
df['box_office'] = pd.to_numeric(df['box_office'], errors='coerce').astype('Int64')

# Sort the dataframe by box_office in descending order
df = df.sort_values('box_office', ascending=False)

# Define function to get top genres by number of movies
def get_top_genres_by_num_movies(df, num_genres=10):
    genre_counts = df['genre'].value_counts()[:num_genres]
    return genre_counts

# Define function to plot number of movies by genre
def plot_num_movies_by_genre(tab, genre_counts):
    plt.figure(figsize=(12, 6))
    sns.barplot(x=genre_counts.index, y=genre_counts.values)
    plt.title('Number of Movies by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=90)
    canvas = FigureCanvasTkAgg(plt.gcf(), master=tab)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Define function to get top directors by box office revenue
def get_top_directors_by_box_office(df, num_directors=10):
    director_revenues = {}
    for _, row in df.iterrows():
        directors = row['directors'].split(',')
        box_office = row['box_office']
        if pd.notna(box_office):
            for director in directors:
                director = director.strip()
                if director in director_revenues:
                    director_revenues[director] += box_office
                else:
                    director_revenues[director] = box_office
    top_directors = sorted(director_revenues.items(), key=lambda x: x[1], reverse=True)[:num_directors]
    return top_directors

# Define function to plot top directors by box office revenue
def plot_top_directors_by_box_office(tab, top_directors):
    plt.figure(figsize=(12, 6))
    directors, revenues = zip(*top_directors)
    plt.bar(directors, revenues)
    plt.title('Top Directors by Box Office Revenue')
    plt.xlabel('Director')
    plt.ylabel('Box Office Revenue (USD)')
    plt.xticks(rotation=90)
    canvas = FigureCanvasTkAgg(plt.gcf(), master=tab)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Define function to search for movies by year
def search_movies():
    year = search_entry.get()
    try:
        year = int(year)
        movies = df[df['year'] == year]
        movies = movies[['rank', 'name', 'year', 'rating']]
        output.delete('1.0', tk.END)  # clear previous output
        output.insert(tk.END, movies.to_string(index=False))
    except ValueError:
        output.delete('1.0', tk.END)  # clear previous output
        output.insert(tk.END, "Please enter a valid year")

# Create the main window
window = tk.Tk()
window.title("IMDB-Top-250-movies-Analyse")

# Create tabs
tab_parent = ttk.Notebook(window)

# Create first tab for number of movies by genre
genre_tab = ttk.Frame(tab_parent)
tab_parent.add(genre_tab, text="Number of Movies by Genre")

# Create second tab for top directors by box office revenue
director_tab = ttk.Frame(tab_parent)
tab_parent.add(director_tab, text="Top Directors by Box Office Revenue")
# Create second tab for top directors by box office revenue
search_tab = ttk.Frame(tab_parent)
tab_parent.add(search_tab, text="Search By Year")
# Add search widgets and output text box to main window
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

# Plot number of movies by genre on the first tab
genre_counts = get_top_genres_by_num_movies(df)
plot_num_movies_by_genre(genre_tab, genre_counts)

# Plot top directors by box office revenue on the second tab
top_directors = get_top_directors_by_box_office(df)
plot_top_directors_by_box_office(director_tab, top_directors)

tab_parent.pack(expand=1, fill='both')

# Run the main loop
window.mainloop()

