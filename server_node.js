const http = require('http');
const url = require('url');

const hostname = '127.0.0.1';
const port = 3000;
var grid = [];

const server = http.createServer((req, res) => {
	const { headers, method, url } = request;
	res.setHeader('Content-Type', 'text/plain');
    switch(url){
        case '/receive_data':
			if (method != "POST") {
				response.statusCode = 400;
				res.end("Invalid Request");
				break;
			}
			response.statusCode = 200;
			let body = [];
			request.on('data', (chunk) => {
				body.push(chunk);
			}).on('end', () => {
				body = Buffer.concat(body).toString();
				grid += body
			});
            res.end('Data Received');
        break;
		case '/request_data':
			response.statusCode = 200;
			res.end(grid);	
		break;
        default:
			response.statusCode = 400;
            res.end('Invalid URL');
        break;
    }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
