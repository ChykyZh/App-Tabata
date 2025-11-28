import streamlit as st

st.set_page_config(
    page_title='Workout!', 
    page_icon="💪🏻",
    layout="centered",
    initial_sidebar_state='expanded'
)

#Titulo
st.title('💪🏻 Workout!')
st.divider()

c_progres = st.container(border=True, width='stretch', horizontal_alignment='center')
progres = st.container()

c_rutines = st.container()
rutines = st.container()

with c_progres:
    st.header("Progress")

with c_rutines:
    st.header('Rutinas')
