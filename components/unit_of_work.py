import threading


class UnitOfWork:
    current = threading.local()

    # Waiting lists - performing actions.
    def __init__(self):
        self.new_objects = []
        self.dirty_objects = []
        self.removed_objects = []

    def set_mapper_registry(self, mapper_registry):
        self.MapperRegistry = mapper_registry

    def register_new(self, obj):
        """
        Adds an object to the creation list.

        :param obj: object to add to the database.
        """
        self.new_objects.append(obj)

    def register_dirty(self, obj):
        """
        Adds an object to the changes list.

        :param obj: object to change to the database.
        """
        self.dirty_objects.append(obj)

    def register_removed(self, obj):
        """
        Adds an object to the removes list.

        :param obj: object to remove to the database.
        """
        self.removed_objects.append(obj)

    def commit(self):
        """
        A function that starts the process of adding data to the database
        and clearing the task queue.
        """

        self.insert_new()
        self.update_dirty()
        self.delete_removed()

        self.new_objects.clear()
        self.dirty_objects.clear()
        self.removed_objects.clear()

    def insert_new(self):
        for obj in self.new_objects:
            self.MapperRegistry.get_mapper(obj).insert(obj)

    def update_dirty(self):
        for obj in self.dirty_objects:
            self.MapperRegistry.get_mapper(obj).update(obj)

    def delete_removed(self):
        for obj in self.removed_objects:
            self.MapperRegistry.get_mapper(obj).delete(obj)

    @staticmethod
    def new_current():
        __class__.set_current(UnitOfWork())

    @classmethod
    def set_current(cls, unit_of_work):
        cls.current.unit_of_work = unit_of_work

    @classmethod
    def get_current(cls):
        return cls.current.unit_of_work


class DomainObject:
    def mark_new(self):
        """The function adds information about data changes to the queue."""

        UnitOfWork.get_current().register_new(self)

    def mark_dirty(self):
        """The function adds data update information to the queue."""

        UnitOfWork.get_current().register_dirty(self)

    def mark_removed(self):
        """The function adds information about data deletion to the queue."""

        UnitOfWork.get_current().register_removed(self)
