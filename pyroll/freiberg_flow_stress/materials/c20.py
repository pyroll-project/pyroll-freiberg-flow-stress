from pyroll.core import Profile
from ..freiberg_flow_stress import FreibergFlowStressCoefficients

MATERIALS = {"C20", "C22"}


@Profile.freiberg_flow_stress_coefficients
def freiberg_flow_stress_coefficients(self: Profile):
    if MATERIALS.intersection(self.material):
        return FreibergFlowStressCoefficients(
            a=3304.39 * 1e6,
            m1=-0.00281,
            m2=0.34766,
            m4=0.00002,
            m5=-0.00130,
            m7=0.07632,
            m8=0.000148,
            baseStrain=0.1,
            baseStrainRate=0.1
        )
