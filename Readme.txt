1- Overview:
  - Developed a machine learning model to predict flight prices using regression techniques. Explored and preprocessed the dataset, identified key features, and applied various regression models.

2- Data Exploration:
 - Conducted exploratory data analysis (EDA) to understand the dataset.
 - Cleaned data by removing duplicates, handling missing values, and fixing inconsistencies.
 - Explored features like airline, date of journey, source, destination, flight duration, stops, and more.

3- Business Insights:
- Explored business questions such as the impact of airline, routes, flight duration, stops, and departure times on flight prices.
Analyzed the distribution of flight distances, durations, and prices.

4- Data Preparation:
- Engineered features such as distance categories, duration categories, and encoded categorical variables using ordinal and binary encoders.
- Applied RobustScaler to standardize numerical features.

5- Model Training:
- Trained multiple regression models, including Linear Regression, Decision Tree Regressor, Random Forest Regressor, XGBoost, KNeighbors Regressor, Support Vector Regression, and Multi-Layer Perceptron Regressor.
- Evaluated models using cross-validation to assess performance.

6- Model Tuning:
- Fine-tuned hyperparameters for the XGBoost model using GridSearchCV.

7- Deployment:
- Deployed the best-performing model (XGBoost) on Streamlit for creating an interactive data science application.
- Connected the project to Streamlit Cloud for wider accessibility.
- You can interact with the deployed application on the cloud by visiting the following link:
(https://flightpriceprediction-92mayfuvw6lfhbkapa6dd5.streamlit.app/)

