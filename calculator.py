import streamlit as st

# Define custom CSS styles
def local_css():
    st.markdown("""
        <style>
        /* Set background color and font color for the entire app */
        .stApp {
            background-color: #1c1c1c; /* Dark background */
            color: #ffffff; /* White text color */
        }
        /* Style the title */
        .css-1e8m4b7 {
            color: #e57373; /* Light red */
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
            text-align: center;
            color: #ffffff; /* White text color */
        }
        /* Style the sidebar */
        .css-1kyxreq {
            background-color: #424242; /* Dark gray background */
            color: #ffffff; /* White text color */
            padding: 20px;
            border-radius: 10px;
        }
        /* Style the selectbox in the sidebar */
        .css-2hb0u5 {
            background-color: #616161; /* Medium gray background */
            color: #ffffff; /* White text color */
            border: 1px solid #e57373; /* Light red border */
            border-radius: 4px;
        }
        /* Style the number inputs */
        .css-1l02f7b {
            background-color: #616161; /* Medium gray background */
            color: #ffffff; /* White text color */
            border: 1px solid #e57373; /* Light red border */
            border-radius: 4px;
            padding: 10px;
            font-size: 18px;
        }
        /* Style the button */
        .css-1v0mbdj {
            background-color: #d32f2f; /* Dark red background */
            color: #ffffff; /* White text color */
            font-size: 18px;
            border-radius: 4px;
            border: none;
            padding: 10px;
        }
        /* Style the result text */
        .css-1f2i6ps {
            font-size: 24px;
            font-weight: bold;
            color: #e57373; /* Light red */
            text-align: center;
            margin-top: 20px;
        }
        /* Add padding to the main content area */
        .css-1y0tads {
            padding: 20px;
            background-color: #1c1c1c; /* Dark background */
            border-radius: 10px;
            color: #ffffff; /* White text color */
        }
        </style>
    """, unsafe_allow_html=True)

def main():
    local_css()  # Apply the custom CSS

    st.title('Simple Calculator')

    # Create a sidebar for the calculator options
    st.sidebar.header('Select Operation')
    operation = st.sidebar.selectbox('Choose operation', ['Addition', 'Subtraction', 'Multiplication', 'Division'])

    # Input fields for numbers
    num1 = st.number_input('Enter first number', format="%f")
    num2 = st.number_input('Enter second number', format="%f")

    # Perform the calculation based on user selection
    result = None
    if operation == 'Addition':
        result = num1 + num2
    elif operation == 'Subtraction':
        result = num1 - num2
    elif operation == 'Multiplication':
        result = num1 * num2
    elif operation == 'Division':
        if num2 != 0:
            result = num1 / num2
        else:
            st.error('Cannot divide by zero')

    # Display the result
    if result is not None:
        st.write(f'The result of {operation.lower()} is: {result}')

if __name__ == "__main__":
    main()
