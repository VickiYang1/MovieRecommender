import tkinter as tk
from tkinter import Frame, Canvas, ttk, messagebox
import pandas as pd

# datasets
mf = pd.read_csv(r"C:/Users/vicki/PycharmProjects/movierecommender/movie.csv")
tf = pd.read_csv(r"C:/Users/vicki/PycharmProjects/movierecommender/tag.csv")
all_df = pd.merge(mf, tf, on="movieId", how="inner")


# button functions
def recommend():
    tag = tag_entry.get().strip()
    movie = movie_entry.get().strip()
    tag_entry.delete("0", "end")
    movie_entry.delete("0", "end")

    # Check which checkboxes are checked
    checked_genres = [genre for genre, var in genre_check_buttons if var.get()]
    any_checkbox_checked = any(var.get() for _, var in genre_check_buttons)

    # Initialize filtered_df with the original DataFrame
    filtered_df = all_df.copy()

    # Apply filtering based on checked genres
    for genre in checked_genres:
        genre_mask = filtered_df["genres"].str.strip().str.lower().str.contains(genre.lower())
        filtered_df = filtered_df[genre_mask]

    # Apply filtering based on tag (if provided)
    if tag:
        filtered_df = filtered_df[filtered_df["tag"].str.contains(tag, case=False, na=False)]

    # Apply filtering based on movie title (if provided)
    if movie:
        filtered_df = filtered_df[filtered_df["title"].str.contains(movie, case=False, na=False)]

    # Group by movie ID and concatenate tags
    grouped_df = filtered_df.groupby("movieId").agg({
        "title": "first",  # Take the first movie title
        "tag": lambda x: ", ".join(x.dropna().astype(str)),  # Concatenate tags, handle NaN
        "genres": "first"  # Take the first genre
    }).reset_index()

    if not tag and not movie and not any_checkbox_checked:
        tk.messagebox.showinfo("Error","Please input a selection")
    else:
        # Clear existing table data
        for item in movie_tree.get_children():
            movie_tree.delete(item)

        # Populate the table with filtered movie data
        for index, row in grouped_df.iterrows():
            movie_tree.insert("", "end", values=(row["title"], row["genres"], row["tag"]))



# Define window
root = tk.Tk()
root.iconbitmap("movies.ico")
root.title("Movie Recommendation System")
root.geometry("1000x650")
root.resizable(False, False)

# Text and colors
input_font = ("Courier", 14)
letter_font = ("Courier", 10)
bg_color = "#2F3E46"  # Dark green (darkest color)
letter_color = "#CAD2C5"  # Light green (lightest color)

# Main Frame
main_frame = Frame(root)
main_frame.grid(sticky=tk.NSEW)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Canvas
canvas = Canvas(main_frame)
canvas.grid(row=0, column=0, sticky=tk.NSEW)
canvas.configure(bg=bg_color)

# Scrollbar
scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Interior Frame
int_frame = Frame(canvas, bg=bg_color)
canvas.create_window((0, 0), window=int_frame, anchor="nw")

# Create a Treeview widget for displaying movies
movie_tree = ttk.Treeview(int_frame, columns=("Movie Title", "Genre", "Tag"), show="headings")
movie_tree.heading("Movie Title", text="Movie Title")
movie_tree.heading("Genre", text="Genre")
movie_tree.heading("Tag", text="Tag")
movie_tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

title_label = tk.Label(int_frame, text="Movie Recommendation System", font=("Helvetica", 48), fg=letter_color, bg=bg_color)
title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Movie Search label
movie_label = tk.Label(int_frame, text="Search by Title:", font=input_font, fg=letter_color, bg=bg_color)
movie_label.grid(row=1, column=0, padx=10, pady=10)

# Movie entry
movie_entry = tk.Entry(int_frame, width=50, font = ("Helvetica", 16 ))
movie_entry.grid(row=1, column=1, padx=10, pady=10)

# Search tag label
tag_label = tk.Label(int_frame, text="Search by Tag:", font=input_font, fg=letter_color, bg=bg_color)
tag_label.grid(row=2, column=0, padx=10, pady=10)

# search entry
tag_entry = tk.Entry(int_frame, width=50, font = ("Helvetica", 16 ))
tag_entry.grid(row=2, column=1, padx=10, pady=10)

# recommend button
recommend_button = tk.Button(int_frame, text="Recommend", command=recommend, font=input_font)
recommend_button.grid(row=2, column=2, padx=10, pady=10)

# Create a separate frame for checkboxes
checkbox_frame = Frame(int_frame, bg=bg_color)
checkbox_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky=tk.W)

# checkbox for categories
genres = ["Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary", "Fantasy", "Horror",
          "IMAX", "Musical", " Mystery", "Romance", "Sci-fi", "Thriller", "War", "Western", "(no genre listed)"]


genre_check_buttons = []
for i, genre in enumerate(genres):
    var = tk.BooleanVar()
    check_button = tk.Checkbutton(checkbox_frame, text=genre, variable=var, bg=bg_color, font=input_font, fg=letter_color, selectcolor="#52796F")
    row_num = i // 6
    col_num = i % 6
    check_button.grid(row=row_num, column=col_num, padx=10, pady=5, sticky=tk.W)
    genre_check_buttons.append((genre, var))

# Configure weights for expansion
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

root.mainloop()
