import random
import sys
from threading import Thread, RLock
import time

lock = RLock()


class Afficheur(Thread):

    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 5:
            with lock:
                for lettre in self.mot:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)
            i += 1

mon_affiche_a = Afficheur('con')
mon_affiche_b = Afficheur('MALIN')
mon_affiche_a.start()
mon_affiche_b.start()


mon_affiche_a.join()
mon_affiche_b.join()


