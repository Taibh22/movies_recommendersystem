# Movies Recommender System Website 

# Introduction:
The Movies Recommender System Website is a web application designed to suggest movies to users based on their viewing history. This application is built using Python and Flask web framework, and relies on the collaborative filtering algorithm to make suggestions. The website allows users to create an account, rate movies, and receive movie recommendations based on their ratings.

# Requirements:
To run this application, the user must have Python 3 installed on their computer. Additionally, the application requires the following libraries to be installed:
Flask
NumPy
Pandas
Scikit-learn
SQLAlchemy
Requests

# Installation:
The Movies Recommender System Website is a web application designed to suggest movies to users based on their viewing history. This application is built using Python and Flask web framework, and relies on the collaborative filtering algorithm to make suggestions. The website allows users to create an account, rate movies, and receive movie recommendations based on their ratings. In addition, the application uses the IMDb API to display movie information and ratings.


# Usage:
To use the application, the user must first provide a dataset of movie ratings. The dataset should be in a CSV file format and should contain the following columns: user ID, movie ID, and rating. A popular dataset that can be used is the ml-latest-small dataset, which can be downloaded from the GroupLens website (https://grouplens.org/datasets/movielens/latest/).

Once the dataset is available, the user can run the application by executing the app.py file using the following command in their terminal/command prompt:
python app.py

The user can access the website using their web browser and create an account, rate movies, and receive movie recommendations based on their ratings. The website also displays movie information and ratings using the IMDb API.

# Output:
The application will output a list of recommended movies for the user, along with their predicted ratings. The list will be sorted in descending order based on the predicted ratings, with the highest rated movies appearing first. 

# Conclusion:
The Movies Recommender System Website is a powerful tool for suggesting movies to users based on their viewing history. By using collaborative filtering and the IMDb API, the application can accurately predict which movies a user is likely to enjoy and display detailed information about each movie. With the ability to create an account, rate movies, and receive recommendations, the website provides a personalized experience for each user. The ml-latest-small dataset is a popular choice for testing the application and can be easily integrated into the program.

