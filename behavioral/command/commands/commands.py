from behavioral.command.commands.i_command import ICommand
from behavioral.command.receivers.receiver import Light, Stereo


class NoCommand(ICommand):
    def execute(self) -> bool:
        return True


class LightOnCommand(ICommand):

    def __init__(self, light: Light):
        self.light: Light = light

    def execute(self) -> bool:
        self.light.on()
        return True


class LightOffCommand(ICommand):

    def __init__(self, light: Light):
        self.light: Light = light

    def execute(self) -> bool:
        self.light.off()
        return True


class StereoOffWithCDCommand(ICommand):

    def __init__(self, stereo: Stereo):
        self.stereo: Stereo = stereo

    def execute(self) -> bool:
        self.stereo.off()
        return True


class StereoOnWithCDCommand(ICommand):

    def __init__(self, stereo: Stereo):
        self.stereo: Stereo = stereo

    def execute(self) -> bool:
        self.stereo.on()
        return True
