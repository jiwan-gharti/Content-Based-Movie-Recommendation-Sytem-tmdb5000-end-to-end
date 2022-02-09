**** Content-Based-Movie-Recommendation-Sytem-tmdb500 ****


Running this project, you should do following steps:

- first you should go to training_model folder and run the jupyter notebook file (Movie Recommendation system.ipynb)
    - in this file you can do further featuring engineering, feature selection and many more before exporting models
    - I used bag of words for the feature vectorization.
- after then you get the training weight in the form of .pkl 
- place .pkl files on the working directory
- finally, Run the command : 
    - streamlit run app.py

**Requirements:**

- Model Training phase:
    - numpy 
    - pandas
    - seaborn
    - matplolib
    - sklearn
- web implementing phase:
    - streamlit
    - requests
        

