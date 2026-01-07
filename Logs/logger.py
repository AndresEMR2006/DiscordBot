from datetime import datetime

class Logger:
    @staticmethod
    def log(mensaje):
        archivo = open("Logs/log.log", "a")
        archivo.write("["+str(datetime.now())+"] "+mensaje+"\n")
        archivo.close()