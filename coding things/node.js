var http = require('http');
var fs = require('fs');
var url = require('url');
var querystring = require('querystring');
// Create a server
http.createServer(
    function (req, resp) {
        // Parse the request containing file name
        var pathname = url.parse(req.url, true).pathname;
        var query = url.parse(req.url, true).query;
        // Print the name of the file for which request is made
        console.log('Request for ' + pathname + ' received.');
                  
        if (req.method === 'GET' && pathname === '/prefcalc') {
            prefix = (0xFFFFFFFF ^ (1 << (32 - query.preflen)) - 1);
            ma = (prefix >> 24) & 0xFF;
            mb = (prefix >> 16) & 0xFF;
            mc = (prefix >> 8 ) & 0xFF;
            md = (prefix) & 0xFF;

            var result = {
                subnet: (query.b1 & ma) + '.' + (query.b2 & mb) + '.' + (query.b3 & mc) + '.' + (query.b4 & md),
                first: (query.b1 & ma) + '.' +  (query.b2 & mb) + '.' + (query.b3 & mc) + '.' + ((query.b4 & md) + 1),
                entered: query.b1 + '.' + query.b2 + '.' + query.b3 + '.' + query.b4,
                last: ((query.b1 & ma)|(255^ma)) + '.' + ((query.b2 & mb)|(255^mb)) + '.' + ((query.b3 & mc)|(255^ mc)) + '.' + (((query.b4 & md)|(255^ md)) - 1),
                broadcast: ((query.b1 & ma)|(255^ma)) + '.' + ((query.b2 & mb)|(255^mb)) + '.' + ((query.b3 & mc)|(255^ mc)) + '.' + ((query.b4 & md)|(255^ md)),
                netmask: ma + '.' + mb + '.' + mc + '.' + md
                };
                  
            resp.writeHead(200, {'Content-Type': 'text/html'});
            resp.write(JSON.stringify(result));
            resp.end();
                  
        } else {

            // Read the requested file content from file system
            fs.readFile(pathname.substr(1), function (err, data) {
            if (err) {
                console.log(err);
                // HTTP Status: 404 : NOT FOUND
                // Content Type: text/plain
                resp.writeHead(404, {'Content-Type': 'text/html'});
            } else {
                // Page found
                // HTTP Status: 200 : OK
                // Content Type: text/plain
                resp.writeHead(200, {'Content-Type': 'text/html'});
                // Write the content of the file to response body
                resp.write(data.toString());
            }
            // Send the response body
            resp.end();
            });
        }
    }
).listen(8000);
// Console will print the message
console.log('Server running at http://localhost:8000/');
