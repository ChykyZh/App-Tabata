import streamlit as st
from exercises import exercise_manager
from timer import run_timer
from database import save_session, get_sessions
from database import get_exercises

st.set_page_config(page_title="App Tabarca", layout="centered")

st.title("🏋️ App Tabarca — Entrenamientos estilo Tabata")

menu = st.sidebar.selectbox("Menú", ["Cronómetro", "Ejercicios", "Historial"])

# --- Cronómetro ---
if menu == "Cronómetro":
    st.header("Entrenamiento")

    ejercicios = get_exercises()
    if not ejercicios:
        st.info("Primero crea ejercicios desde la sección 'Ejercicios'")
    else:
        nombres = [e["name"] for e in ejercicios]
        seleccionado = st.selectbox("Elige ejercicio", nombres)
        
        e = next(x for x in ejercicios if x["name"] == seleccionado)

        st.write(f"Trabajo: {e['work_time']}s — Descanso: {e['rest_time']}s — Rondas: {e['rounds']}")

        if st.button("Iniciar entrenamiento"):
            run_timer(e["work_time"], e["rest_time"], e["rounds"])
            save_session(
                e["name"],
                (e["work_time"] + e["rest_time"]) * e["rounds"],
                e["rounds"],
                notes="Auto-guardado"
            )

# --- Ejercicios ---
elif menu == "Ejercicios":
    exercise_manager()

# --- Historial ---
elif menu == "Historial":
    st.header("Historial de sesiones")
    data = get_sessions()

    if data:
        for s in data:
            st.write(f"- **{s['datetime']}** — {s['exercise']} — {s['duration']}s — {s['rounds']} rondas — {s.get('notes','')}")
    else:
        st.write("Aún no hay sesiones registradas.")
