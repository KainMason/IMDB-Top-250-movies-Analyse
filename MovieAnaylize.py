import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load the data from CSV file
#This CODE meets requirement 1 of the CODE LOUISVILLE PROJECT LISTED IN THE .README
df = pd.read_csv('moviesData.csv')

# Replace 'Not Available' values in box_office column with NaN
#This CODE meets requirement 2 of the CODE LOUISVILLE PROJECT LISTED IN THE .README
df['box_office'] = df['box_office'].replace('Not Available', pd.NaT)

# Convert box_office to integer
df['box_office'] = pd.to_numeric(df['box_office'], errors='coerce').astype('Int64')

# Sort the dataframe by box_office in descending order
df = df.sort_values('box_office', ascending=False)

# Define function to get top genres by number of movies
#This CODE meets requirement 3(fig.1) of the CODE LOUISVILLE PROJECT LISTED IN THE .README
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
#This CODE meets requirement 3(fig.2) of the CODE LOUISVILLE PROJECT LISTED IN THE .README
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
#This CODE meets requirement 3 (fig.3) of the CODE LOUISVILLE PROJECT LISTED IN THE .README
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
#This CODE meets requirement 4 of the CODE LOUISVILLE PROJECT LISTED IN THE .README
window = tk.Tk()
window.title("IMDB-Top-250-movies-Analyse")

# Create tabs
tab_parent = ttk.Notebook(window)

# Set custom style
style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn', borderwidth=0)
style.configure('lefttab.TNotebook.Tab', padding=(15,10), width=20, foreground="gray")
style.map('lefttab.TNotebook.Tab', background=[('selected', 'white')], foreground=[('selected', '#0B72B9')])


# Create home tab that explains the project and each tab
home_tab = ttk.Frame(tab_parent)
tab_parent.add(home_tab, text="Home")

home_label = tk.Label(home_tab, text="Welcome to IMDB-Top-250-movies-Analyse!", font=('Arial', 18, 'bold'))
home_label.pack(pady=20)

description_label = tk.Label(home_tab, text="This project analyzes data on top 250 movies from IMDb and provides insights through visualization.", font=('Arial', 14))
description_label.pack(pady=20)

genre_label = tk.Label(home_tab, text="Number of Movies by Genre", font=('Arial', 16, 'bold'))
genre_label.pack(pady=10, anchor="w")

genre_desc_label = tk.Label(home_tab, text="This tab displays the number of movies by genre.", font=('Arial', 12))
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

