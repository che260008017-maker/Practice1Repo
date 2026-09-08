

stop="Stop";
slow="Slow";
go="Go";

readings = {"left" : 8, "center" : 25, "right" : 40};
stopped_sensors = [];

def decide(x, y):
	if x < 10:
		print(stop);
		stopped_sensors.append(i);
	elif  x  < 30 :
		print(slow);
	else :
		print(go);

for i in readings :
	decide(readings[i], i);


while True:
	if len(stopped_sensors) > 0:			# I think you can  use some function that directly checks if list is empty (list.empty())? 
		print("Counting Down..",end='\n');
		for j in range(3):
			print(j+1, end='\n');
		else :
			print("HALT")
			break;
	else:
		break;


print("End of Execution");
