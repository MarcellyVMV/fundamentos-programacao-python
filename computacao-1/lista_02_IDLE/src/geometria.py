import math


# 4. (a) uma função que calcule a distância entre dois pontos em um plano dadas suas coordenadas.
def distancia_2pontos(x1, y1, x2, y2):
    """
    Calcula a distância entre dois pontos em um plano dadas suas coordenadas.

    Parameters:
    x1 (float): Primeira coordenada x
    y1 (float): Primeira coordenada y
    x2 (float): Segunda coordenada x
    y2 (float): Segunda coordenada y

    Returns:
    distancia (float): Distância entre os dois pontos
    """
    distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distancia


# 4. (b) uma função que calcule o perímetro de um triângulo reto dados os catetos.
def hipotenusa(c1, c2):
    """
    Calcula a hipotenusa de um triângulo reto dados os catetos.

    Parameters:
    c1 (float): Primeiro cateto
    c2 (float): Segundo cateto

    Returns:
    hipo (float): Hipotenusa
    """
    hipo = math.sqrt((c1**2) + (c2**2))
    return hipo


def perimetro_triangulo(c1, c2):
    """
    Calcula o perímetro de um triângulo reto dados os catetos.

    Parameters:
    c1 (float): Primeiro cateto
    c2 (float): Segundo cateto

    Returns:
    perimetro (float): Perímetro
    """
    perimetro = c1 + c2 + hipotenusa(c1, c2)
    return perimetro


# 4. (c) uma função que calcule a soma do quadrado do seno com o quadrado do cosseno de um ângulo.
def soma_pow2_SinCos(theta):
    """
    Calcula a soma do quadrado do seno com o quadrado do cosseno de um ângulo.

    Parameters:
    theta (float): Ângulo em graus

    Returns:
    soma (float): Soma do quadrado do seno com o quadrado do cosseno
    """
    theta_rad = math.radians(theta)
    soma = (math.sin(theta_rad) ** 2) + (math.cos(theta_rad) ** 2)
    return soma


# 5. Escreva uma função que calcule a área de um setor circular, dados o raio e o ângulo. Use um argumento default para o ângulo, de modo que se nenhum ângulo for informado, a função retorne a área do círculo inteiro.
def area_setor_circular(r, theta=360):
    """
    Calcula a área de um setor circular, dados o raio e o ângulo.

    Parameters:
    r (float): Raio
    theta (float): Ângulo em graus

    Returns:
    area (float): Área do setor circular
    """
    area = (r**2) * (theta / 360) * math.pi
    return area


# test
print("\n\033[1mTest Geometria\033[0m")

print("\nDistância (0,0) → (3,4) =", distancia_2pontos(0, 0, 3, 4))  # 5
print("Distância (1,1) → (1,1) =", distancia_2pontos(1, 1, 1, 1))  # 0
print("Distância (-1,-1) → (2,3) =", distancia_2pontos(-1, -1, 2, 3))  # 5

print("\nHipotenusa (3,4) =", hipotenusa(3, 4))  # 5
print("Perímetro (3,4) =", perimetro_triangulo(3, 4))  # 12
print("Perímetro (5,12) =", perimetro_triangulo(5, 12))  # 30

print("\nsin² + cos² (0º) =", soma_pow2_SinCos(0))  # 1
print("sin² + cos² (90º) =", soma_pow2_SinCos(90))  # 1
print("sin² + cos² (55º) =", soma_pow2_SinCos(55))  # 1

print("\nÁrea setor (r=1, θ=360) =", area_setor_circular(1))  # π ≈ 3.14
print("Área setor (r=1, θ=180) =", area_setor_circular(1, 180))  # π/2 ≈ 1.57
print("Área setor (r=2, θ=90) =", area_setor_circular(2, 90))  # π ≈ 3.14
