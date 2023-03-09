from pyroll.core import Profile, DeformationUnit, Hook

from .freiberg_flow_stress import FreibergFlowStressCoefficients, flow_stress

VERSION = "2.0.0"

Profile.freiberg_flow_stress_coefficients = Hook[FreibergFlowStressCoefficients]()


@DeformationUnit.Profile.flow_stress
def freiberg_flow_stress(self: DeformationUnit.Profile):
    if hasattr(self, "freiberg_flow_stress_coefficients"):
        return flow_stress(
            self.freiberg_flow_stress_coefficients,
            self.strain,
            self.unit.strain_rate,
            self.temperature
        )


@DeformationUnit.Profile.flow_stress_function
def freiberg_flow_stress_function(self: DeformationUnit.Profile):
    if hasattr(self, "freiberg_flow_stress_coefficients"):
        def f(strain: float, strain_rate: float, temperature: float) -> float:
            return flow_stress(self.freiberg_flow_stress_coefficients, strain, strain_rate, temperature)

        return f


from . import materials
