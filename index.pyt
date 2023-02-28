import turtle

# propriedades do sol
sun_radius = 50
sun_color = "yellow"

# propriedades dos planetas
mercury_radius = 10
mercury_distance = 100
mercury_color = "gray"
venus_radius = 20
venus_distance = 150
venus_color = "orange"
earth_radius = 25
earth_distance = 200
earth_color = "blue"
mars_radius = 15
mars_distance = 250
mars_color = "red"

# Configuração tela
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Desenha o sol
sun = turtle.Turtle()
sun.shape("circle")
sun.shapesize(sun_radius / 10)
sun.color(sun_color)

# Desenha o planeta Mercúrio
mercury = turtle.Turtle()
mercury.shape("circle")
mercury.penup()
mercury.goto(mercury_distance, 0)
mercury.pendown()
mercury.color(mercury_color)
mercury.shapesize(mercury_radius / 10)

# Desenha o planeta Vênus
venus = turtle.Turtle()
venus.shape("circle")
venus.penup()
venus.goto(venus_distance, 0)
venus.pendown()
venus.color(venus_color)
venus.shapesize(venus_radius / 10)

# Desenha o planeta Terra
earth = turtle.Turtle()
earth.shape("circle")
earth.penup()
earth.goto(earth_distance, 0)
earth.pendown()
earth.color(earth_color)
earth.shapesize(earth_radius / 10)

# Desenha o planeta Marte
mars = turtle.Turtle()
mars.shape("circle")
mars.penup()
mars.goto(mars_distance, 0)
mars.pendown()
mars.color(mars_color)
mars.shapesize(mars_radius / 10)

# velocidade dos planetas
mercury_speed = 10
venus_speed = 5
earth_speed = 4
mars_speed = 2

# Animação do sistema solar
while True:
    mercury.circle(mercury_distance, mercury_speed)
    venus.circle(venus_distance, venus_speed)
    earth.circle(earth_distance, earth_speed)
    mars.circle(mars_distance, mars_speed)
