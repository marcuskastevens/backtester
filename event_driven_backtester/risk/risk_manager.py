from abc import ABC, abstractmethod


class RiskManager(ABC):
    """
    Implements risk modeling, risk control, and bet sizing management logic.
    """

    @abstractmethod
    def run() -> None:
        raise NotImplementedError
