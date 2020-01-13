print("aaaa")
#

l = []
for i in range(10):
    l.append(i)


def a():
    pass

class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


if __name__ == "__main__":
    a()
