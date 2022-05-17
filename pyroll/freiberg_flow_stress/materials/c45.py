import sys

from pyroll.core import RollPass
from pyroll.utils import for_materials
from ..freiberg_flow_stress import FreibergFlowStressCoefficients


@RollPass.Profile.hookimpl
@for_materials("C45")
def freiberg_flow_stress_coefficients(profile):
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


RollPass.Profile.plugin_manager.register(sys.modules[__name__])
