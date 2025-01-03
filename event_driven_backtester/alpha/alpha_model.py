# Built-in dependencies
from typing import Dict, Union
from abc import ABC, abstractmethod

# External dependencies
import numpy as np
import pandas as pd

# Local dependencies
from event_driven_backtester.alpha.signal_model import Signal, StatisticalArbitrageMarketMakerSignal


class AlphaModel(ABC):
    """
    Implements signal postprocessing to form a vector of views (e.g., weights and expected returns).
    """

    signal: Signal

    def __init__(self, data: Union[Dict, pd.DataFrame]) -> None:

        self.data = data

        return

    @abstractmethod
    def __call__(self) -> None:
        raise NotImplementedError


class StatisticalArbitrageMarketMaker(AlphaModel):
    """
    Selectively provides liquidity when identifying dislocations from fair value.
    """

    signal: StatisticalArbitrageMarketMakerSignal = StatisticalArbitrageMarketMakerSignal()

    def __init__(self, data: Union[Dict, pd.DataFrame]) -> None:

        self.data = data

        return

    def __call__(self) -> None:

        signals: Dict = {index: self.signal(data=series) for index, series in self.data.items()}
