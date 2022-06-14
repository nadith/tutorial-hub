
import ray
import time

# Start Ray head node on a separate PC
# ray start --head --port=8000  # will start the head with 127.0.0.1 which can only be accessed locally.
# ray start --head --port=8000 --node-ip-address=192.168.1.117   # will start the head with 192.168.1.117 (can be accessed globally)
# ray start --address=192.168.1.117:8000 --node-ip-address=192.168.1.103


# Start Ray.
# ray.init(address='auto', _node_ip_address='192.168.1.117')

@ray.remote
def f(x):
    time.sleep(1)
    return x

# Start 4 tasks in parallel.
result_ids = []
for i in range(4):
    result_ids.append(f.remote(i))
    
# Wait for the tasks to complete and retrieve the results.
# With at least 4 cores, this will take 1 second.
results = ray.get(result_ids)  # [0, 1, 2, 3]
print(results)