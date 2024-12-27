from abc import ABC, abstractmethod


class AlphaManager(ABC):
    """
    Implements alpha model management logic.
    """

    @abstractmethod
    def run() -> None:
        raise NotImplementedError
