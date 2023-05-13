import multiprocessing
import time
import random

class ServiceRegistry:
    def __init__(self):
        self.nodes = []

    def register_node(self, node_id):
        self.nodes.append(node_id)

    def unregister_node(self, node_id):
        self.nodes.remove(node_id)

    def get_nodes(self):
        return self.nodes

def generate_node_id():
    current_time_ms = int(time.time() * 1000)
    random_number = random.randint(1, 1000)
    return current_time_ms + random_number

def start_election():

    print("Starting election...")

def crack_password(password):

    return "Cracked: " + password

def master_task(passwords, service_registry):

    nodes = service_registry.get_nodes()


    workload_size = len(passwords) // len(nodes)
    schedules = []


    for i, node_id in enumerate(nodes):
        start_index = i * workload_size
        end_index = start_index + workload_size if i < len(nodes) - 1 else None
        schedule = passwords[start_index:end_index]
        schedules.append((node_id, schedule))


    for node_id, schedule in schedules:

        print("Sending schedule to node", node_id, ":", schedule)

    for password in passwords:



        for node_id in nodes:

            print("Waiting for response from node", node_id)


        for node_id in nodes:
            # Placeholder code for sending completion message to nodes
            print("Sending completion message to node", node_id)

def slave_task(node_id):

    print("Slave node", node_id, "waiting for schedules...")

if __name__ == '__main__':

    service_registry = ServiceRegistry()


    node_id = generate_node_id()


    service_registry.register_node(node_id)


    if len(service_registry.get_nodes()) == 1:
        wait_time = random.randint(1, 10)
        print("No leader found. Waiting for", wait_time, "seconds before starting an election...")
        time.sleep(wait_time)
        start_election()


    with open("passwords.txt", "r") as file:
        passwords = file.read().splitlines()


    passwords = [password for password in passwords if len(password) == 6 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password)]

    if node_id == service_registry.get_nodes()[0]:
        master_task(passwords, service_registry)
    else:
        slave_task(node_id)
