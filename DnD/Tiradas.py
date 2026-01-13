import random
import re

class tiradas():

    def __init__(self):
        self.dados = [4, 6, 8, 10, 12, 20, 100]

    def segmentar(self, dado: str):
        # funcion para segmentar el string del dado
        patron = r'(\d*)d(\d+)([+-]\d+)?'
        coincidencia = re.match(patron, dado)
        if coincidencia:
            num_dados = int(coincidencia.group(1)) if coincidencia.group(1) else 1
            tipo_dado = int(coincidencia.group(2))
            modificador = int(coincidencia.group(3)) if coincidencia.group(3) else 0
            return num_dados, tipo_dado, modificador
        else:
            return None

    def roll(self, tirada: str):

        tiradas = []

        if not ("d" in tirada):
            return {"estado": False, "error":"Formato inválido. Usa NdM, donde N es el número de dados y M el número de caras."}

        segmentacion = self.segmentar(tirada)

        if segmentacion is None:
            return {"estado": False, "error":"Formato inválido. Usa NdM, donde N es el número de dados y M el número de caras."}
        
        if not (segmentacion[1] in self.dados):
            return {"estado": False, "error":f"Tipo de dado inválido. Los tipos permitidos son: {', '.join(map(str, self.dados))}."}
        
        posNat20 = []
        for tiros in range(segmentacion[0]):
            rng = random.randint(1, segmentacion[1])
            if rng == 20 and segmentacion[1] == 20:
                tiradas.append(rng)
                posNat20.append(tiros)
            else:
                tiradas.append(rng+segmentacion[2])

        return {"estado": True, "tiradas": tiradas, "posNat20": posNat20}