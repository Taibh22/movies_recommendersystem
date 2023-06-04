# movies_recommendersystem
Movies Recommender System Website 

Introduction:
The Movies Recommender System Website is a web application designed to suggest movies to users based on their viewing history. This application is built using Python and Flask web framework, and relies on the collaborative filtering algorithm to make suggestions. The website allows users to create an account, rate movies, and receive movie recommendations based on their ratings.

Requirements:
To run this application, the user must have Python 3 installed on their computer. Additionally, the application requires the following libraries to be installed:
- Flask
- NumPy
- Pandas
- Scikit-learn
- SQLAlchemy

Installation:
To install the required libraries, the user can use the following command in their terminal/command prompt:
pip install flask numpy pandas scikit-learn sqlalchemy

Usage:
To use the application, the user must first provide a dataset of movie ratings. The dataset should be in a CSV file format and should contain the following columns: user ID, movie ID, and rating.

Once the dataset is available, the user can run the application by executing the app.py file using the following command in their terminal/command prompt:
python app.py

The application will then start running on localhost (http://127.0.0.1:5000/). The user can access the website using their web browser and create an account, rate movies, and receive movie recommendations based on their ratings.

Output:
The application will output a list of recommended movies for the user, along with their predicted ratings. The list will be sorted in descending order based on the predicted ratings, with the highest rated movies appearing first.

Conclusion:
The Movies Recommender System Website is a powerful tool for suggesting movies to users based on their viewing history. By using collaborative filtering, the application can accurately predict which movies a user is likely to enjoy, making it a valuable resource for anyone looking for movie recommendations. With the ability to create an account, rate movies, and receive recommendations, the website provides a personalized experience for each user.
