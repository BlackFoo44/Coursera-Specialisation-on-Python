Представьте себя ненадолго разработчиком компьютерной игры в стиле фэнтези. Вам поручено написать реализацию системы эффектов, которые могут быть наложены на героя вашей игры.

В игре есть герой, который обладает некоторым набором характеристик. Класс героя описан следующим образом:
```
class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points, 
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость 
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()

```
К основным характеристикам относятся: Сила (Strength), Восприятие (Perception), Выносливость (Endurance), Харизма (Charisma), Интеллект (Intelligence), Ловкость (Agility), Удача (Luck).

Враги и союзники могут накладывать на героя положительные и отрицательные эффекты. Эти эффекты изменяют характеристики героя,  увеличивая или уменьшая значения определенных характеристик, в зависимости от того какие эффекты были наложены.  На героя можно накладывать бесконечно много эффектов, действие одинаковых эффектов суммируется. Игрок должен знать, какие положительные и какие отрицательные эффекты на него были наложены и в каком порядке. Названия эффектов совпадают с названиями классов.

За получение данных о текущем состоянии героя отвечают методы get_stats, get_positive_effects,  get_negative_effects.

Описание эффектов:
Берсерк (Berserk) - Увеличивает характеристики: Сила, Выносливость, Ловкость, Удача на 7;

Уменьшает характеристики: Восприятие, Харизма, Интеллект на 3; количество единиц здоровья увеличивается на 50.

Благословение (Blessing) - увеличивает все основные характеристики на 2.

Слабость (Weakness) - уменьшает характеристики: Сила, Выносливость, Ловкость на 4.

Сглаз (EvilEye) - уменьшает  характеристику Удача на 10.

Проклятье (Curse) - уменьшает все основные характеристики на 2.

 

При выполнении задания необходимо учитывать, что:

изначальные характеристики базового объекта не должны меняться.

изменения характеристик и накладываемых эффектов (баффов/дебаффов) должны происходить динамически, то есть вычисляться при вызове методов get_stats, get_positive_effects, get_negative_effects

абстрактные классы AbstractPositive,  AbstractNegative и соответственно их потомки могут принимать любой параметр base при инициализации объекта (_ _ init _ _ (self, base))

эффекты должны корректно сниматься, в том числе и из середины стека

Для тестирования правильности работы вашего решения вы можете повторить пример работы, приведенный ниже, или использовать тестовый скрипт.  Заметим, что данные примеры не покрывают всех тестовых случаев, проверяемых тестовой системой, это всего лишь отправная точка для ваших экспериментов с кодом решения.

Важно!  На проверку необходимо сдать фрагмент кода, содержащий только реализацию 8 классов: AbstractEffect,  AbstractPositive,  AbstractNegative, Berserk, Blessing, Weakness, Curse, EvilEye. Описывать класс Hero и импортировать его в коде НЕ НУЖНО (он уже реализован и будет импортирован тестовой системой).

Решение

````
from abc import abstractmethod,ABC

class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        return self.positive_effects

    @abstractmethod
    def get_negative_effects(self):
        return self.negative_effects

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):
    def get_negative_effects(self):
        return self.base.get_negative_effects()


class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Berserk(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["HP"] += 50
        stats["Strength"] += 7
        stats["Endurance"] += 7
        stats["Agility"] += 7
        stats["Luck"] += 7
        stats["Perception"] -= 3
        stats["Charisma"] -= 3
        stats["Intelligence"] -= 3
        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Berserk"]


class Blessing(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] += 2
        stats["Endurance"] += 2
        stats["Agility"] += 2
        stats["Luck"] += 2
        stats["Perception"] += 2
        stats["Charisma"] += 2
        stats["Intelligence"] += 2
        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Blessing"]


class Weakness(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 4
        stats["Endurance"] -= 4
        stats["Agility"] -= 4
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Weakness"]


class Curse(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 2
        stats["Endurance"] -= 2
        stats["Agility"] -= 2
        stats["Luck"] -= 2
        stats["Perception"] -= 2
        stats["Charisma"] -= 2
        stats["Intelligence"] -= 2
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Curse"]


class EvilEye(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Luck"] -= 10
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["EvilEye"]