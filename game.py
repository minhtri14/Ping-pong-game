from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, width, height, speed=0):
        super().__init__()
        self.image = image.load(filename)
        self.image = transform.scale(self.image, (width, height))
        self.rect = Rect(x, y, width, height)
        self.speed = speed
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
    
class Player(GameSprite):
    def update(self):
        Key = key.get_pressed()
        if Key[K_w]:
            self.rect.x += self.speed 
        if Key[K_s]:
            self.rect.x -= self.speed

_WIDTH = 800
_HEIGHT = 640

window = display.set_mode((_WIDTH, _HEIGHT))
clock = time.Clock()

ball = GameSprite('ball.png', 500, 300, 60, 80, 5)
paddle = Player('Paddle.png', _WIDTH/2, _HEIGHT-95, 60, 80, 4.5)
