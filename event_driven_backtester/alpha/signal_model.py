# Built-in dependencies
from typing import Dict, Union
from abc import ABC, abstractmethod

# External dependencies
import pandas as pd


class Signal(ABC):
    """
    Implements low-level, raw signal. This is the atomic element that an AlphaModel builds upon.
    """

    @abstractmethod
    def __call__(self, data: Union[Dict, pd.Series]) -> Union[float, int]:
        raise NotImplementedError


class StatisticalArbitrageMarketMakerSignal(Signal):
    """
    Selectively provides liquidity when identifying dislocations from fair value.
    """

    def __call__(self, data: Union[Dict, pd.Series]) -> int:

        if (data["value"] <= data["lower_band"]) or (
            data["previous_signal"] is not None and data["previous_signal"] == 1 and data["value"] < data["fair_value"]
        ):
            return 1
        elif (data["value"] >= data["upper_band"]) or (
            data["previous_signal"] is not None and data["previous_signal"] == -1 and data["value"] > data["fair_value"]
        ):
            return -1
        else:
            return 0


def main() -> None:

    # Instantiate signal object
    signal: Signal = StatisticalArbitrageMarketMakerSignal()

    # Synthetic data
    data: Dict = {
        "value": 140.00,
        "fair_value": 101.00,
        "upper_band": 110.00,
        "lower_band": 90.00,
        "previous_signal": 0,
    }

    # Generate signal
    print(f"Signal = {signal(data=data)}")

    # Synthetic data
    data: Dict = {
        "value": 70,
        "fair_value": 101.00,
        "upper_band": 110.00,
        "lower_band": 90.00,
        "previous_signal": 0,
    }

    # Generate signal
    print(f"Signal = {signal(data=data)}")

    # Synthetic data
    data: Dict = {
        "value": 100.00,
        "fair_value": 101.00,
        "upper_band": 110.00,
        "lower_band": 90.00,
        "previous_signal": 1,
    }

    # Generate signal
    print(f"Signal = {signal(data=data)}")

    # Synthetic data
    data: Dict = {
        "value": 100.00,
        "fair_value": 101.00,
        "upper_band": 110.00,
        "lower_band": 90.00,
        "previous_signal": None,
    }

    # Generate signal
    print(f"Signal = {signal(data=data)}")

    return


if __name__ == "__main__":
    main()
