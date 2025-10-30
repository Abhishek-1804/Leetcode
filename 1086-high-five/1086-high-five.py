class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        import heapq
        
        avg_scores = {}

        for id_, score in items:
            if id_ not in avg_scores:
                avg_scores[id_] = []
            
            if len(avg_scores[id_]) < 5:
                heapq.heappush(avg_scores[id_], score)

            elif len(avg_scores[id_]) == 5 and score > avg_scores[id_][0]:
                heapq.heappop(avg_scores[id_])
                heapq.heappush(avg_scores[id_], score)
            
            else:
                continue
        
        output = []

        for key, scores in avg_scores.items():
            output.append([key, sum(scores)//len(scores)])
        
        return sorted(output, key = lambda x : x[0])