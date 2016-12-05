#proto req: {"on": true,"bri":255}


from flask import Flask, request, url_for
import json
import mraa

app = Flask(__name__)

@app.route('/red', methods=['GET', 'POST'])
def red():
	print("red")

	js=json.dumps(request.get_json())
	js=json.loads(js)
	#print("recived data: "+str(js["on"]))
	#print("recived data: "+str(js["bri"]))
	if (js["on"]==False):
		red.write(1)
		return "200"
	if (js["on"]==True and len(js)==1):
		red.write(0)
		return "200"
	if len(js)>1:
		pwmvalue=float(js["bri"])/255.0000
		pwmvalue=round(pwmvalue,2)
		red.write(1-pwmvalue)
		print(1-pwmvalue)

	return "200"

@app.route('/blue', methods=['GET', 'POST'])
def blue():
	print("blue")

	js=json.dumps(request.get_json())
	js=json.loads(js)
	#print("recived data: "+str(js["on"]))
	#print("recived data: "+str(js["bri"]))
	if (js["on"]==False):
		blue.write(1)
		return "200"
	if (js["on"]==True and len(js)==1):
		blue.write(0)
		return "200"
	if len(js)>1:
		pwmvalue=float(js["bri"])/255.0000
		pwmvalue=round(pwmvalue,2)
		blue.write(1.00-pwmvalue)
		print(1.00-pwmvalue)
		
	return "200"

@app.route('/green', methods=['GET', 'POST'])
def green():
	print("green")

	js=json.dumps(request.get_json())
	js=json.loads(js)
	#print("recived data: "+str(js["on"]))
	#print("recived data: "+str(js["bri"]))
	if (js["on"]==False):
		green.write(1)
		return "200"
	if (js["on"]==True and len(js)==1):
		green.write(0)
		return "200"
	if len(js)>1:
		pwmvalue=float(js["bri"])/255.0000
		pwmvalue=round(pwmvalue,2)
		green.write(1.00-pwmvalue)
		print(1-pwmvalue)
		
	return "200"

@app.route('/all', methods=['GET', 'POST'])
def all():
	print("all")
	js=json.dumps(request.get_json())
	js=json.loads(js)
	#print("recived data: "+str(js["on"]))
	#print("recived data: "+str(js["bri"]))
	if (js["on"]==False):
		red.write(1)
		blue.write(1)
		green.write(1)
		return "200"
	if (js["on"]==True and len(js)==1):
		red.write(0)
		blue.write(0)
		green.write(0)
		return "200"
	if len(js)>1:
		pwmvalue=float(js["bri"])/255.0000
		pwmvalue=round(pwmvalue,2)
		red.write(1.00-pwmvalue)
		blue.write(1.00-pwmvalue)
		green.write(1.00-pwmvalue)
		print(1-pwmvalue)
		
	return "200"

if __name__ == '__main__':
	red = mraa.Pwm(14)
	blue = mraa.Pwm(21)
	green = mraa.Pwm(0)
	red.period_us(700)
	blue.period_us(700)
	green.period_us(700)
	red.enable(True)
	blue.enable(True)
	green.enable(True)
	red.write(1)
	blue.write(1)
	green.write(1)
	app.run( 
		host="0.0.0.0",
		port=int("5000")
  )
