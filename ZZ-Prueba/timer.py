import streamlit as st
import time

def run_timer(work_time, rest_time, rounds):
    st.header("Cronómetro")

    if "running" not in st.session_state:
        st.session_state.running = False
        st.session_state.phase = "work"
        st.session_state.current_round = 1
        st.session_state.time_left = work_time

    start_button = st.button("▶ Empezar")
    stop_button = st.button("⏹ Parar / Reiniciar")

    if start_button:
        st.session_state.running = True

    if stop_button:
        st.session_state.running = False
        st.session_state.phase = "work"
        st.session_state.current_round = 1
        st.session_state.time_left = work_time

    # Bucle temporal controlado
    placeholder = st.empty()

    while st.session_state.running:
        with placeholder.container():
            st.subheader(f"Ronda {st.session_state.current_round}/{rounds}")
            st.write(f"Fase: **{st.session_state.phase}**")
            st.write(f"Tiempo restante: **{st.session_state.time_left} s**")

        time.sleep(1)
        st.session_state.time_left -= 1

        # Cuando termina fase
        if st.session_state.time_left <= 0:
            if st.session_state.phase == "work":
                # cambia a descanso
                st.session_state.phase = "rest"
                st.session_state.time_left = rest_time
            else:
                # pasa a siguiente ronda
                st.session_state.current_round += 1
                if st.session_state.current_round > rounds:
                    st.session_state.running = False
                    st.success("Entrenamiento completado")
                    break
                st.session_state.phase = "work"
                st.session_state.time_left = work_time

        # Obligatorio refrescar Streamlit
        st.experimental_rerun()
