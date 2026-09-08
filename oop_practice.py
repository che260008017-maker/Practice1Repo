
"""
def decide(distance):
	if distance < 10:
		return "STOP";
	elif distance < 30:
		return "SLOW";
	else :
		return "GO";
"""
class Sensor:
	total_checks = 0;

	def __init__(self, name, threshold):
		self.name = name;
		self.threshold = threshold;

	def check(self, distance):
		Sensor.total_checks += 1;

		if distance < self.threshold:
			return "STOP";

		elif distance < 3*self.threshold:
			return "SLOW";

		else :
			return "GO";

class Robot:
	def __init__(self, name):
		self.name = name;
		self.sensors = [];

	def add_sensors(self, sensor):
		self.sensors.append(sensor);

	def run_check(self, readings):
		for i in self.sensors:
			print(i.name + ":" + i.check(readings[i.name]))


readings = {"S1" : 8, "S2" : 25, "S3" : 40}

S1 = Sensor("S1", 10);
S2 = Sensor("S2", 10);
S3 = Sensor("S3", 10);

robot1 = Robot("robot1");

robot1.add_sensors(S1);
robot1.add_sensors(S2);
robot1.add_sensors(S3);


robot1.run_check(readings)

print(Sensor.total_checks)
