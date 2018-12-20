from abc import (
    ABC,
    abstractmethod,
)


class BaseSedes(ABC):
    @abstractmethod
    def serialize(self, obj):
        pass

    @abstractmethod
    def deserialize_segment(self, serialized_obj, start_index):
        pass

    @abstractmethod
    def deserialize(self, data):
        pass
