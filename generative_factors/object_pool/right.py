class MyClass:
    # Return the resource to default setting
    def reset(self):
        self.setting = 0


class ObjectPool:
    def __init__(self, size):
        self.objects = [MyClass() for _ in range(size)]

    def acquire(self):
        if self.objects:
            return self.objects.pop()
        else:
            self.objects.append(MyClass())
            return self.objects.pop()

    def release(self, reusable):
        reusable.reset()
        self.objects.append(reusable)


pool = ObjectPool(10)
reusable = pool.acquire()
pool.release(reusable)
