import streamlit as st
st.title("Input your information ",anchor=False)
st.divider()
name = st.text_input("Enter your name",placeholder="Type your name here")
#st.write("your name is ",name)
st.divider()
age = st.number_input("Enter your age",value=None,placeholder="Enter your age here")
#st.write("your age is ",age)


profession = st.selectbox("Choose your profession",("Student","Teacher","Engineer","Doctor","Other")
                          ,index=None,accept_new_options=True)

pressed=st.button("Enter to confirm",type="primary")
if pressed:
    st.write("Your name is ",name)
    st.write(" and your age is ",age)
    st.write(" and your profession is ",profession)



# st.divider()
# password = st.text_input("Enter your password",type="password",placeholder="Type your password here")
# st.write("your password is ",password)