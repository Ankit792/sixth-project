import sys
def shortestpath(graph,start,end,visited=[],distances={},predecessors={}):

    # detect if first time through, set current distance to zero
    if not visited : distances[start]=0

    # if we've found our end node, find the path to it, and return
    if start==end:
        path=[]
        while end != None:
            path.append(end)
            end=predecessors.get(end,None)
        return distances[start], path[::-1]

    # process neighbors as per algorithm, keep track of predecessors
    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor,sys.maxsize)
            tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor]=start

    # neighbors processed, now mark the current node as visited
    visited.append(start)

    # finds the closest unvisited node to the start
    unvisiteds = dict((k, distances.get(k,sys.maxsize))
                      for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)

    # now take the closest node and recurse, making it current
    return shortestpath(graph,closestnode,end,visited,distances,predecessors)

graph = {'0': {'1': 4, '7': 8},
        '1': {'0': 4, '2': 8, '7': 11},
        '2': {'1': 8,'8': 2, '5': 4, '3': 7},
        '7': {'0': 8, '1': 11, '8': 7, '6': 1},
        '6': {'7': 1, '8': 6, '5': 2},
        '5': {'6':2, '2': 4, '3': 14, '4': 10},
        '3': {'2': 7, '4': 9, '5': 14},
        '4': {'5': 10, '3': 9},
        '8': {'2': 2, '6': 6,'7': 7}
         }
print("The shortest path from the source node '0' to the destination node '5' is {0} ".format(shortestpath(graph,'0','5')))