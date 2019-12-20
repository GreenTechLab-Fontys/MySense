from core.config_file import ConfigFile
from core.modules import PlatformModule
from core.log import *

class LoPy4(PlatformModule):
    """
    This class wrapps the generic LoPy4 features.
    The goal is to keep the core class independent from pycom libraries.
    """

    def __init__(self):
        super(LoPy4, self).__init__()

        # configure power pins
        from machine import Pin
        for i in self.config().get("pwr_pins"):
            log_debug("Activating power pin " + str(i) + ".")
            p = Pin("P" + str(i),mode=Pin.OUT)
            p.value(1)

        # set wifi access point
        import pycom
        pycom.wifi_on_boot(self.config().get("wifi_on_boot"))

    def is_run_tests(self):
        # only run test if not woke up from deep sleep
        import machine
        return machine.reset_cause() != machine.DEEPSLEEP_RESET

    def test(self):
        pass

    def get_config_definition():
        return (
            "platform_lopy4",
            "LoPy4 platform options.",
            (
                ("wifi_on_boot", "true", "If set to true a wireless access point will be started on boot.", ConfigFile.VariableType.bool),
                ("pwr_pins", "", "A list of pins seperated by spaces which are used as power sources.", ConfigFile.VariableType.uint_list),
            )
        )
