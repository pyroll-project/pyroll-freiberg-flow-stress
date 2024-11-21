import numpy as np
import importlib.util

from pyroll.core import Profile, DeformationUnit, Hook, DiskElementUnit, RollPass


from .freiberg_flow_stress import FreibergFlowStressCoefficients, flow_stress

VERSION = "3.0.1"

REPORT_INSTALLED = bool(importlib.util.find_spec("pyroll.report"))
PILLAR_MODEL_INSTALLED = bool(importlib.util.find_spec("pyroll.pillar_model"))

if REPORT_INSTALLED and PILLAR_MODEL_INSTALLED:
    from . import report
    import pyroll.report

    pyroll.report.plugin_manager.register(report)


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


try:
    @DeformationUnit.Profile.pillars_flow_stress
    def pillars_flow_stress(self: DeformationUnit.Profile):
        if hasattr(self, "freiberg_flow_stress_coefficients"):
            return flow_stress(
                self.freiberg_flow_stress_coefficients,
                self.pillar_strains,
                self.unit.pillar_strain_rates,
                self.temperature
            )

    def initial_values(self: RollPass):
        from pyroll.pillar_model import Config
        self.in_profile.pillar_strains = np.zeros(Config.PILLAR_COUNT)

    RollPass.additional_inits.append(initial_values)

except AttributeError:
    pass  # pillar_model not loaded

from . import materials