import numpy as np

from pyroll_freiberg_flow_stress.freiberg_flow_stress import flow_stress
from pyroll_freiberg_flow_stress.materials.c45 import freiberg_flow_stress_coefficients


class DummyProfile:
    def __init__(self):
        self.strain = 1
        self.temperature = 1200
        self.material = "C45"
        self.freiberg_flow_stress_coefficients = freiberg_flow_stress_coefficients(self)


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
