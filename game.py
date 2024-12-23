import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = (pygame.display.get_window_size()[1] - self.left) // self.width

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        color = ["#000000", "#facecc"]
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(
                    screen, color[1],
                    (x * self.cell_size + self.left, y * self.cell_size + self.left,
                     self.cell_size, self.cell_size), 1
                )

    def get_cell(self, mouse_pos):
        print(mouse_pos)
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if (0 <= cell_x <= self.width and 0 <= cell_y <= self.height):
            return cell_x, cell_y


    def on_click(self, cell_coords):
        print(cell_coords)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    fps = 60

    SIZE = width, height = 400, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Клечатое поле")
    board = Board(10, 10)
    board.set_view(0, 0, 40)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.get_click(event.pos)

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
pygame.quit()
