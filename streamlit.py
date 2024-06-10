import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data
def load_data():
    data = pd.read_csv('C:/Users/user/Documents/Sir Neil/PYTHON/premid/ObesityDataSet_raw_and_data_sinthetic.csv')
    return data

# Function to plot distribution of a variable
def plot_distribution(data, column):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data[column], ax=ax)
    ax.set_title(f'Distribution of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Count')
    st.pyplot(fig)

# Function to plot a pie chart
def plot_pie_chart(data, column):
    fig, ax = plt.subplots(figsize=(8, 6))
    data[column].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    ax.set_title(f'Pie Chart of {column}')
    st.pyplot(fig)

# Function to plot a bar chart
def plot_bar_chart(data, x_column, y_column):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=data[x_column], y=data[y_column], ci=None, ax=ax)
    ax.set_title(f'Bar Chart of {y_column} by {x_column}')
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    st.pyplot(fig)

# Function to plot a correlation heatmap
def plot_correlation_heatmap(data):
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

# Main function to run the app
def main():
    st.title('Insights from Obesity Dataset')
    st.write('This app showcases insights from the obesity dataset.')

    # Load the data
    data = load_data()

    # Sidebar for user inputs
    st.sidebar.header('Options')
    
    # Show dataset
    if st.sidebar.checkbox('Show Dataset'):
        st.write(data)

    # Show data summary
    if st.sidebar.checkbox('Show Data Summary'):
        st.write(data.describe(include='all'))

    # Narrative explaining the context of the data
    st.sidebar.write("""
    ## About the Dataset
    The dataset contains information about individuals including attributes such as age, gender, height, weight, physical activity level, eating habits, transportation mode, and family history of obesity.
    The target variable, 'NObeyesdad', represents the level of obesity classified into several categories.
    We'll explore various insights from this dataset using different visualization charts.
    """)

    # Select visualization type
    visualization_type = st.sidebar.selectbox('Select Visualization Type', ['Distribution Plot', 'Pie Chart', 'Bar Chart', 'Correlation Heatmap'])

    # Visualizations
    if visualization_type == 'Distribution Plot':
        selected_column = st.sidebar.selectbox('Select Column for Distribution Plot', data.columns)
        plot_distribution(data, selected_column)
    elif visualization_type == 'Pie Chart':
        selected_column = st.sidebar.selectbox('Select Column for Pie Chart', data.columns)
        plot_pie_chart(data, selected_column)
    elif visualization_type == 'Bar Chart':
        x_column = st.sidebar.selectbox('Select X-Axis Column', data.columns)
        y_column = st.sidebar.selectbox('Select Y-Axis Column', data.columns)
        plot_bar_chart(data, x_column, y_column)
    elif visualization_type == 'Correlation Heatmap':
        plot_correlation_heatmap(data)

if __name__ == '__main__':
    main()
