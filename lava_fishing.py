import time
import random
import minescript


def _fish_nearby():
    for ent in minescript.entities(max_distance=50):
        if "!!!" in ent.name:
            return True
    return False

fished = False

while True:
    if fished:
        time.sleep(random.uniform(0.0, 0.3))

        minescript.press_key_bind("key.hotbar.2", True)
        minescript.press_key_bind("key.hotbar.2", False)

        minescript.player_press_use(True)
        minescript.player_press_use(False)

        time.sleep(random.uniform(0.1, 0.4))

        minescript.press_key_bind("key.hotbar.1", True)
        minescript.press_key_bind("key.hotbar.1", False)

        minescript.player_press_use(True)
        minescript.player_press_use(False)

        time.sleep(random.uniform(0.1, 0.3))

        # back to fishing
        minescript.press_key_bind("key.hotbar.5", True)
        minescript.press_key_bind("key.hotbar.5", False)


        time.sleep(random.uniform(0.05, 0.15))
        minescript.player_press_use(True)
        minescript.player_press_use(False)
        fished = False

    elif _fish_nearby():
        wait_seconds = random.uniform(0.05, 0.3)
        time.sleep(wait_seconds)
        minescript.player_press_use(True)
        minescript.player_press_use(False)
        fished = True
    else:
        time.sleep(0.05)