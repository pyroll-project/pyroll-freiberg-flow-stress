import weakref

import numpy as np

from pyroll.freiberg_flow_stress.freiberg_flow_stress import FreibergFlowStressCoefficients, flow_stress
from pyroll.freiberg_flow_stress import freiberg_flow_stress as hook

strain = 1
strain_rate = 1
temperature = 1200
coefficients = FreibergFlowStressCoefficients(
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


class DummyProfile:
    def __init__(self):
        self.strain = strain
        self.temperature = temperature
        self.material = "C45"
        self.freiberg_flow_stress_coefficients = coefficients


class DummyRollPass:
    def __init__(self):
        self.strain_rate = strain_rate


def test_hook():
    rp = DummyRollPass()
    p = DummyProfile()
    p.unit = rp
    print()

    fs = hook(p)
    print(fs)
    assert np.isfinite(fs)
    assert fs == flow_stress(coefficients, strain, strain_rate, temperature)

    rp.strain_rate = 0
    fs = hook(p)
    print(fs)
    assert np.isfinite(fs)
    assert fs == flow_stress(coefficients, strain, 0, temperature)

    p.strain = 0
    fs = hook(p)
    print(fs)
    assert np.isfinite(fs)
    assert fs == flow_stress(coefficients, 0, 0, temperature)
