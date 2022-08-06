from launcher import Launch
from converter import Converter

#Setup
launch = Launch()

while launch.software_executed:
    convert = Converter(launch.message_request())
    print(f'Your Message as Morse Code:\n{convert.message}')
    launch.continue_or_quit_decision()
