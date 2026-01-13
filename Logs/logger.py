from datetime import datetime
import json
import os

class Logger:
    @staticmethod
    def log(mensaje):
        with open("Logs/log.log","a") as archivo:
            archivo.write("["+str(datetime.now())+"] "+mensaje+"\n")

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