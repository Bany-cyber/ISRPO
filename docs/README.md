# Документация проекта Geometric Lib
## Общее описание решения
**Geometric Lib** — это библиотека, предназначенная для выполнения базовых геометрических вычислений.
## Описание функций

### circle.py

**area(r)**
Принимает радиус круга и выводит его площадь
```python
import circle

circle_area = circle.area(1)

print(f"Площадь круга: {circle_area}")

```

**perimeter(r)**
Принимает радиус круга и выводит его периметр
```python
import circle

circle_perimetr = circle.perimeter(1)

print(f"Периметр круга: {circle_perimetr}")

```






### rectangle.py

**area(a,b)**
Принимает значения сторон прямоугольника и возвращает площадь этого прямоугольника
```python
import rectangle

rectangle_area = rectangle.area(1,1)

print(f"Площадь прямоугольника: {rectangle_area}")

```

**perimeter(a,b)**
Принимает значения сторон прямоугольника и возвращает периметр этого прямоугольника
```python
import rectangle

rectangle_perimetr = rectangle.perimeter(1,1)

print(f"Периметр прямоугольника: {rectangle_perimetr}")

```





### square.py

**area(a)**
Принимает значение стороны квадрата и возвращает его площадь
```python
import square

square_area = square.area(1)

print(f"Площадь квадрата: {square_area}")

```

**perimeter(a)**
Принимает значение стороны квадрата и возвращает его периметр
```python
import square

square_perimetr = square.perimeter(1)

print(f"Периметр квадрата: {square_perimetr}")

```



### triangle.py

**area(a,h)**
Принимает значение стороны треугольника и высоту к этой стороне, возвращает его площадь
```python
import triangle

triangle_area = triangle.area(1,1)

print(f"Площадь треугольника: {triangle_area}")

```

**perimeter(a,b,c)**
Принимает значения сторон треугольника и возвращает его периметр
```python
import triangle

triangle_perimetr = triangle.perimeter(1,1,1)

print(f"Периметр треугольника: {triangle_perimetr}")

```

## История изменений проекта
**9cd2d37** (HEAD -> new_features_588088) добавлены комментарии
**e82d8b9** исправлена ошибка и добавлен файл для вычисления периметра и площади треугольника
**ecec6c0** добавлен новый файл для вычисления площади и периметра прямоугольника
**d078c8d** (origin/main, origin/HEAD, main) L-03: Docs added
**8ba9aeb** L-03: Circle and square added