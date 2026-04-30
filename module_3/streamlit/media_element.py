import streamlit as st
st.title("Input your file ",anchor=False)
st.divider()

st.image("image/photo_6296356717058526627_y.jpg")

st.divider()
image=st.file_uploader("Enter your image", type=["jpg","jpeg","png"],
                        accept_multiple_files=True)
print(type(image))
if image:
    col=st.columns(len(image))
    for i,img in enumerate(image):
        with col[i]:
            st.image(img)