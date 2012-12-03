var express = require('express');
var app = express();
var server = require('http').createServer(app);
var sleep = require('sleep');
var port = 9001;

server.listen(port);
var SerialPort = require("serialport").SerialPort;
var serialport = new SerialPort("/dev/tty.usbmodem1411");

app.get('/', function(req, res) {
    res.sendfile(__dirname + '/index.html');
    serialport.write(String.fromCharCode(179));
    sleep.sleep(2);
    serialport.write(String.fromCharCode(0));
});
