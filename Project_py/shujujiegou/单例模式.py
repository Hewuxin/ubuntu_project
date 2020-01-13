


class Sigleton:
    # 私有化   单例的地址就保存在__instance
    # 使用dir() 可以看到私有属性 但是不能访问
    __instance = None
    # 重写__new__ cls代表当前类  __new__方法构建地址

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance


s = Sigleton()
s1 = Sigleton()
print(s)
print(s1)











class Sigleton01:
    # 定有私有变量
    __instance = None

    # 重写__new__方法 构建对象内存地址的方法
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
