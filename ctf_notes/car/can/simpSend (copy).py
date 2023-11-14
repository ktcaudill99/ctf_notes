
"""
This example shows how sending a single message works.
example from https://python-can.readthedocs.io/en/master/index.html
"""
import time
import can
can.rc['interface'] = 'socketcan'
can.rc['channel'] = 'vcan0'
can.rc['bitrate'] = 500000
from can.interface import Bus
#bus = can.Bus(channel=channel, interface=bustype)
bus = Bus()


def send_one():
	"send a single message"
	
	#this uses the default configuration (for example from the config file

	# see https://python-can.readthedocs.io/en/stable/configuration.html
	with can.interface.Bus() as bus:

	# Using specific buses works similar:
	# bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
	# bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=250000)
	# bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
	# bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0, bitrate=250000)
	#...

		msg = can.Message(
			arbitration_id=0x024, data=[2, 1, 1, 243, 98, 14, 128, 19], is_extended_id=False
		)

		try:
			bus.send(msg)
			print(f"Message sent on {bus.channel_info}")
		except can.CanError:
			print("Message NOT sent")


def spam():
	":param id: Spam the bus with messages including the data id."

#	with can.interface.Bus() as bus:

	while True:
#			msg = can.Message(arbitration_id=0x666, data=[id, i, 0, 1, 3, 1, 4, 1], is_extended_id=False)
#			bus.send(msg)
		send_one()

		time.sleep(1)

 
if __name__ == "__main__":
	send_one()
#	spam()


