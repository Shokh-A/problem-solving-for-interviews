# Problem:
# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.
# EXAMPLE
# Input:
  # projects: a, b, c, d, e, f
  # dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c

# Brainstorming:
# It is a graph problem. In case graph has a cycle, there is no valid build order.
# Building can start with the projects that have no dependecy, then down the graph.

from typing import List, Tuple

class Solution:

  # Time - O(P+D), where P - the number of projects, D - the number of dependecies.
  def findBuildOrder(self, projects: List[str], dependencies: Tuple[str, str]) -> List[str]:
    buildOrder = []
    unbuilt_projects = set(projects)
    graph = self.buildGraph(projects, dependencies)

    while unbuilt_projects:
      something_built = False
      for project in list(unbuilt_projects):
        dependencies = graph[project]
        if not unbuilt_projects.intersection(dependencies):
          buildOrder.append(project)
          unbuilt_projects.remove(project)
          something_built = True
      if not something_built:
        raise Exception("No valid build order exists.")    

    return buildOrder
  
  def buildGraph(self, projects: List[str], dependencies: Tuple[str, str]):
    graph = dict()

    for proj in projects:
      graph[proj] = []

    for dependecy, proj in dependencies:
      graph[proj].append(dependecy)

    return graph

# Test
sol = Solution()
# Test case 1
print("1st test case", sol.findBuildOrder(projects=['a', 'b', 'c', 'd', 'e', 'f'], 
                                          dependencies=[('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]))
