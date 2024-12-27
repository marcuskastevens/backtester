from abc import ABC, abstractmethod


class AlphaModel(ABC):
    """
    Implements signal postprocessing to form a vector of views (e.g., weights and expected returns).
    """

    @abstractmethod
    def run() -> None:
        raise NotImplementedError
