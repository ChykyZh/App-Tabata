import streamlit as st
from database import save_exercise, get_exercises

def exercise_manager():
    st.header("Gestión de Ejercicios")

    with st.form("form_ejercicio"):
        name = st.text_input("Nombre del ejercicio")
        work = st.number_input("Tiempo de trabajo (seg)", min_value=5, max_value=600)
        rest = st.number_input("Tiempo de descanso (seg)", min_value=0, max_value=600)
        rounds = st.number_input("Rondas", min_value=1, max_value=50)
        
        submitted = st.form_submit_button("Guardar")
        if submitted:
            save_exercise(name, work, rest, rounds)
            st.success("Ejercicio guardado")

    st.subheader("Ejercicios disponibles:")
    ejercicios = get_exercises()
    if ejercicios:
        for e in ejercicios:
            st.write(f"**{e['name']}** — trabajo {e['work_time']}s / descanso {e['rest_time']}s × {e['rounds']} rondas")
    else:
        st.write("Aún no hay ejercicios.")
