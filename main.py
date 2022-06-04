import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

# datasets
mf = pd.read_csv(r"C:/Users/vicki/PycharmProjects/movierecommender/movie.csv")
tf = pd.read_csv(r"C:/Users/vicki/PycharmProjects/movierecommender/tag.csv")
all_df = pd.merge(mf, tf, on="movieId", how="inner")

# define window
root = tkinter.Tk()
root.iconbitmap("movies.ico")
root.title("Movie Recommendations")
root.geometry("870x600")

letter_font = ('Times New Roman', 18)
bg_color = "#183642" # dark blue
button_color = "#73628A" # purple
letter_color = "#EAEAEA" # white
root.config(bg=bg_color)

text = tk.Text(root, height=8, width=70)
text.grid(row=22, column=1,columnspan=3, sticky='EW')

scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
scrollbar.grid(row=22, column=4, columnspan=3, sticky='ns')
text['yscrollcommand'] = scrollbar.set

# genres
genres = [" ","Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary", "Fantasy", "Horror",
          "IMAX", "Musical", " Mystery", "Romance", "Sci-fi", "Thriller", "War", "Western", "(no genre listed)"]

# gui font
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
display_frame.grid(padx=2, pady=(5, 20))
button_frame.grid(padx=2, pady=5)

# functions


def search():
    text.delete("1.0", "end")
    first = input_list1.get()
    second = input_list2.get()
    third = input_list3.get()
    tag_word = tags.get().title()
    number = int(num.get())

    if first != "" and second != "" and third != "" and tag_word != "":
        r1 = all_df.loc[all_df['genres'].str.contains(first, case=False)]
        r2 = r1.loc[r1['genres'].str.contains(second, case=False)]
        r3 = r2.loc[r2['genres'].str.contains(third, case=False)]
        r4 = r3.loc[r3['tag'].str.contains(tag_word, case=False, na=False)]
        result = (r4.drop_duplicates(subset=['title']).head(number))
        text.insert(INSERT, result.title.to_string(index=False))

    elif first != "" and second != "" and third == "" and tag_word != "":
        r1 = all_df.loc[all_df['genres'].str.contains(first, case=False)]
        r2 = r1.loc[r1['genres'].str.contains(second, case=False)]
        r3 = r2.loc[r2['tag'].str.contains(tag_word, case=False, na=False)]
        result = (r3.drop_duplicates(subset=['title']).head(number))
        text.insert(INSERT, result.title.to_string(index=False))

    elif first != "" and second == "" and third == "" and tag_word != "":
        r1 = all_df.loc[all_df['genres'].str.contains(first, case=False)]
        r2 = r1.loc[r1['tag'].str.contains(tag_word, case=False, na=False)]
        result = (r2.drop_duplicates(subset=['title']).head(number))
        text.insert(INSERT, result.title.to_string(index=False))

    elif first != "" and second != "" and third != "" and tag_word == "":
        r1 = all_df.loc[all_df['genres'].str.contains(first, case=False)]
        r2 = r1.loc[r1['genres'].str.contains(second, case=False)]
        r3 = r2.loc[r2['genres'].str.contains(third, case=False)]
        result = (r3.drop_duplicates(subset=['title']).head(number))
        text.insert(INSERT, result.title.to_string(index=False))

    elif first != " " and second != "" and third == "" and tag_word == "":
        r1 = all_df.loc[all_df['genres'].str.contains(first, case=False)]
        r2 = r1.loc[r1['genres'].str.contains(second, case=False)]
        result = (r2.drop_duplicates(subset=['title']).head(number))
        text.insert(INSERT, result.title.to_string(index=False))

    elif first != "" and second == "" and third == "" and tag_word == "":
        r1 = all_df.loc[all_df['genres'].str.contains(first, case=False)]
        result = (r1.drop_duplicates(subset=['title']).head(number))
        text.insert(INSERT, result.title.to_string(index=False))

    elif first == "" and second == "" and third == "" and tag_word != "":
        r1 = all_df.loc[all_df['tag'].str.contains(tag_word, case=False, na=False)]
        result = (r1.drop_duplicates(subset=['title']).head(number))
        text.insert(INSERT, result.title.to_string(index=False))
    elif first == "" and second == "" and third == "" and tag_word == "" and str(number) == "0":
        messagebox.showinfo("Error", "Please enter a movie genre or tag")


input_option1 = StringVar()
input_option1.set(genres[0])
input_option2 = StringVar()
input_option2.set(genres[0])
input_option3 = StringVar()
input_option3.set(genres[0])


# button layouts
tag_question = Label(root, text="Enter a Tag: ", font=letter_font, bg=bg_color, fg=letter_color)
tag_question.grid(row=0, column=1,padx=10, pady=10)

tags = Entry(root, width=20, font=letter_font, borderwidth=3)
tags.grid(row=0, column=2,padx=10, pady=10)
tags.insert(0, "")

directions = Label(root, text="Select up to 3 movie genres: ", font=letter_font, bg=bg_color, fg=letter_color)
directions.grid(row=6, column=2)

input_list1 = ttk.Combobox(root, values=genres, width=20, font=letter_font)
input_list1.grid(row=10, column=1, padx=10, pady=10)

input_list2 = ttk.Combobox(root, values=genres, width=20, font=letter_font)
input_list2.grid(row=10, column=2, padx=10, pady=10)

input_list3 = ttk.Combobox(root, values=genres, width=20, font=letter_font)
input_list3.grid(row=10, column=3, padx=10, pady=10)

num_question = Label(root, text="How many movie recommendations would you like to see?: ", font=letter_font, bg=bg_color, fg=letter_color)
num_question.grid(row=16, column=0, columnspan=4)

num = Entry(root, width=10, font=letter_font, borderwidth=3)
num.grid(row=17, column=1, columnspan=3, padx=10, pady=10)
num.insert(0, "0")

find_movie = Button(root, text="Search Movies", bg=button_color, fg=letter_color, font =letter_font, command=search)
find_movie.grid(row=20, column=1, columnspan=3, padx=10, pady=10, ipadx=50)


root.mainloop()
