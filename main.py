import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Load the data from the CSV file
df = pd.read_csv('moviesData.csv')

# Replace 'Not Available' values in box_office column with NaN
df['box_office'] = df['box_office'].replace('Not Available', pd.NaT)

# Convert box_office to integer
df['box_office'] = pd.to_numeric(df['box_office'], errors='coerce').astype('Int64')

# Sort the dataframe by box_office in descending order
df = df.sort_values('box_office', ascending=False)

# Define a function to get the top genres by the number of movies
def get_top_genres_by_num_movies(df, num_genres=10):
    # Count the occurrences of each genre and select the top num_genres
    genre_counts = df['genre'].value_counts()[:num_genres]
    return genre_counts

# Define a function to plot the number of movies by genre
import matplotlib.patches as mpatches

def plot_num_movies_by_genre(tab, genre_counts):
    fig, ax = plt.subplots()
    barplot = sns.barplot(x=genre_counts.index, y=genre_counts.values, ax=ax)
    ax.set_title('Number of Movies by Genre')
    ax.set_xlabel('Genre')
    ax.set_ylabel('Number of Movies')
    ax.set_xticklabels([])  # Remove x-axis labels

    # Create custom legend
    legend_patches = []
    for index, genre in enumerate(genre_counts.index):
        color = barplot.patches[index].get_facecolor()
        legend_patch = mpatches.Patch(color=color, label=genre)
        legend_patches.append(legend_patch)
    
    ax.legend(handles=legend_patches, loc='upper right', bbox_to_anchor=(1.15, 1))

    canvas = FigureCanvasTkAgg(fig, master=tab)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True, anchor=tk.CENTER)

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
import matplotlib.patches as mpatches

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
    legend_patches = []
    for index, director in enumerate(directors):
        color = barplot.patches[index].get_facecolor()
        legend_patch = mpatches.Patch(color=color, label=director)
        legend_patches.append(legend_patch)
    
    ax.legend(handles=legend_patches, loc='upper right', bbox_to_anchor=(1.15, 1))

    canvas = FigureCanvasTkAgg(fig, master=tab)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True, anchor=tk.CENTER)

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

# Create the main window
window = tk.Tk()
window.title("IMDB-Top-250-movies-Analyse")

# Set dark theme colors
bg_color = "#2b2b2b"
fg_color = "#ffffff"

window.config(bg=bg_color)

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

home_label = tk.Label(home_tab, text="Welcome to IMDB-Top-250-movies-Analyse!", font=('Arial', 18, 'bold'), bg=bg_color, fg=fg_color)
home_label.pack(pady=20)

description_label = tk.Label(home_tab, text="This project analyzes data on top 250 movies from IMDb and provides insights through visualization.", font=('Arial', 14), wraplength=400, justify='left', bg=bg_color, fg=fg_color)
description_label.pack(pady=20)

info_label = tk.Label(home_tab, text="Each tab provides a different analysis:\n1. Number of Movies by Genre\n2. Top Directors by Box Office Revenue\n3. Search Movies by Year", font=('Arial', 14), wraplength=400, justify='left', bg=bg_color, fg=fg_color)
info_label.pack(pady=20)

# Create genre tab
genre_tab = ttk.Frame(tab_parent)
tab_parent.add(genre_tab, text="Movies by Genre")

# Plot the number of movies by genre in the genre tab
top_genres = get_top_genres_by_num_movies(df)
plot_num_movies_by_genre(genre_tab, top_genres)

# Create director tab
director_tab = ttk.Frame(tab_parent)
tab_parent.add(director_tab, text="Top Directors")

# Plot the top directors by box office revenue in the director tab
top_directors = get_top_directors_by_box_office(df)
plot_top_directors_by_box_office(director_tab, top_directors)

# Create search tab
search_tab = ttk.Frame(tab_parent)
tab_parent.add(search_tab, text="Search Movies by Year")

search_label = tk.Label(search_tab, text="Enter the year:", bg=bg_color, fg=fg_color)
search_label.pack(pady=10)

search_entry = tk.Entry(search_tab)
search_entry.pack(pady=10)

search_button = tk.Button(search_tab, text="Search", command=search_movies, bg=bg_color, fg=fg_color)
search_button.pack(pady=10)

output = tk.Text(search_tab, height=10, width=60, bg=bg_color, fg=fg_color)
output.pack(pady=10)

tab_parent.pack(expand=True, fill="both")







window.mainloop()

