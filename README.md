# Alexa LAN API Integration

Bored of tutorials about labda functions and online stuff?
Here is a simple way to integrate your Amazon Echo/Dot in your new whatever.

The main part of the project is a Java code edited from Armzilla repo.
The Java Server emulates a Hue bridge, it then sends the list of devices to Alexa and when you say Alexa set "whatever" at 50% it sends a request to the Java Server that redirects the request as a JSON to a desired IP or address.

## Release notes:

Java Server  v0.4.0

Change log:

* require --upnp.config.address= to be specified during startup
* support more than 25 emulated devices currently set to 75, can be increased at 25 device increments by specifying --emulator.portcount= default is 3 thus 3*25 = 75 total devices. Works by taking emulator.baseport and opening n number of ports sequentially from baseport to baseport+portcount
* relaxed http response codes to anything in the 200 to less than 300 http response codes to support misbehaving resources

other notes:
Ive seen some folks able to run this but not able to discover devices. I would recommend checking for devices with duplicate names as i have seen this to cause the echo to reject all devices. The lazy way would be to delete the /data directory and start over.

Python Server  v0.2.1a

Change log:

* Using Flask to handle various request with a single server.

Node Server  v0.1a

* Still developing the detection it seems to work whenever he whats to.


## Quick Start install Java Server

You need to built the Server that is going to run on the Intel Edison or any other platform or use the pre-built one just make sure you use the flags ```--upnp.config.address``` and ```--server.port``` to override the hardcoded values currently implemented.

**Java -** ```java -jar amazon-echo-bridge-*.jar```

**Maven -** ```mvn spring-boot:run```

**Examples:** ``--upnp.config.address=192.168.1.240 --server.port=8081``

After the application is started and running, you can access the configurator by accessing http://YOURIP:PORT/configurator.html. 

Instruct your Amazon Echo to learn about your devices by saying "Alexa, discover my devices" and your all set!

## Build

In case you would like to internally configure your own build of the Amazon Echo Bridge, a few requisites are required.

### Install Maven: 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Ubuntu/Linux** - ```sudo apt-get install maven```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
**OS X** - Install [Homebrew](http://brew.sh/) and run ```brew install maven```

### Make Changes:
For instance, the server defaults to running on port 8080. If you're already running a server (like openHAB) on 8080, you could edit ```server.port``` in ```Java_API_Server/src/main/resources/application.properties``` to your desired port before building the jar. 

Alternatively you could also pass in a command line argument to override ```server.port```.

### Compile:
To build the jar file yourself, make your changes and simply run Maven like this:
```
mvn install
```

Then locate the jar and start the server using the instructions above. By default maven will put the jar file in the target directory. ```java -jar target/amazon-echo-bridge-*.jar``` 

### Python Server Req:

It requires Flask and Request to be installed

### Node Server Req:

Node Server is based on this repo here https://github.com/hortinstein/node-dash-button
is required to sense when the button is pressed and then it will send a post to the Python Server

### Watchdog Folder:

It contains 3 scripts, one for each server, the main function of those scripts is to keep alive the 3 servers, they need to be put into a crontab line and they need to run every minute to keep stuff alive.

# Video of it working:

https://youtu.be/r7PsyCOyaZ8##






