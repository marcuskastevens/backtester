from abc import ABC, abstractmethod


class PortfolioManager(ABC):
    """
    Implements a centralized controller of all portfolio management sub-processes.
    """

    @abstractmethod
    def run() -> None:
        raise NotImplementedError
