import streamlit as st
st.title("simple calculator",anchor=False)
num1 = st.number_input("Enter first number",value=None,placeholder="Type your first number here")
num2 = st.number_input("Enter second number",value=None,placeholder="Type your second number here")
operation = st.selectbox("Choose an operation",("+","-","*","/"),index=None)
pressed=st.button("Calculate",type="primary")

if pressed:
    if operation=="+":
        st.write("The sum is ",num1+num2)
    elif operation=="-":
        st.write("The difference is ",num1-num2)
    elif operation=="*":
        st.write("The product is ",num1*num2)
    elif operation=="/":
        if num2!=0:
            st.write("The quotient is ",num1/num2)
        else:
            st.write("Error: Division by zero is not allowed.")