import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
rect(screen, (255, 255, 255), (0, 0, 400, 400))


def draw_body(screen, x, y, size, color, circuit_color):
    """
    Функция рисует туловище смайлика
    :param screen: объект pygame.Surface
    :param x: координата центра вдоль оси х
    :param y: координата центра вдоль оси у
    :param size: размер туловища, задается радиусом
    :param color: цвет туловища
    :param circuit_color: цвет контура
    :return: изображение туловища
    """
    circuit_width = 2
    circle(screen, color, (x, y), size)
    circle(screen, circuit_color, (x, y), size, circuit_width)


def draw_eyes(screen, x, y, distance, size, pupil_size, color, pupil_color, eyebrow_size, eyebrow_thickness,
              eyebrow_color):
    """
    Функция рисует глаза смайлика
    :param screen: объект pygame.Surface
    :param x: координата вдоль оси х
    :param y: координата вдоль оси у
    :param distance: расстояние между глаз
    :param size: размер глаз, задается радиусом
    :param pupil_size: размер зрачков
    :param color: цвет глаза
    :param pupil_color: цвет зрачка
    :param eyebrow_size: размер бровей, величина [2;4]
    :param eyebrow_thickness: толщина бровей
    :param eyebrow_color: цвет бровей
    :return: изображение глаз
    """
    circuit_width = 2
    circle(screen, color, (x + distance // 2, y), size)
    circle(screen, pupil_color, (x + distance // 2, y), size, circuit_width)
    circle(screen, pupil_color, (x + distance // 2, y), pupil_size)
    circle(screen, color, (x - distance // 2, y), size)
    circle(screen, pupil_color, (x - distance // 2, y), size, circuit_width)
    circle(screen, pupil_color, (x - distance // 2, y), pupil_size)
    line(screen, eyebrow_color, (x - distance // 2 + size, y - size // 2),
         (x - distance // 2 - int(size*eyebrow_size), y - size - int((size // 2)*eyebrow_size)), eyebrow_thickness)
    line(screen, eyebrow_color, (x + distance // 2 - size, y - size // 1.3),
         (x + distance // 2 + int(size*eyebrow_size*0.8), y - size - int((size - size // 1.3)*eyebrow_size*0.6)),
         eyebrow_thickness)


def draw_mouth(screen, x, y, width, thickness, color):
    """
    Функция рисует рот смайлика
    :param screen: объект pygame.Surface
    :param x: координата х, центра рта
    :param y: кооржината у, центра рта
    :param width: ширина
    :param thickness: толщина рта
    :param color: цвет рта
    :return: изображение рта
    """
    rect(screen, color, (x - width // 2, y - thickness // 2, width, thickness))


def draw_emoji(screen, x, y, size):
    """
    Функция рисует злой смайлик на экране
    :param screen: объект pygame.Surface
    :param x: координата центра вдоль оси х
    :param y: координата центра вдоль оси у
    :param size: размер изображения, описываемый радиусом окружности
    :return: изображение смайлика
    """
    body_x = x
    body_y = y
    body_size = size
    body_color = (255, 255, 0) # Цвет задан как в задании
    body_circuit_color = (0, 0, 0) # Цвет задан как в задании
    draw_body(screen, body_x, body_y, body_size, body_color, body_circuit_color) # Рисуем туловище

    eyes_x = x
    eyes_y = y - size // 3
    eyes_distance = size // 1.2
    eyes_size = size // 4
    eyes_pupil_size = eyes_size / 2
    eyes_color = (255, 0, 0) # Цвет задан как в задании
    eyes_pupil_color = (0, 0, 0) # Цвет задан как в задании
    eyes_eyebrow_size = 2
    eyes_eyebrow_thickness = size // 20
    eyes_eyebrow_color = (0, 0, 0) # Цвет задан как в задании
    draw_eyes(screen, eyes_x, eyes_y, eyes_distance, eyes_size, eyes_pupil_size,
              eyes_color, eyes_pupil_color, eyes_eyebrow_size, eyes_eyebrow_thickness, eyes_eyebrow_color)

    mouth_x = x
    mouth_y = y + size // 2
    mouth_width = size
    mouth_thickness = size // 10
    mouth_color = (0, 0, 0) # Цвет задан как в задании
    draw_mouth(screen, mouth_x, mouth_y, mouth_width, mouth_thickness, mouth_color)


x, y, size = 250, 150, 100
draw_emoji(screen, x, y, 100)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
