var http = require('http');
var server = http.createServer(function(req, res) {
	res.writeHead(200, {'Content-Type': 'text/HTML'});
	res.end('<HTML><body><marquee align="middle" bgcolor="red">Hello</marquee></body></HTML>')});
server.listen(8080, '192.168.1.79');
console.log('Running!');
