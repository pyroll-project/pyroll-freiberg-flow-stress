import sys

from pyroll import RollPassProfile
from pyroll.utils import hookutils
from ..freiberg_flow_stress import FreibergFlowStressCoefficients


@RollPassProfile.hookimpl
@hookutils.applies_to_materials("C20")
@hookutils.applies_to_materials("C22")
def freiberg_flow_stress_coefficients(profile):
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


RollPassProfile.plugin_manager.register(sys.modules[__name__])
