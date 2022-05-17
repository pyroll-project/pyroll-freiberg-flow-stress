import sys

from pyroll.core import RollPass
from pyroll.utils import for_materials
from ..freiberg_flow_stress import FreibergFlowStressCoefficients


@RollPass.Profile.hookimpl
@for_materials("C20")
@for_materials("C22")
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


RollPass.Profile.plugin_manager.register(sys.modules[__name__])
