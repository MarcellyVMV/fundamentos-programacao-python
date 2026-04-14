# 1. Defina uma função que calcule a área de um retângulo dados seus dois lados.
def area_rectangle(base, height):
    """
    Calcula a área de um retângulo a partir da base e da altura.

    Parameters:
    base (float): Base do retângulo
    height (float): Altura do retângulo

    Returns:
    area_rectangle (float): Área do retângulo
    """
    area_rectangle = base * height
    return area_rectangle


# 2. Defina uma função que calcule a área da superfície de um cubo que tem c por aresta.
def area_cube(edge):
    """
    Calcula a área de um cubo a partir da medida da aresta.

    Parameters:
    edge (float): Aresta do cubo

    Returns:
    area_cube (float): Área do cubo
    """
    area_cube = 6 * edge**2
    return area_cube


# 3. Defina uma função que calcule a área da coroa circular (anel) formada por dois círculos de raios r1 e r2 (r1 > r2 e P i = 3.14).
import math


def area_circle(radius):
    """
    Calcula a área de um círculo a partir do raio.

    Parameters:
    radius (float): Raio do círculo

    Returns:
    area_circle (float): Área do círculo
    """
    area_circle = math.pi * radius**2
    return area_circle


def area_anel(inner_radius, outer_radius):
    """
    Calcula a área de um anel a partir dos raios internos e externos.

    Parameters:
    inner_radius (float): Raio interno do anel
    outer_radius (float): Raio externo do anel

    Returns:
    area_anel (float): Área do anel
    """
    area_anel = area_circle(inner_radius) - area_circle(outer_radius)
    return area_anel


# test
print("\n\033[1mTest Geometria\033[0m")

print("\nÁrea retângulo (5, 7) =", area_rectangle(5, 7))  # 35
print("Área retângulo (15, 2) =", area_rectangle(15, 2))  # 30
print("Área retângulo (500, 700) =", area_rectangle(500, 700))  # 350000
print("Área retângulo (5, 0) =", area_rectangle(5, 0))  # 0

print("\nÁrea cubo (5) =", area_cube(5))  # 150
print("Área cubo (7) =", area_cube(7))  # 294

print("\nÁrea anel (2, 1) =", area_anel(2, 1))  # 9.42
print("Área anel (15, 5) =", area_anel(15, 5))  # 628.32
print("Área anel (100, 0) =", area_anel(100, 0))  # 31415.93
