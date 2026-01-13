from datetime import datetime
import json
import os
from enum import Enum

class NivelLog(Enum):
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    DEBUG = "DEBUG"

class Logger:

    @staticmethod
    def log(nivelLOG, parte_sistema, suceso, causante):
        nivel = nivelLOG.value
        with open("Logs/log.log", "a") as archivo:
            archivo.write(f"[{str(datetime.now())}]") # timestamp
            archivo.write(f" | {nivel}") # gravedad - nivel
            archivo.write(f" | {parte_sistema}") # parte - modulo
            archivo.write(f" | {suceso}") # contexto
            if not (causante is None):
                archivo.write(f" | USADO POR: {causante}")
            archivo.write("\n")


    @staticmethod
    def cargar_md_users():
        usuarios = {}
        with open("Logs/users.log","r") as archivo:
            for linea in archivo:
                partes = linea.split(',')
                usuarios[partes[0]] = partes[1] # key = nombre, value = id

        return usuarios

    @staticmethod
    def guardar_md_users(md_user): # tomamos md_user como lista que contiene en pos0 el nombre y en pos 1 el id
        with open("Logs/users.log","r+") as archivo:
            for linea in archivo:
                if md_user[1] in linea:
                    return
 
            archivo.write(md_user[0] + "," + md_user[1] + "\n")