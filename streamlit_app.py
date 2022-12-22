import streamlit
import pandas
import requests

streamlit.title('Joes Vegan Rib Shack ')
streamlit.header('Breakfast Menu')
streamlit.text('Vegan Blueberry Bacon Oatmeal')
streamlit.text('Kale and Chicken Stock Smoothie')
streamlit.text('Free Range Instant Eggs')
streamlit.text('Avocado Toast')

streamlit.title('Build you own fruit smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
