from datetime import datetime
import json
import os

class Logger:
    @staticmethod
    def log(mensaje):
        archivo = open("Logs/log.log", "a")
        archivo.write("["+str(datetime.now())+"] "+mensaje+"\n")
        archivo.close()

    @staticmethod
    def cargar_md_users():
        if not os.path.exists("data/md_users.json"):
            return {}

        with open("data/md_users.json", "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def guardar_md_users(md_users):
        with open("data/md_users.json", "w", encoding="utf-8") as f:
            json.dump(md_users, f, indent=4, ensure_ascii=False)
        