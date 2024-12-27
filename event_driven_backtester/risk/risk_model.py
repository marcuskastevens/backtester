from abc import ABC, abstractmethod


class RiskModel(ABC):
    """
    Implements risk modeling logic.
    """

    @abstractmethod
    def run() -> None:
        raise NotImplementedError
