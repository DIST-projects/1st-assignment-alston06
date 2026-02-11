from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to particular path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create Server
server = SimpleXMLRPCServer(("0.0.0.0", 8000),
                            requestHandler=RequestHandler,
                            allow_none=True)

server.register_introspection_functions()

print("RPC Server started on port 8000...")

# Remote procedures
def add(a, b):
    print("Add request received")
    return a + b

def multiply(a, b):
    print("Multiply request received")
    return a * b

# Register functions
server.register_function(add, "add")
server.register_function(multiply, "multiply")

# Run server
server.serve_forever()
