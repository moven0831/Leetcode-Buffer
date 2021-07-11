"""Need to learn how to form a graph to judge"""
"""Whether if there's no cycle in it"""

import collections
"""DAG + DFS"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: '''List[List[int]]''') -> bool:
        graph = collections.defaultdict(list)
        visited = [0] * numCourses
        for pre, after in prerequisites:
            graph[pre].append(after)
        print(graph)
        print(visited)
        for i in range(numCourses):
            if not self.dfs(graph=graph, visited=visited, i=i):
                return False
        return True
    
    # 0 = unprocessed, 1 = processing, 2 = processed
    def dfs(self, graph, visited, i):
        # when dfs find there's a processing node
        # It indicates that the DAG has cycle. Thus return False
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        
        # If visited == 0, then set it as processing
        visited[i] = 1

        # loop through through each node in the graph[i]
        for j in graph[i]:
            if not self.dfs(graph=graph, visited=visited, i=j):
                return False
        
        # If the process of looping graph[i] is completed without False
        # Then set it as processed
        visited[i] = 2
        return True


result = Solution().canFinish(numCourses=4, prerequisites=[[0,1],[1,2],[2,3]])
print(result)


"""第一次嘗試，因無法判斷環而失敗"""
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: '''List[List[int]]''') -> bool:
#         graph = dict()
#         for each in prerequisites:
#             if each[1] not in graph:
#                 graph[each[1]] = [each[0],]
#             else:
#                 graph[each[1]].append(each[0])
#         print(graph)

#         takedCourses = set()
#         for pre, after in graph.items():
#             takedCourses.add(pre)
#             for each in after:
#                 if each in graph.keys() and pre in graph[each]:
#                     return False
#                 takedCourses.add(each)
#         print(takedCourses)

#         if numCourses >= len(takedCourses):
#             return True
#         else:
#             return False
        

# result = Solution().canFinish(numCourses=5, prerequisites=[[1,0],[0,2],[2,1]])
# print(f'RESULT:{result}')



"""根據課程建制關係建立有向圖，判斷這個圖是否存在環"""
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         inbound = [0] * numCourses
#         edge = defaultdict(list)
#         for x, y in prerequisites:
#             inbound[x] += 1
#             edge[y].append(x)
#         q = [i for i in range(numCourses) if inbound[i] == 0]
#         visited = 0
#         while q:
#             cur = q.pop()
#             visited += 1  
#             for n in edge[cur]:
#                 inbound[n] -= 1
#                 if inbound[n] == 0:
#                     q.append(n)
#         return  visited == numCourses
        