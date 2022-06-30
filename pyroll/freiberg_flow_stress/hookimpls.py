from pyroll.core import RollPass
from . import freiberg_flow_stress


@RollPass.Profile.hookimpl
def flow_stress(roll_pass: RollPass, profile: RollPass.Profile):
    if not hasattr(profile, "freiberg_flow_stress_coefficients"):
        return None

    return freiberg_flow_stress.flow_stress(
        profile.freiberg_flow_stress_coefficients,
        profile.strain,
        roll_pass.strain_rate,
        profile.temperature
    )
