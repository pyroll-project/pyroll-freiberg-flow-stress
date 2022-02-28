import sys
from pyroll.utils import hookutils

from pyroll import RollPassProfile
from ..freiberg_flow_stress import FreibergFlowStressCoefficients


@RollPassProfile.hookimpl
@hookutils.applies_to_materials("C45")
def freiberg_flow_stress_coefficients(profile):
    return FreibergFlowStressCoefficients(
        a=4936.26 * 1e6,
        m1=-0.00284749,
        m2=0.230591,
        m4=0.0007177260,
        m5=-0.00154014,
        m7=0.44794,
        m8=0.000117008,
        baseStrain=0.1,
        baseStrainRate=0.1
    )


RollPassProfile.plugin_manager.register(sys.modules[__name__])
