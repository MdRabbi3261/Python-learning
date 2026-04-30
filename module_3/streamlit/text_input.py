import streamlit as st
st.title("my first streamlit web app",anchor=False,width=400)
st.header("This is a header",divider=True)
st.subheader("This is a subheader")
st.text("This is a text")
#st.write("This is a text input example.")
st.markdown("**:red[This is a]:green[ markdown]** *:yellow[text.]*")

a=10
b=20
st.write(a,b)