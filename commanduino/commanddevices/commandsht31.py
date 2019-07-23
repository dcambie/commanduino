from .commanddevice import CommandDevice

import logging
module_logger = logging.getLogger(__name__)

# bonjour info
BONJOUR_ID = 'SHT31'
CLASS_NAME = 'CommandSHT31'

# incoming
CMD_ANSWER_CELSIUS = 'C'
CMD_ANSWER_HUMIDITY = 'H'

# outgoing
CMD_REQUEST_CELSIUS = 'RC'
CMD_REQUEST_HUMIDITY = 'RH'


class CommandSHT31(CommandDevice):

    def __init__(self):
        CommandDevice.__init__(self)
        self.register_all_requests()

    ##
    def register_all_requests(self):
        self.register_request(
            CMD_REQUEST_CELSIUS,
            CMD_ANSWER_CELSIUS,
            'celsius',
            self.handle_celsius_command)

        self.register_request(
            CMD_REQUEST_HUMIDITY,
            CMD_ANSWER_HUMIDITY,
            'humidity',
            self.handle_humidity_command)

    def handle_celsius_command(self, *arg):
        if arg[0]:
            self.celsius = float(arg[0])
            self.celsius_lock.ensure_released()

    def handle_humidity_command(self, *arg):
        if arg[0]:
            self.humidity = float(arg[0])
            self.humidity_lock.ensure_released()
