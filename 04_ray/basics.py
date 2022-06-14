# Ref: https://www.youtube.com/watch?v=LmROEotKhJA


from collections import Counter
from collections import Counter
import socket
import time
import ray


print(socket.gethostbyname(socket.gethostname()))

#ray.init(address='auto')
ray.init(address='ray://192.168.1.117:10001')

print('''This cluster consists of
    {} nodes in total
    {} CPU resources in total
'''.format(len(ray.nodes()), ray.cluster_resources()['CPU']))

@ray.remote
def f():
    time.sleep(0.001)
    # Return IP address.
    return socket.gethostbyname(socket.gethostname())


object_ids = [f.remote() for _ in range(100000)]
ip_addresses = ray.get(object_ids)
print(Counter(ip_addresses))


# C:\Users\chath\anaconda3\lib\site-packages\ray\util\client\worker.py:599: 
# UserWarning: More than 10MB of messages have been created to schedule tasks on the server. 
# This can be slow on Ray Client due to communication overhead over the network. If you're
# running many fine-grained tasks, consider running them inside a single remote function. 
# See the section on "Too fine-grained tasks" in the Ray Design Patterns document for more 
# details: https://docs.google.com/document/d/167rnnDFIVRhHhK4mznEIemOtj63IOhtIPvSYaPgI4Fg/edit#heading=h.f7ins22n6nyl. 
# If your functions frequently use large objects, consider storing the objects remotely 
# with ray.put. An example of this is shown in the "Closure capture of
# large / unserializable object" section of the Ray Design Patterns document, available
# here: https://docs.google.com/document/d/167rnnDFIVRhHhK4mznEIemOtj63IOhtIPvSYaPgI4Fg/edit#heading=h.1afmymq455wu