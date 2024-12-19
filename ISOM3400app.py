import streamlit as st
import pandas as pd
import numpy as np
st.title("Welcome to my website .w.") #Main title
#_____________________________________________________________
st.header("This is a header") #Header 
#_____________________________________________________________
st.subheader("This is a subheader") #Subheader
#_____________________________________________________________

st.write("I am so handsome")

list1 = [1,2,3,4]

st.text(list1)
st.write(list1) ## 'st.write() will display in the corresponding data type while 'st.text()' will only display in text form

#_____________________________________________________________

st.divider() # divider

#_____________________________________________________________

st.markdown("## This is the second content") 
# st.markdown 可以用來表示不同的format而不需要使用不同的commmand
# ‘#’一個井號是title ， ‘##’兩個是header ，‘###’三個是subheader
# ‘**文字**’ / ‘__文字__' 是bold ， ‘*文字*’/ '_文字_' 是斜體
# ‘___' / '***' 是分割線

#_____________________________________________________________

code = '''print('I am so handsome')
def haha():
    print("Messi is goat")
'''
st.code(code, language='python')

#_____________________________________________________________

st.caption('The above is a python code')
#說明
st.divider()

#_____________________________________________________________

# Create a sample dataframe with random data
data = pd.DataFrame({
    'x': range(1, 11),
    'y': np.random.randn(10)
})

# Display the line chart
st.line_chart(data.set_index('x'))

#_____________________________________________________________

# Create a slider for selecting a number between 1 and 100
selected_number = st.slider("Select a number", 0, 100, 50,10)
#st.slider(label,min_value, max_value, value ,step (optional))

# Display the selected number
st.write(f"You selected: {selected_number}")

#_____________________________________________________________

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
}
df = pd.DataFrame(data)

# Display the DataFrame using st.dataframe()
st.text("Displaying DataFrame:")
st.dataframe(df)

st.divider()

#_____________________________________________________________

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
}
df = pd.DataFrame(data)

# Display the DataFrame as a table using st.table()
st.write("Displaying DataFrame as a table:")
st.table(df)

## st.table() and st.dataframe() basically the same 
# while st.table is quick and simple and st.dataframe can provide users with interactive capabilities

st.divider()
#_____________________________________________________________

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = df[('rating'== df['rating'].max())]
st.markdown(f"Your favorite command is **{favorite_command[command]}** 🎈")

st.divider()
#_____________________________________________________________

# List of options for the select box
options = ['Option 1', 'Option 2', 'Option 3']

# Create a select box for the user to choose an option
selected_option = st.selectbox("Select an option", options)
## st.selectbox(label, options, index=0(optional, preselected option on first render))

# Display the selected option
st.write(f"You selected: {selected_option}")

st.divider()
#_____________________________________________________________

# Create a text input box for the user to enter their name
user_name = st.text_input("Enter your name",'Nick')
#st.text_input(label, value(optional)

# Display a message using the entered name
st.write(f"Hello, {user_name}!")

st.divider()
#_____________________________________________________________

# Create a text area for the user to enter a message
user_message = st.text_area("Enter your message here", "HAHA")
#st.text_area(label, value(optional))

# Display the entered message
st.write(f"Your message: {user_message}")

st.divider()
#_____________________________________________________________

# Create a checkbox for the user to select/unselect an option
option_selected = st.checkbox("Buy")
#st.checkbox(lab, value(optional - default is false = not choose))

if option_selected:
    st.write("BUY!!!!!")
else:
    st.write("Not buy!!!!!")

st.divider()
#_____________________________________________________________

# Display a file uploader widget
uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt", "xlsx"])
#st.file_uploader(label, type(file type))
if uploaded_file is not None:
    # Process the uploaded file
    file_contents = uploaded_file.read()
    st.write("File contents:")
    st.write(file_contents)

st.divider()
#_____________________________________________________________

# Create a button widget
if st.button("Click me"):
    st.write("Button clicked!")

st.divider()
#_____________________________________________________________

with st.form("my_form"):
#st.form(key, clear_on_submit=False(optional))
    # Adding form elements
    name = st.text_input("Enter your name", "John Doe")
    age = st.number_input("Enter your age", min_value=0, max_value=120)
    # st.number_input(label, min_value, max_value, value="min" (default = minimum value))
    submitted = st.form_submit_button()
    #st.form_submit_button(label="submit"(defalut = 'Submit))
    # Processing the form data
    if submitted:
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
