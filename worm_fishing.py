#####################################
# hotbar slot 2: fire veil          #
# hotbar slot 5: fishing rod        #
# hotbar slot 6: sword with looting #
#####################################

# (get looting 4 as it's really cheap on bazaar)

import time
import random
import minescript


def _fish_nearby():
    for ent in minescript.entities(max_distance=50):
        if "!!!" in ent.name:
            return True
    return False


last_item_time = time.time()

BASE_ITEM_INTERVAL = 80

while True:
    now = time.time()
    # every 80 seconds switch to fire veil and clear worms
    if now - last_item_time >= BASE_ITEM_INTERVAL + random.uniform(-5, 5):
        time.sleep(random.uniform(0.0, 0.3))

        minescript.press_key_bind("key.hotbar.2", True)
        minescript.press_key_bind("key.hotbar.2", False)

        minescript.player_press_use(True)
        minescript.player_press_use(False)

        time.sleep(random.uniform(0.2, 0.5))
        # switch to a weapon with LOOTING (sword swap for more loot basically)
        minescript.press_key_bind("key.hotbar.6", True)
        minescript.press_key_bind("key.hotbar.6", False)

        time.sleep(random.uniform(2.1, 3.1))

        # back to fishing
        minescript.press_key_bind("key.hotbar.5", True)
        minescript.press_key_bind("key.hotbar.5", False)


        time.sleep(random.uniform(0.05, 0.15))
        minescript.player_press_use(True)
        minescript.player_press_use(False)

        last_item_time = now

    if _fish_nearby():
        wait_seconds = random.uniform(0.05, 0.3)
        time.sleep(wait_seconds)
        minescript.player_press_use(True)
        minescript.player_press_use(False)
        time.sleep(random.uniform(0.4, 0.7))
        minescript.player_press_use(True)
        minescript.player_press_use(False)
    else:
        time.sleep(0.05)