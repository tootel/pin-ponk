from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed



back = (200, 255, 255)
win_height = 500
win_width = 600
window = display.set_mode((win_width, win_height))
window.fill(back)
Tru = True
finish = False
FPS = 60
clock = time.Clock()
speed_x, speed_y = 3,3
ball = GameSprite('ball.png', 200, 200, 50, 50, 4)
raket1 = Player('raket.png', 30, 200, 50, 150, 4)
raket2 = Player('raket.png', 520, 200, 50, 150, 4)

while Tru:
    for e in event.get():
        if e.type == QUIT:
            Tru = False
    if finish != True:
        raket1.update_l()
        raket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(raket1, ball) or sprite.collide_rect(raket2, ball):
           speed_x *= -1
           speed_y *= 1  
        if ball.rect.x < 0 or ball.rect.x > win_width:
            finish = True
        raket1.reset()
        raket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)                   
