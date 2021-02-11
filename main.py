import pygame
import pygame_gui
from Map import Map

if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption('')
    width, height = 610, 660
    size = width, height
    manager = pygame_gui.UIManager(size)

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    fps = 60
    dt = 0
    yamap = Map(screen, manager, width, height)
    yamap.init_ui()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    yamap.update_change_map(event.text)
            if event.type == pygame.QUIT:
                running = False
            manager.process_events(event)
            yamap.on_event(event)
        dt = clock.tick(fps)
        manager.update(dt)
        screen.fill('#6699FF')
        yamap.draw()
        manager.draw_ui(screen)
        pygame.display.flip()
    pygame.quit()
