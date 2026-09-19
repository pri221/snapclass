from src.screen.database.config import supabase
import bcrypt

def hash_pass(pwd: str) -> bool:
    return bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_pass(pwd: str,hashed: str) -> bool:
    return bcrypt.checkpw(pwd.encode('utf-8'), hashed.encode('utf-8'))

def check_teacher_exists(username: str) -> bool:
    username = username.strip() if username else ""
    if not username:
        return False
    #check for unique username, return false when username id already taken
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data)>0


def create_teacher(username: str, password: str, name: str) -> bool:

    data = {"username" : username, "password": hash_pass(password), "name":name}
    response = supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username: str, password: str) -> bool:
    clean_username = username.strip() if username else ""
    if not clean_username:
        return None
    response = supabase.table("teachers").select("*").eq("username",clean_username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher['password']):
            return teacher
    return None

def get_all_students():
    response = supabase.table('student').select("*").execute()
    return response.data