import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        
        for num in range(1, 6):
            img = pygame.image.load(f"assets/explosion/exp{num}.png")
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        
        self.index = 0
        self.current_image = self.images[self.index]
        self.rect = self.current_image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0
    def update(self):
        animation_speed = 4
        
        self.counter += 1
        
        if self.counter >= animation_speed and self.index > len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.current_image = self.images[self.index]
            
        if self.index >= len (self.images) - 1 and self.counter >= animation_speed:
            self.kill()
