Diabetes Prediction System
===========================

Description:
------------
This system is designed to diagnostically predict whether a patient has diabetes based on certain diagnostic measurements. The dataset comprises female patients of at least 21 years old of Pima Indian heritage.

Files:
------
1. data_preprocessing.py - Contains functions for preprocessing the dataset. It deals with missing values, scales the features, and splits the dataset into training and testing sets.
2. evaluation.py - Contains functions to evaluate the prediction results. Metrics such as accuracy, precision, recall, and F1 score are used.
3. model_building.py - Contains functions to train the Logistic Regression model and make predictions.
4. main.py - The main execution script. It loads the data, preprocesses it, and visualizes the distribution of diagnostic measurements.

Instructions:
-------------
1. Ensure that Python 3.x is installed.
2. Install the necessary packages using the command:
    ```
    pip install -r requirements.txt
    ```
3. To run the main script and visualize the data, use the command:
    ```
    python main.py
    ```

Notes:
------
- The dataset 'diabetes.csv' should be present in the same directory as the scripts for the code to run successfully.
- Make sure all the .py files (`data_preprocessing.py`, `evaluation.py`, `model_building.py`, and `main.py`) are in the same directory.
