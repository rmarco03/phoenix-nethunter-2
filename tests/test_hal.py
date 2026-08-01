from phoenix_hal.core.hal import PhoenixHAL


def test_device():

    hal = PhoenixHAL()

    device = hal.get_device()

    assert device["identifier"] == "iPhone9,1"