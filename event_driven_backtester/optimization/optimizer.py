from abc import ABC, abstractmethod


class Optimizer(ABC):
    """
    Implements generalized optimization logic.
    """

    @abstractmethod
    def run() -> None:
        raise NotImplementedError
