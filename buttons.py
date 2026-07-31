from gpiozero import Button


class Buttons:

    def __init__(self, controller):

        self.controller = controller

        self.amarelo = Button(26)
        self.verde = Button(16)
        self.vermelho = Button(21)
        self.azul = Button(20)

        self.amarelo.when_pressed = lambda: self.controller.button_pressed("Amarelo")
        self.amarelo.when_released = lambda: self.controller.button_released("Amarelo")

        self.verde.when_pressed = lambda: self.controller.button_pressed("Verde")
        self.verde.when_released = lambda: self.controller.button_released("Verde")

        self.vermelho.when_pressed = lambda: self.controller.button_pressed("Vermelho")
        self.vermelho.when_released = lambda: self.controller.button_released("Vermelho")

        self.azul.when_pressed = lambda: self.controller.button_pressed("Azul")
        self.azul.when_released = lambda: self.controller.button_released("Azul")

    def close(self):
        self.amarelo.close()
        self.verde.close()
        self.vermelho.close()
        self.azul.close()
