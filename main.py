import streamlit as st
st.title("welcome to my first web page on streamlit")
#to add text
st.write(
""" # Hi all,
here you learn diffrent techonologies related to computer science field
""")
#select a text box for widgets
#st.selectbox("select course",("IoT","Machine Learning","Deep Learning","Python"))

# also you can assign this to a variable like
#coursename =st.selectbox("select course",("IoT","Machine Learning","Deep Learning","Python"))

#how to print a same using variable name
st.write("coursename")

#streamlit cache things which will help to run the application faster

# if you want to move the widgets to a sidebar then
coursename =st.sidebar.selectbox("select course",("CSE","Interview Question","Deep Learning","Python"))
csecoursename =st.sidebar.selectbox("select CSE course",("IoT","Machine Learning","Deep Learning","Python"))

img = st.file_uploader("upload a file")
st.image(img)

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')