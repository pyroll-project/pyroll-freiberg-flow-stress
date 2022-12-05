from pyroll.core import Profile
from ..freiberg_flow_stress import FreibergFlowStressCoefficients

MATERIALS = {"S355J2"}


@Profile.freiberg_flow_stress_coefficients
def freiberg_flow_stress_coefficients(self: Profile):
    if MATERIALS.intersection(self.material):
        return FreibergFlowStressCoefficients(
            a=2852.66 * 1e6,
            m1=-0.00244,
            m2=0.41934,
            m4=0.00088,
            m5=-0.00149,
            m7=0.12169,
            m8=0.000127,
            baseStrain=0.1,
            baseStrainRate=0.1
        )
