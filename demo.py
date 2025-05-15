from geometry.shapes import Circle, Triangle

# Создаем круг и выводим его площадь
circle = Circle(radius=10)
print(f"Площадь круга: {circle.area():.2f}")

# Создаем треугольник и проверяем, является ли он прямоугольным
triangle = Triangle(a=3, b=4, c=5)
print(f"Треугольник ({triangle.a}, {triangle.b}, {triangle.c}) {'является' if triangle.is_right_triangle() else 'не является'} прямоугольным.")

# Рассчитываем площадь треугольника
print(f"Площадь треугольника: {triangle.area():.2f}")