import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Blueberry Oatmeal')
streamlit.text('Kale Smoothie')
streamlit.text('Free Range Eggs')
streamlit.text('Avocado Toast')

streamlit.title('Build you own fruit smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
