import xmlrpc.client

server_ip = "http://20.188.114.10:8000/RPC2"

try:
    proxy = xmlrpc.client.ServerProxy(server_ip)

    print("Connected to RPC Server")

    result1 = proxy.add(10, 20)
    print("Addition Result:", result1)

    result2 = proxy.multiply(5, 6)
    print("Multiplication Result:", result2)

except Exception as e:
    print("Error:", e)
