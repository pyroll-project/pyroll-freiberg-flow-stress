from pyroll.core import Profile, RollPass
from pyroll.core.hooks import Hook
from functools import partial

from .freiberg_flow_stress import FreibergFlowStressCoefficients, flow_stress

VERSION = "2.0.0b"

Profile.freiberg_flow_stress_coefficients = Hook[FreibergFlowStressCoefficients]()


@RollPass.Profile.flow_stress
def freiberg_flow_stress(self: RollPass.Profile):
    if hasattr(self, "freiberg_flow_stress_coefficients"):
        return flow_stress(
            self.freiberg_flow_stress_coefficients,
            self.strain,
            self.roll_pass().strain_rate,
            self.temperature
        )


@RollPass.Profile.flow_stress_function
def freiberg_flow_stress_function(self: RollPass.Profile):
    return partial(
        flow_stress,
        coefficients=self.freiberg_flow_stress_coefficients
    )


from . import materials
