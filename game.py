from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, width, height, speed=(0, 0)):
        super().__init__()
        self.image = image.load(filename)
        self.image = transform.scale(self.image, (width, height))
        self.rect = Rect(x, y, width, height)
        self.speed = Vector2(speed)
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class RectSprite(sprite.Sprite):
    def __init__(self, color, x, y, height, width, speed = 0):
        super().__init__()
        self.image = Surface((width, height))
        self.image = fill(color)
        self.rect = Rect(x, y, width, height)
        self.speed = speed()
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
    
class Ball(GameSprite):
    def update(self):
        if self.rect.bottom >= _HEIGHT or self.rect.top <= 0:
            self.speed.y *= -1

        self.rect.topleft += self.speed

class Player1(GameSprite):
    def update(self):
        Key = key.get_pressed()
        if Key[K_i]:
            self.rect.y -= self.speed.y
        if Key[K_k]:
            self.rect.y += self.speed.y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > _HEIGHT:
            self.rect.bottom = _HEIGHT
class Player2(GameSprite):
    def update(self):
        Key = key.get_pressed()
        if Key[K_w]:
            self.rect.y -= self.speed.y
        if Key[K_s]:
            self.rect.y += self.speed.y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > _HEIGHT:
            self.rect.bottom = _HEIGHT
_WIDTH = 800
_HEIGHT = 640

window = display.set_mode((_WIDTH, _HEIGHT))
clock = time.Clock()

bg = GameSprite('TTTable.png', 0, 0, _WIDTH, _HEIGHT)
ball = Ball('ball.png', 390, 290, 60, 80, (6, 4))
P1 = Player1('paddleblack.png', _WIDTH-100, _HEIGHT/2, 120, 125, 6)
P2 = Player2('paddlered.png', _WIDTH-770, _HEIGHT/2, 125, 120, 6) 
font.init()
f = font.SysFont('Arial', 70)
game_is_running = True
while game_is_running:
    for e in event.get():
        if e.type == QUIT:
            game_is_running = False
    window.fill((210, 222, 255))
    bg.update()
    bg.draw(window)

    if sprite.collide_rect(ball, P1) or sprite.collide_rect(ball, P2):
        ball.speed.x *=-1
    if ball.rect.left < 0:
        winner2_text = f.render("Player 2 win", True, (229, 0, 0))
        window.blit(winner2_text, (220, 280))
    if ball.rect.right > _WIDTH:
        winner2_text = f.render("Player 1 win", True, (229, 0, 0))
        window.blit(winner2_text, (220, 280))
    ball.update()
    P1.update()
    P2.update()

    ball.draw(window)
    P1.draw(window)
    P2.draw(window)

    display.update()
    clock.tick(60)