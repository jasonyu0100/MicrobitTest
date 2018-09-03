const http = require('http');
const url = require('url');

const hostname = '127.0.0.1';
const port = 3000;
let grid = [];


const server = http.createServer((req, res) => {
	const { headers, method, url } = req;
	res.setHeader('Content-Type', 'text/plain');
    switch(url){
        case '/receive_data':
			if (method != "POST") {
				res.statusCode = 400;
				res.end("Invalid POST Request");
			} else {
				res.statusCode = 200;
				let body = [];
				req.on('data', (chunk) => {
					body.push(chunk);
				}).on('end', () => {
					body = Buffer.concat(body).toString();
					body = JSON.parse(body);
					let left = JSON.stringify(body["l"]);
					let right = JSON.stringify(body["r"]);
					grid.push(left,right);
				});
				res.end('Data Received'+body);
			}
        	break;
		case '/request_data':
			res.writeHead(200, {"Access-Control-Allow-Origin":'*'})
			res.end(grid.toString());	
			break;
        default:
			res.statusCode = 400;
            res.end('Root Index');
        	break;
    }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
