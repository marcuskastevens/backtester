from abc import ABC, abstractmethod


class ExecutionManager(ABC):
    """
    Implements trade execution logic.
    """

    @abstractmethod
    def run() -> None:
        raise NotImplementedError
