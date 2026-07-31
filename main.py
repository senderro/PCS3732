from signal import pause

from controller import Controller
from buttons import Buttons
from joystick import Joystick


def main():

    controller = Controller()

    buttons = Buttons(controller)

    joystick = Joystick(controller)

    print("Sistema iniciado.")

    try:
        pause()

    except KeyboardInterrupt:
        print("Encerrando...")

    finally:
        joystick.close()
        buttons.close()


if __name__ == "__main__":
    main()
