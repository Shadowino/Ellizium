import sys
import pygame
import platform
# user library's
from render import *

print(f"""Versions OF:
      Pygame:{pygame.version.ver}
      Python:{sys.version}
      Machine:{platform.machine()
}  System:{platform.system()
} Version:{platform.version()
} Platform:{platform.platform()
} Processor:{platform.processor()
} """
      )

# global variables
do_exit = 0


def doExit():
    """(CORE) function for safe exit from application"""
    global do_exit
    do_exit = 1
    pass


# this should be inside initApp function...
windowedScreen = pygame.display.set_mode((1280, 720))


def initApp() -> int:
    """(CORE) init application"""
    # init to global`s variables....
    # i made it later
    return 0
    pass


# TODO: move all (CORE) functions in CORE.py file
# event-handler function
def keyPressUpdate(event: pygame.event.Event):
    """(CORE) update function for keyboard events."""
    print(f"""
EVENT:\t{event.type}
KEY(id):\t{event.dict['key']}
ASCII:\t{event.dict['unicode']}
Modification:
    SHIFT:{event.dict['mod'] & pygame.KMOD_SHIFT}
    CTRL: {event.dict['mod'] & pygame.KMOD_CTRL}
    ALT:  {event.dict['mod'] & pygame.KMOD_ALT}
""")
    # TODO: made class 'keyEvent' with coder-friendly methods and fields
    # TODO: made function 'keyEventUpdate' (noCORE) for game logic
    pass


def eventUpdate():
    """(CORE) update function for all events. Redirect to other update functions"""
    for eve in pygame.event.get():
        eveType = eve.type
        if eveType == pygame.QUIT:
            doExit()
        elif eveType == pygame.KEYDOWN or eveType == pygame.KEYUP:
            keyPressUpdate(eve)
        elif eveType == pygame.MOUSEMOTION:
            # TODO: make mouseMotionUpdate() function for mouseMotion event
            pass
        elif eveType == pygame.MOUSEBUTTONUP or eveType == pygame.MOUSEBUTTONDOWN:
            # TODO: make mouseButtonUpdate() function for mouseButtonUp(Down) event
            pass
        elif eveType == pygame.VIDEOEXPOSE:  # none
            pass
        elif eveType == pygame.VIDEORESIZE:  # none
            pass
        else:
            # TODO: make more event handler`s
            print(f"event '{pygame.event.event_name(eveType)}' \tID:{eveType}")
        pass
    pass


def main() -> int:
    initApp()
    render(windowedScreen)
    while not do_exit:
        eventUpdate()
    return 0
    pass


if __name__ == "__main__":
    print("main.py is __main__")
    main()
