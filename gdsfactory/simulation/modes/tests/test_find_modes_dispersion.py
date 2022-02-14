import numpy as np

from gdsfactory.simulation.modes.find_mode_dispersion import find_mode_dispersion


def test_find_modes_waveguide_dispersion():
    modes = find_mode_dispersion(wg_width=0.45, resolution=20, cache=None)
    m1 = modes

    # print(f"neff1 = {m1.neff}")
    # print(f"ng1 = {m1.ng}")

    # neff1 = 2.3948
    neff1 = 2.344238

    # ng1 = 4.23194
    ng1 = 4.226678

    assert np.isclose(m1.neff, neff1), (m1.neff, neff1)
    assert np.isclose(m1.ng, ng1), (m1.ng, ng1)


if __name__ == "__main__":
    test_find_modes_waveguide_dispersion()
