from supabase_config import supabase
from datetime import datetime

# Guarda una sesión completa de entrenamiento
def save_session(exercise, duration, rounds, notes=""):
    data = {
        "datetime": datetime.now().isoformat(),
        "exercise": exercise,
        "duration": duration,
        "rounds": rounds,
        "notes": notes
    }
    supabase.table("sessions").insert(data).execute()


# Guarda un ejercicio definido por el usuario
def save_exercise(name, work_time, rest_time, rounds):
    data = {
        "name": name,
        "work_time": work_time,
        "rest_time": rest_time,
        "rounds": rounds,
    }
    supabase.table("exercises").insert(data).execute()


# Obtiene todos los ejercicios creados
def get_exercises():
    r = supabase.table("exercises").select("*").execute()
    return r.data


# Obtiene todas las sesiones registradas
def get_sessions():
    r = supabase.table("sessions").select("*").order("datetime", desc=True).execute()
    return r.data
