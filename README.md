# Movie Recommendation System

The **Movie Recommendation System** is a Python-based application that allows users to discover recommended and similar movies based on their preferences. By leveraging data from CSV files, the system enables users to search for movies by title, tag, and genre, filtering the results according to the input provided.

## Features

- **Search by Title**: Users can search for movies by entering a specific title or keyword.
- **Search by Tag**: Users can find movies associated with specific tags (e.g., "adventure," "comedy").
- **Filter by Genre**: Users can select one or more genres to filter the movie recommendations.
- **Result Display**: Filtered movies are displayed in a table format with their title, genres, and associated tags.
- **User-Friendly Interface**: The application features a graphical user interface (GUI) using Tkinter, providing an intuitive way to interact with the system.

## Modules and Libraries

- **tkinter**: The core library used to create the graphical user interface (GUI).
  - **Frame**: A container widget used to hold and organize other widgets.
  - **Canvas**: A widget used to create scrollable areas for the interface.
  - **ttk**: A themed widget set that provides a more modern look to standard Tkinter widgets.
  - **messagebox**: A module that provides a way to show message dialogs (like error or information pop-ups) in the GUI.
  
- **pandas**: A powerful data analysis library used for reading, merging, and filtering the movie and tag datasets.
  - `pd.read_csv`: Reads the CSV files into Pandas DataFrames for easy data manipulation.
  - `pd.merge`: Merges the movie and tag DataFrames on the common `movieId` column, creating a unified dataset.

## Project Workflow

1. **Data Loading**: The system loads data from `movie.csv` and `tag.csv` using Pandas. These datasets are merged based on the movie ID to create a comprehensive DataFrame that includes movie titles, genres, and tags.

2. **User Input**: Users can input a movie title, tag, or select genres from a list of checkboxes.

3. **Data Filtering**: The system filters the dataset based on user input:
   - **Title Search**: Filters movies that contain the input title or keyword.
   - **Tag Search**: Filters movies associated with the input tag.
   - **Genre Filter**: Filters movies that belong to the selected genres.

4. **Result Display**: The filtered movie data is displayed in a table within the GUI, showing the movie title, genres, and associated tags.

5. **Error Handling**: The system includes error handling to prompt the user if no input is provided before searching.

## Future Enhancements

- **Additional Filters**: Incorporate filters for movie release year, director, or ratings.
- **Data Visualization**: Add visualizations to display genre distributions or trends in the recommended movies.
- **Machine Learning**: Integrate machine learning algorithms to provide personalized movie recommendations
