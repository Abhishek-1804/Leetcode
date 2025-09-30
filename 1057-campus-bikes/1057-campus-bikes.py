class Solution:
    def assignBikes(self, workers, bikes):
        from itertools import product

        num_workers = len(workers)
        num_bikes = len(bikes)
        distance_pairs = []

        for worker_idx, bike_idx in product(range(num_workers), range(num_bikes)):
            distance = abs(workers[worker_idx][0] - bikes[bike_idx][0]) + abs(workers[worker_idx][1] - bikes[bike_idx][1])
            distance_pairs.append((distance, worker_idx, bike_idx))

        distance_pairs.sort()

        worker_assigned = [False] * num_workers
        bike_assigned = [False] * num_bikes
        result = [0] * num_workers

        for distance, worker_idx, bike_idx in distance_pairs:
            if not worker_assigned[worker_idx] and not bike_assigned[bike_idx]:
                worker_assigned[worker_idx] = True
                bike_assigned[bike_idx] = True
                result[worker_idx] = bike_idx
                
        return result