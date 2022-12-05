from pyroll.core import Profile
from ..freiberg_flow_stress import FreibergFlowStressCoefficients

MATERIALS = {"C45"}


@Profile.freiberg_flow_stress_coefficients
def freiberg_flow_stress_coefficients(self: Profile):
    if MATERIALS.intersection(self.material):
        return FreibergFlowStressCoefficients(
            a=3268.49 * 1e6,
            m1=-0.00267855,
            m2=0.34446,
            m4=0.000551814,
            m5=-0.00132042,
            m7=0.0166334,
            m8=0.000149907,
            baseStrain=0.1,
            baseStrainRate=0.1
        )
