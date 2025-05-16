# StudyDesignPatterns
A repository for learning popular design patterns in Python
## CREATIONAL patterns
Resume: 
1. We use SINGLETON когда нам нужно чтобы какая-то сущность была только в одном экземпляре
2. АбстрактнаяФабрика порождает семейство объектов, сама по себе фабрика тоже объект (их мб много для разных семейств)
3. Фабричный МЕТОД порождает обьекты в зависимости от того какой объект мы хотим, во время runtime
Абстрактные фабрики очень часто содержат в себе эти фабричные методы вместо того чтобы возвращать захардкоженые листы, как в примере с прошлого коммита

//TODO: Взять фабричный метод и внедрить его в абстрактную фабрику, чтобы улучшить код (не хардкодить тупо списком кнопки, для каких-нибудь специфических эквалайзеров).
### Singleton Design Pattern

The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.

- **Intent**: Control object creation so that only one instance of a class exists.
- **Implementation**: Override the `__new__` method (or use a metaclass/decorator) to check for an existing instance and return it if present.
- **Pros**:
  - Guarantees a single, consistent instance throughout an application.
  - Provides a well-defined access point.
- **Cons**:
  - Introduces global state, which can complicate testing and maintenance.
  - Can hide dependencies and violate the single responsibility principle.

In this repository, `creational/singleton.py` implements the pattern by storing the first instance in `__it__`:

```python
class Singleton(object):
    def __new__(cls, *args, **kwds):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it

    def init(self, *args, **kwds):
        pass
```

To use it, subclass `Singleton` and implement an `init` method instead of `__init__`:

```python
class MySingleton(Singleton):
    def init(self, value):
        self.value = value

a = MySingleton(10)
b = MySingleton(20)
assert a is b
print(a.value)  # Outputs: 10
```

In `mainwindow.py`, `Window` inherits from both `Tk` and `Singleton`, so calls to `Window()` always return the same GUI window instance.

ABSTRACT FACTORY:
    A - Abstract Factory - this is added level of abstraction
    B - Abstraction need for programmer, not for computer
