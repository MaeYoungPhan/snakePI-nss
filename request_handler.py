from urllib.parse import urlparse, parse_qs
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import (all, single, get_snakes_by_species, create_snake)


method_mapper = {
    'single': single, 'all': all
}

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    def get_all_or_single(self, resource, id):
        """Determines whether the client is needing all items or a single item and then calls the correct function.
        """
        if id is not None:
            response = method_mapper["single"](resource, id)

            if response is None:
                self._set_headers(404)
                response = ''
            elif response == '':
                self._set_headers(405)
            else:
                self._set_headers(200)
        else:
            response = method_mapper["all"](resource)

            if response is not None:
                self._set_headers(200)
            else:
                self._set_headers(404)
                response = ''

        return response

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')  # ['', 'animals', 1]
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def do_GET(self):
        """Handles GET requests to the server
        """
        # Parse URL and store entire tuple in a variable
        parsed = self.parse_url(self.path)

        if '?' not in self.path:
            response = None
            (resource, id) = parsed
            response = self.get_all_or_single(resource, id)

        else: # There is a ? in the path, run the query param functions
            response = {}
            (resource, query) = parsed

            # see if the query dictionary has a species key
            if query.get('species') and resource == 'snakes':
                self._set_headers(200)
                response = get_snakes_by_species(query['species'][0])

        self.wfile.write(json.dumps(response).encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        """Handles POST requests to the server"""

    # Set response code to 'Created'
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        if resource == "snakes":
            new_snake = None

            if ("name" in post_body and "ownerId" in post_body and "speciesId" in post_body
            and "gender" in post_body and "color" in post_body):
                self._set_headers(201)
                new_snake = create_snake(post_body)

            else:
                self._set_headers(400)

                new_snake = {
                "message": f'{"name is required"}' if "name" not in post_body else "" f'{"ownerId is required"}' if "ownerId" not in post_body else ""
                f'{"speciesId is required"}' if "speciesId" not in post_body else "" f'{"gender is required"}' if "gender" not in post_body else ""
                f'{"color is required"}' if "color" not in post_body else ""}
            
        else:
            self._set_headers(404)
            new_snake = ''

        self.wfile.write(json.dumps(new_snake).encode())

    # A method that handles any PUT request.
    def do_PUT(self):
        """Handles PUT requests to the server"""
        self._set_headers(404)
        response = ''

        self.wfile.write(json.dumps(response).encode())

    # A method that handles any DELETE request.
    def do_DELETE(self):
        """Handles DELETE requests to the server"""
        self._set_headers(404)

    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
