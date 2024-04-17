import numpy as np

from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class FreibergFlowStressCoefficients:
    """
    Class representing the Freiberg flow stress model published by Hensel et al.
    """
    a: Optional[float]
    m1: Optional[float] = 0
    m2: Optional[float] = 0
    m3: Optional[float] = 0
    m4: Optional[float] = 0
    m5: Optional[float] = 0
    m6: Optional[float] = 0
    m7: Optional[float] = 0
    m8: Optional[float] = 0
    m9: Optional[float] = 0

    baseStrain: Optional[float] = 0.1
    baseStrainRate: Optional[float] = 0.1


def flow_stress(coefficients: FreibergFlowStressCoefficients, strain: Union[float, np.ndarray],
                strain_rate: Union[float, np.ndarray], temperature: Union[float, np.ndarray]):
    """
    Calculates the flow stress according to the model from the provided coefficients, strain, strain rate and temperature.

    :param coefficients: the coefficients set to use
    :param strain: the equivalent strain experienced
    :param strain_rate: the equivalent strain rate experienced
    :param temperature: the absolute temperature of the material (K)
    """

    strain = strain + coefficients.baseStrain
    strain_rate = strain_rate + coefficients.baseStrainRate
    temperature = temperature - 273.15
    return (coefficients.a * np.exp(coefficients.m1 * temperature) * (strain ** coefficients.m2) *
            (strain_rate ** coefficients.m3) * np.exp(coefficients.m4 / strain) *
            ((1 + strain) ** (coefficients.m5 * temperature)) *
            ((1 + strain) ** coefficients.m6) * np.exp(coefficients.m7 * strain) *
            (strain_rate ** (coefficients.m8 * temperature)) * (temperature ** coefficients.m9))
