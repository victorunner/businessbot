# :keycap_0: Pythonistas love Python

:backhand_index_pointing_right: Какие источники информации (книги, youtube-каналы etc) вы используете для изучения (совершенствования) языка программирования `Python`?
:backhand_index_pointing_right: Кто является автором `Python`?
:backhand_index_pointing_right: `Python` является интерпретируемым или компилируемым языком программирования?
:backhand_index_pointing_right: Какие ваши любимые фичи языка `Python`?

&&

# :keycap_1: Всё течет, всё изменяется

Каков будет результат выполнения кода:

```
record = (0, ['a'], 2)
assert type(rесоrd) is tuple

rесоrd[1][0] = 'b'
print(rесоrd)
```

&&

# :keycap_2: От малого к большему

Как отсортировать список, приведенный ниже, в порядке возрастания длины слова.

```
words_list = ['monitorsoft', 'best', 'the', 'company']
```

&&

# :keycap_3: Зоопарк (змеи, верблюды, ...)

Реализуйте функцию, которая преобразует строку из `snake_case`-формата в `UpperCamelCase`.

&&

# :keycap_4: Даешь больше функций!

:backhand_index_pointing_right: Реализовать функцию `f`, такую что `f(x)(y) == x`.

```
# реализация функции f

assert f('bar')('dummy') == 'bar'
assert f(42)('dumb') == 42
```

:backhand_index_pointing_right: Написать декоратор `@result2str`, который результат, возвращаемый функцией, преобразует в строку.

&&

# :keycap_5: Полная семья

Класс `C` имеет двух родителей, в каждом из которых реализован метод `run()`.

```
class A:
    def run(self):
        print('run in A')

class B:
    def run(self):
        print('run in B')

class С(B, A): pass
```

:backhand_index_pointing_right: Каков будет результат выполнения кода:

```
C().run()
```

:backhand_index_pointing_right: Если теперь реализовать в классе `C` метод `run()`, то как внутри его методов вызвать `run()` из классов `A` и `B`?
:backhand_index_pointing_right: Что такое `MRO` (Method Resolution Order)?

&&

# :keycap_6: Позвони мне, позвони

Найти сумму квадратов цифр телефонного номера. Телефонный номер дан в виде строки, в которой также могут содержаться нецифровые символы (например, такие как `+` и `-`).

&&

# :keycap_7: Милые роботы

Класс `Robot2D` описывает робота, который под действием управляющих команд шаг за шагом передвигается по плоскости.

```
class Robot2D:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def step_left(self):
        self.x -= 1

    def step_right(self):
        self.x += 1

    def step_backward(self):
        self.y -= 1

    def step_forward(self):
        self.y += 1

    def __repr__(self):
        return f'{type(self).__name__}({self.x!r}, {self.y!r})'
```

:backhand_index_pointing_right: Какие изменения необходимо внести в код, чтобы была возможность выполнить:

```
robot = Robot2D()
robot.step_right().step_forward().step_forward()
```

:backhand_index_pointing_right: В чем разница между `__str__` и `__repr__`?

&&

# :keycap_8: Словарей мало не бывает

Дан словарь:

```
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
```

:backhand_index_pointing_right: Как из данного словаря получить "инвертированный", т.е. такой словарь, в котором ключами (значениями) становятся значения (ключи) исходного словаря?
:backhand_index_pointing_right: Как на результат повлияет дублирование значений в исходном словаре? Кстати, как проверить уникальность значений словаря?
:backhand_index_pointing_right: Как на результат повлияет замена значений на списки (`'a' -> ['a']`, `'b' -> ['b']` etc) в исходном словаре?

&&

# :keycap_9: Не любим комментарии

Как реализовать генератор, возвращающий строки файла, за исключением начинающихся с символа `#`?

&&

# :keycap_1::keycap_0: Джанго: музыка и вестерн

Чем вьюсет отличается от view-функций?
