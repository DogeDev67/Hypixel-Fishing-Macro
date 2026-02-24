import time
import random
import minescript


def _fish_nearby():
    for ent in minescript.entities(max_distance=5):
        if "!!!" in ent.name:
            return True
    return False


while True:
    if _fish_nearby():
        wait_seconds = random.uniform(0.05, 0.3)
        time.sleep(wait_seconds)
        minescript.player_press_use(True)
        minescript.player_press_use(False)
        time.sleep(random.uniform(0.4, 0.7))
        minescript.player_press_use(True)
        minescript.player_press_use(False)

    else:
        time.sleep(0.1)