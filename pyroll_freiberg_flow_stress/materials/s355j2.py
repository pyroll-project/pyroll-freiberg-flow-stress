import sys

from pyroll import RollPassProfile
from pyroll.utils import hookutils
from ..freiberg_flow_stress import FreibergFlowStressCoefficients


@RollPassProfile.hookimpl
@hookutils.applies_to_materials("S355J2")
def freiberg_flow_stress_coefficients(profile):
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


RollPassProfile.plugin_manager.register(sys.modules[__name__])
