import numpy as np

from pyroll.freiberg_flow_stress.freiberg_flow_stress import FreibergFlowStressCoefficients
from pyroll.freiberg_flow_stress.hookimpls import flow_stress


class DummyProfile:
    def __init__(self):
        self.strain = 1
        self.temperature = 1200
        self.material = "C45"
        self.freiberg_flow_stress_coefficients = FreibergFlowStressCoefficients(
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


class DummyRollPass:
    def __init__(self):
        self.strain_rate = 1


def test_hook():
    rp = DummyRollPass()
    p = DummyProfile()
    print()

    fs = flow_stress(rp, p)
    print(fs)
    assert np.isfinite(fs)

    rp.strain_rate = 0
    fs = flow_stress(rp, p)
    print(fs)
    assert np.isfinite(fs)

    p.strain = 0
    fs = flow_stress(rp, p)
    print(fs)
    assert np.isfinite(fs)
