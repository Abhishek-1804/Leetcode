class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        import collections
        
        bank_set = set(bank)
        n = len(startGene)
        q = collections.deque([(startGene, 0)])
        gene_chars = "ACTG"
        
        while q:
            curr_gene, mutations = q.popleft()
            
            for i in range(len(curr_gene)):
                for char in gene_chars:
                    if curr_gene[i] != char:
                        new_gene = curr_gene[:i] + char + curr_gene[i+1:]
                        
                        if new_gene in bank_set:
                            if new_gene == endGene:
                                return mutations+1
                            q.append((new_gene, mutations + 1))
                            bank_set.remove(new_gene)
            
        return -1