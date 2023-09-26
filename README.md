# Sportify Song Recommender System
# Introduction
Sportify Song Recommender System is a project designed to demonstrate capabilities in building a recommendation system. The system utilizes cosine similarity calculations to recommend songs based on user input and provides detailed information about the songs. This documentation provides a comprehensive overview of the project, its features, installation instructions, usage guide, and deployment options.
**Features**
The Sportify Song Recommender System offers the following features:
1.	Song Recommendation: The system recommends songs based on cosine similarity calculations. Given a song name, it identifies similar songs and suggests them to the user.
2.	Song Information Retrieval: Users can search for a specific song and retrieve detailed information about the song, including artist, album, album number, track number, duration, and release date.
3.	Song Name Suggestions: The system provides song name suggestions as users type in the search bar. This feature assists users in finding the desired song quickly.
4.	User-Friendly Interface: The system is built using Streamlit, a user-friendly Python library for creating interactive web applications. The interface allows users to easily search for songs, view suggestions, and explore recommended songs.

# Requirements
To run the Sportify Song Recommender System, ensure that the following libraries are installed:
•	Streamlit
•	Pandas
•	Pickle
•	Pillow (PIL)
You can install these libraries using pip, for example:
pip install streamlit pandas pillow
# Project Overview
1.	Data Collection: The project utilizes song data collected from Kaggle or any other relevant source. The data should be in a CSV format.
2.	Data Cleaning: The collected data is cleaned to remove any inconsistencies or irrelevant features. The cleaned data should be saved in a CSV format.
3.	Cosine Similarity Calculation: The project calculates the cosine similarity matrix based on the cleaned data. The matrix serves as the foundation for song recommendations.
4.	Streamlit App Development: The project uses Streamlit to create an interactive web application. The app includes a search bar, song suggestions, song information display, and recommended song cards.
5.	Deployment: The Streamlit app can be deployed to a hosting platform or server for users to access and interact with the system.
# Author
This project was developed by Bennett Mhlanga, a student at the University of Zimbabwe.
Bennettmhlanga959@gmail.com

# Note
You might not see the recommended songs because the dataset that I used has millions of songs but I calculated the cosine similarity on 1000 sample songs only because of limited computational resources😓😓.
