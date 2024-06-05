from blockeng_lasertune.blkqcl import BLKQCL_Proxy


if __name__ == "__main__":
    lasertune = BLKQCL_Proxy(url="http://169.254.83.220:8080")

    version_details: dict = lasertune.GetVersionDetails()

    factory_settings: dict = lasertune.GetFactorySettings()

    user_settings: dict = lasertune.GetUserSettings()

    power_state: str = lasertune.GetPowerState()

    device_name: str = lasertune.GetDeviceName()

    alarms: list = lasertune.GetAlarms()

    laser_pointer_on: bool = lasertune.GetLaserPointerOn()

    toggle_switch_state: str = lasertune.GetToggleSwitchState(which=lasertune.ToggleSwitchType.FanA)

    sensors: dict = lasertune.ReadSensors(sensorsToRead={})

    # Laser remains on after MoveTune()
    move_tune: float = lasertune.MoveTune(waveNumber=1599.2)  # returns wavenumber of laser after move tune

    print("Pause...")
