#####################################
# hotbar slot 2: fire veil          #
# hotbar slot 5: fishing rod        #
# hotbar slot 6: sword with looting #
#####################################

# (get looting 4 as it's really cheap on bazaar)

import time
import random
import threading
from minescript import *


def _fish_nearby():
    for ent in entities(max_distance=50):
        if "!!!" in ent.name:
            return True
    return False


current_worms = 0


def listen_for_worms():
    with EventQueue() as event_queue:
        event_queue.register_chat_listener()
        while True:
            global current_worms
            event = event_queue.get()
            if event.type == EventType.CHAT and "A Flaming Worm surfaces from the depths!" in event.message:
                current_worms += 1
                echo(f"Worms caught: {current_worms}")


# Start event listener in background thread
listener_thread = threading.Thread(target=listen_for_worms, daemon=True)
listener_thread.start()

while True:
    # when 20 worms caught, switch to fire veil and clear worms
    if current_worms >= 20:
        time.sleep(random.uniform(0.0, 0.3))

        press_key_bind("key.hotbar.2", True)
        press_key_bind("key.hotbar.2", False)

        player_press_use(True)
        player_press_use(False)

        time.sleep(random.uniform(0.1, 0.25))
        # switch to a weapon with LOOTING (sword swap for more loot basically)
        press_key_bind("key.hotbar.6", True)
        press_key_bind("key.hotbar.6", False)

        time.sleep(random.uniform(2.1, 3.1))

        # back to fishing
        press_key_bind("key.hotbar.5", True)
        press_key_bind("key.hotbar.5", False)


        time.sleep(random.uniform(0.05, 0.15))
        player_press_use(True)
        player_press_use(False)

        current_worms = 0

    if _fish_nearby():
        wait_seconds = random.uniform(0.05, 0.3)
        time.sleep(wait_seconds)
        player_press_use(True)
        player_press_use(False)
        time.sleep(random.uniform(0.4, 0.7))
        player_press_use(True)
        player_press_use(False)
    else:
        time.sleep(0.05)