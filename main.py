def genmap():
  path = [
    "container",
    "process",
    "thread",
    "socket"
  ]
  servers = ["node1", "node2", "node3"]
  data = {

    "container": ["javaapp1", "microservice1"],
    "process": ["javaappprocess"],
    "thread": ["recvthread", "sendthread"],
    "socket": ["user1socket"]
  }
  
  results = []
  for server in servers:
    result = ""
    for item in path:
      
      
      for instance in data[item]:
          subinstance = str(server)
          subinstance += instance + "."
          results.append(subinstance)
  
  print(results)

genmap()
    