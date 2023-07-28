import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock

class PongBall(Widget):
    # Define las propiedades de la pelota
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # Actualiza la posición de la pelota en cada frame
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongPaddle(Widget):
    # Define las propiedades de las paletas
    score = NumericProperty(0)

    # Mueve la paleta en función del tiempo transcurrido
    def move(self, touch):
        if self.collide_point(*touch.pos):
            self.center_y = touch.y

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    # Inicializa el juego
    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    # Actualiza el estado del juego
    def update(self, dt):
        self.ball.move()

        # Comprueba la colisión con las paletas
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # Comprueba la colisión con los bordes superior e inferior
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # Comprueba la colisión con
    # los bordes laterales
        if (self.ball.x < 0) or (self.ball.right > self.width):
            if self.ball.velocity_x > 0:
                self.player1.score += 1
        else:
            self.player2.score += 1
            self.ball.velocity_x *= -1
            self.ball.center = self.center

# Reinicia el juego
def serve_ball(self, vel=(4, 0)):
    self.ball.center = self.center
    self.ball.velocity = vel

# Maneja la entrada de teclado
def on_touch_move(self, touch):
    if touch.x < self.width / 3:
        self.player1.move(touch)
    elif touch.x > self.width - self.width / 3:
        self.player2.move(touch)

