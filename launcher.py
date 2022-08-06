class Launch:
    def __init__(self):
        self.welcome='Welcome to Morse Code Converter!'
        print(self.welcome)
        self.software_executed=True

    def message_request(self):
        sentence = input('Please write a message which will be converted to Morse Code!:\n')
        return sentence

    def continue_or_quit_decision(self):
        decision = input('Do you want to convert another message to Morse Code?\nPlease type y or n!\n').lower()
        if decision=='y':
            self.software_executed = True
        else:
            self.software_executed = False

