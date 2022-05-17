from pyroll.core import RollPass


@RollPass.Profile.hookspec
def freiberg_flow_stress_coefficients(roll_pass, profile):
    """Get a FreibergFlowStressCoefficient object suitable for the given roll pass.
    Return None if the implementation cannot serve this.
    The first not None result is taken."""
