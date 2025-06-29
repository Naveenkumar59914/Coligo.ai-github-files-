
from opcua import Server
import time
import random
from datetime import datetime
import csv

# Create OPC UA Server
server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840")
uri = "http://example.org/energy"
idx = server.register_namespace(uri)

objects = server.get_objects_node()
factory = objects.add_object(idx, "Factory")
energy_var = factory.add_variable(idx, "EnergyUsage", 0.0)
energy_var.set_writable()

# CSV Logger
with open("energy_log.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "EnergyUsage"])

    server.start()
    print("✅ OPC UA Server running at opc.tcp://localhost:4840")

    try:
        while True:
            value = round(random.uniform(10, 100), 2)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            energy_var.set_value(value)
            writer.writerow([timestamp, value])
            print(f"[{timestamp}] Energy: {value}")
            time.sleep(2)

    except KeyboardInterrupt:
        print("Shutting down server...")
        server.stop()
