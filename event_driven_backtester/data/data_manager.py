from abc import ABC, abstractmethod


class DataManager(ABC):
    """
    Implements generalized data management logic.
    """

    @abstractmethod
    def run() -> None:
        raise NotImplementedError
