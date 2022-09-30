class PoolManager:
    def __init__(self, pool) -> None:
        self.pool = pool

    def __enter__(self) -> object:
        self.obj = self.pool.acquire()
        return self.obj

    def __exit__(self, type, value, traceback) -> None:
        self.pool.release(self.obj)


class DBConnection:
    def get_db_conn(self):
        print("DB Conn Object-->", self)


class ObjectPool:
    def __init__(self, size, class_) -> None:
        self.size = size
        self.__free_objs = []
        self.__in_use_objs = []
        self.class_ = class_
        for _ in range(size):
            self.__free_objs.append(class_())

    def acquire(self) -> object:
        if not self.__free_objs:
            raise Exception("No available DB object is available.")
        else:
            free_obj = self.__free_objs[-1]
            self.__free_objs.remove(free_obj)
            self.__in_use_objs.append(free_obj)
            return free_obj

    def release(self, obj: object) -> None:
        self.__in_use_objs.remove(obj)
        self.__free_objs.append(obj)


obj_pool = ObjectPool(2, DBConnection)
obj_pool.acquire().get_db_conn()

with PoolManager(obj_pool) as db_conn:
    db_conn.get_db_conn()
with PoolManager(obj_pool) as db_conn:
    db_conn.get_db_conn()
with PoolManager(obj_pool) as db_conn:
    db_conn.get_db_conn()
