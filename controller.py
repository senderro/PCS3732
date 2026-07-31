class Controller:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = False

    #############################
    # Botões
    #############################

    def button_pressed(self, nome):
        print(f"[BUTTON] {nome} pressionado")

    def button_released(self, nome):
        print(f"[BUTTON] {nome} liberado")

    #############################
    # Joystick
    #############################

    def joystick_changed(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

        print(f"[JOYSTICK] X={x}  Y={y}  Z={z}")
