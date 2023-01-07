import pygame

const = b"RIFF\x1a\x00\x00\x00WEBPVP8L\r\x00\x00\x00/\x00\x00\x00\x10\x07\x10\x11\x11\x88\x88\xfe\x07\x00"
surf = pygame.image.frombytes(const, (600, 600), "RGBA")

screen = pygame.display.set_mode((500, 500))

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            raise SystemExit

    screen.blit(surf, (50, 50))
    pygame.display.update()
