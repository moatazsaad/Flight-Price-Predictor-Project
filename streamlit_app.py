
import streamlit as st
import pandas as pd 
import joblib

# Load the trained model and input variables
Model = joblib.load("Model.pkl")
Inputs = joblib.load("Inputs.pkl")

# Function for making flight price predictions
def prediction(Airline, Source, Destination, Month_of_Journey_Num, Day_of_Journey_Num, Distance, Stops_Counts, Dep_Hour, Categorized_Duration, Meal, Arrival_Hour, Arrival_Day_Period, Dep_Day_Period):
    # Create a test DataFrame with the input variables
    test_df = pd.DataFrame(columns=Inputs)
    test_df.at[0, "Airline"] = Airline
    test_df.at[0, "Source"] = Source
    test_df.at[0, "Destination"] = Destination
    test_df.at[0, "Month_of_Journey"] = Month_of_Journey_Num
    test_df.at[0, "Day_of_Journey_Num"] = Day_of_Journey_Num
    test_df.at[0, "Distance"] = Distance
    test_df.at[0, "Stops_Counts"] = Stops_Counts
    test_df.at[0, "Dep_Hour"] = Dep_Hour
    test_df.at[0, "Categorized_Duration"] = Categorized_Duration
    test_df.at[0, "Meal"] = Meal
    test_df.at[0, "Arrival_Hour"] = Arrival_Hour
    test_df.at[0, "Arrival_Day_Period"] = Arrival_Day_Period
    test_df.at[0, "Dep_Day_Period"] = Dep_Day_Period
    # Make predictions using the loaded model
    result = Model.predict(test_df)
    return result[0]

def main():
    # Set up the Streamlit app title and input widgets
    st.set_page_config(page_title="Flight Price Predictor", page_icon="✈️")
    st.title("Flight Price Predictor")
    st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    with st.form("prediction_form"):
        st.subheader("Enter the flight details below:")
        
        Airline = st.selectbox("Airline Name", ['Air India', 'Jet Airways', 'IndiGo', 'SpiceJet', 'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia'])
        col1, col2 = st.columns(2)
        with col1:
            Source = st.selectbox("Departure City", ['Kolkata', 'Delhi', 'Banglore', 'Chennai', 'Mumbai'])
        with col2:
            Destination = st.selectbox("Arrival City", ['Banglore', 'Cochin', 'New Delhi', 'Kolkata', 'Delhi', 'Hyderabad'])
        
        Month_of_Journey_Num = st.slider("Departure Month", 1, 12, 1)
        Day_of_Journey_Num = st.slider("Day of Travel", 1, 31, 1)
        Distance = st.selectbox("Flight Distance", ['medium distance', 'long distance', 'short distance'])
        Stops_Counts = st.selectbox("Number of Stops", [0, 1, 2, 3, 4])
        Categorized_Duration = st.selectbox("Flight Duration", ['Short duration', 'Medium duration', 'Long duration'])
        
        col3, col4 = st.columns(2)
        with col3:
            Dep_Day_Period = st.selectbox("Departure Period", ['Early Morning', 'Afternoon', 'Evening', 'Night'])
            Dep_Hour = st.slider("Departure Hour", 0, 23, 0)
        with col4:
            Arrival_Day_Period = st.selectbox("Arrival Period", ['Early Morning', 'Afternoon', 'Evening', 'Night'])
            Arrival_Hour = st.slider("Arrival Hour", 0, 23, 0)
        
        Meal = st.selectbox("Meal", [0, 1])
        
        submitted = st.form_submit_button("Predict")
        if submitted:
            results = prediction(Airline, Source, Destination, Month_of_Journey_Num, Day_of_Journey_Num, Distance, Stops_Counts, Dep_Hour, Categorized_Duration, Meal, Arrival_Hour, Arrival_Day_Period, Dep_Day_Period)
            st.success(f"The predicted flight cost is {round(results)} Indian Rupees.")

if __name__ == '__main__':
    main()
