// Ben Webb
// Ying Li
// node.js
// Project 3

var http = require('http');
var fs = require('fs');
var url = require('url');
var querystring = require('querystring');

// Create server
http.createServer(
    function (req, resp) {
        // Parse the request containing file name
        var pathname = url.parse(req.url, true).pathname;
        var query = url.parse(req.url, true).query;
                  
        // Print the name of the file
        console.log('Request for ' + pathname);
        switch (pathname.substr(-4)) {
             // If the request if asking for an IP
            case "calc":
                  // Find prefix fields.
                  var prefix = (0xFFFFFFFF ^ (1 << (32 - query.preflen)) - 1);
                  var ma = (prefix >> 24) & 0xFF;
                  var mb = (prefix >> 16) & 0xFF;
                  var mc = (prefix >> 8 ) & 0xFF;
                  var md = (prefix) & 0xFF;
                  // Store result in JSON
                  var result = {
                  subnet: (query.b1 & ma) + '.' + (query.b2 & mb) + '.' + (query.b3 & mc) + '.' + (query.b4 & md),
                  first: (query.b1 & ma) + '.' +  (query.b2 & mb) + '.' + (query.b3 & mc) + '.' + ((query.b4 & md) + 1),
                  entered: query.b1 + '.' + query.b2 + '.' + query.b3 + '.' + query.b4,
                  last: ((query.b1 & ma)|(255^ma)) + '.' + ((query.b2 & mb)|(255^mb)) + '.' + ((query.b3 & mc)|(255^ mc)) + '.' + (((query.b4 & md)|(255^ md)) - 1),
                    broadcast: ((query.b1 & ma)|(255^ma)) + '.' + ((query.b2 & mb)|(255^mb)) + '.' + ((query.b3 & mc)|(255^ mc)) + '.' + ((query.b4 & md)|(255^ md)),
                  netmask: ma + '.' + mb + '.' + mc + '.' + md
                  };
              
                  // Write response
                  resp.writeHead(200, {'Content-Type': 'text/html'});
                  resp.write(JSON.stringify(result));
                  resp.end();
                  break;
            default:
                  // Read the requested file content from file system
                  fs.readFile(pathname.substr(1), function (err, data) {
                  if (err) {
                    console.log(err);
                    resp.writeHead(404, {'Content-Type': 'text/html'});
                  } else {
                        var dotoffset = req.url.lastIndexOf('.');
                        var mimetype = dotoffset == -1
                              ? 'text/plain'
                              : {
                              '.html' : 'text/html',
                              '.ico' : 'image/x-icon',
                              '.jpg' : 'image/jpeg',
                              '.png' : 'image/png',
                              '.gif' : 'image/gif',
                              '.css' : 'text/css',
                              '.js' : 'text/javascript'
                              }[ req.url.substr(dotoffset) ];
                              resp.setHeader('Content-type' , mimetype);
                    resp.write(data.toString());
                }
                // Send response body
                resp.end();
            });
        }
    }
).listen(8000);
// Console will print the message
console.log('Server running at http://localhost:8000/');
