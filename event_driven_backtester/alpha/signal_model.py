from abc import ABC, abstractmethod


class Signal(ABC):
    """
    Implements low-level, raw signal. This is the atomic element that an AlphaModel builds upon.
    """

    @abstractmethod
    def run() -> None:
        raise NotImplementedError
