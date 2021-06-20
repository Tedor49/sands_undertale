class Room():
    """простая структурка

    все и так понятно

    """
    def __init__(self, typ, n):
        types = ["актовый зал", "кабинет для занятий", "учительская", "кабинет директора"]
        if type(typ) == str:
            self.typ = typ.lower()
            self.al = types.index(typ.lower())
        else:
            self.typ = types[typ]
            self.al = typ
        self.n = n

    def __str__(self):
        return f"{self.typ} {self.n}"

class Person():
    """простая структурка

    все и так понятно

    """
    def __init__(self, typ, name, surname, thing):
        types = ["родитель", "ученик", "учитель", "директор"]
        if type(typ) == str:
            self.typ = typ
            self.al = types.index(typ)
        else:
            self.typ = types[typ]
            self.al = typ
        self.name = name
        self.surname = surname
        self.thing = thing

    def enter(self, room):
        """

        :param room: куда чел хочет войти
        :return: лог о успехе входа
        """
        print(f"{self.typ} {self.name} {self.surname} пытается войти в {room.typ} {room.n}: {['неудача', 'успех'][room.al <= self.al]}")

    def __str__(self):
        return f"{self.typ}\n{self.name} {self.surname}\n{self.thing}\n"

people = [Person(0, "Мамка", "Моя", "6 случаев незаконного проникновения на объект"), Person(3, "Директор", "Директорович", "Многа дипломаф"),\
          Person(1, "Арсений", "Воронин", "Идол, архимаг огня"), Person(2, "Макар", "Фамилия", "Любимая шутка: колобок повесился(")]
rooms = [Room(3, 666), Room(2, 228), Room(1, 300), Room(0, 1)]
print(*people, sep="\n")
print(*rooms, sep="\n")
#Person(0, "Мамка", "Моя", "6 случаев незаконного проникновения на объект").enter(Room(3, 666))
print()
for i in rooms:
    people[0].enter(i)
print()
for i in people:
    i.enter(rooms[3])

people[2].enter(rooms[0])