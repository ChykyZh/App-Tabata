from supabase import create_client
import os

# REEMPLAZA ESTO POR TUS DATOS
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://iylhojwxufkrazvrvkgg.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "sb_publishable_PIpBeoQR_huOMwXxwdg_7A_2kfkMoty")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
