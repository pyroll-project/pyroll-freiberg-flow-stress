from pyroll.core import Profile, RollPass
from pyroll.core.hooks import Hook

from .freiberg_flow_stress import FreibergFlowStressCoefficients, flow_stress

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


from . import materials
