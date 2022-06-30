from dataclasses import dataclass
from typing import Optional

from numpy import exp

from pyroll.core import RollPass
from pyroll.utils import for_materials


@dataclass
class FreibergFlowStressCoefficients:
    """
    Class representing the Freiberg flow stress model published by Hensel et al.
    """
    a: Optional[float] = 0
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

    def register(self, material: str) -> str:
        """
        Utility function that registers a hookimpl delivering this instance for the specified ``material`` key.

        :param material: the material key, for which the hookimpl should apply (see :py:func:`pyroll.for_materials`)

        :returns: The cannonical name of the created plugin,
            as returned by ``RollPass.Profile.plugin_manager.register()``
        """

        @RollPass.Profile.hookimpl
        @for_materials(material)
        def freiberg_flow_stress_coefficients(profile):
            return self

        ns = type(f"FreibergFlowStressCoefficients_{material}", (), {
            "freiberg_flow_stress_coefficients": freiberg_flow_stress_coefficients
        })

        return RollPass.Profile.plugin_manager.register(ns)


def flow_stress(coefficients: FreibergFlowStressCoefficients, strain: float, strain_rate: float, temperature: float):
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
    return (coefficients.a * exp(coefficients.m1 * temperature) * (strain ** coefficients.m2) *
            (strain_rate ** coefficients.m3) * exp(coefficients.m4 / strain) *
            ((1 + strain) ** (coefficients.m5 * temperature)) *
            ((1 + strain) ** coefficients.m6) * exp(coefficients.m7 * strain) *
            (strain_rate ** (coefficients.m8 * temperature)) * (temperature ** coefficients.m9))
