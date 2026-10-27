class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # First we construct the adjacency list
        adj_list = {}
        in_degrees = {}
        for spec in prerequisites:
            course, prereq = spec
            prev_adj_list = adj_list.get(prereq, [])
            prev_adj_list.append(course)
            adj_list[prereq] = prev_adj_list
            in_degrees[course] = in_degrees.get(course, 0) + 1
        
        # Find initial sources:
        sources = []
        for course in adj_list:
            if course not in in_degrees:
                sources.append(course)
    
        # Remove sources iteratively until there are only loops left
        while sources:
            source = sources.pop()
            if source not in adj_list:
                continue
    
            for adj in adj_list[source]:
                in_degrees[adj] -= 1
                if in_degrees[adj] == 0:
                    sources.append(adj)
            
            del adj_list[source]

        if adj_list:
            return False
        return True