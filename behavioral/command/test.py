from behavioral.command.commands.commands import *
from behavioral.command.commands.i_command import ICommand
from behavioral.command.receivers.receiver import Light, Stereo
from behavioral.command.remote_control import RemoteControl

if __name__ == "__main__":
    remote: RemoteControl = RemoteControl(4)

    # Command receivers
    living_room_light: Light = Light("Living Room Light")
    bed_room_light: Light = Light("Bed Room Light")
    kitchen_room_light: Light = Light("Kitchen Room Light")
    stereo: Stereo = Stereo()

    # Commands
    living_room_light_on_command: ICommand = LightOnCommand(living_room_light)
    living_room_light_off_command: ICommand = LightOffCommand(living_room_light)

    bed_room_light_on_command: ICommand = LightOnCommand(bed_room_light)
    bed_room_light_off_command: ICommand = LightOffCommand(bed_room_light)

    kitchen_room_light_on_command: ICommand = LightOnCommand(kitchen_room_light)
    kitchen_room_light_off_command: ICommand = LightOffCommand(kitchen_room_light)

    stereo_on_command: ICommand = StereoOnWithCDCommand(stereo)
    stereo_off_command: ICommand = StereoOffWithCDCommand(stereo)

    # Set commands to remote control

    remote.set_command(0, living_room_light_on_command, living_room_light_off_command)
    remote.set_command(1, bed_room_light_on_command, bed_room_light_off_command)
    remote.set_command(2, kitchen_room_light_on_command, kitchen_room_light_off_command)
    remote.set_command(3, stereo_on_command, stereo_off_command)

    print(remote)

    remote.on_button_pushed(3)
    remote.on_button_pushed(2)
    remote.off_button_pushed(2)