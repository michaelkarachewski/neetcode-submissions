class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)

        for num in nums:
            mp[num] += 1
        

        pq = []

        for key in mp:
            heapq.heappush(pq, (mp[key],key))
            if len(pq)>k:
                value, key = heapq.heappop(pq)

        output = []
        for x in range(k):
            value, key = heapq.heappop(pq)
            output.append(key)

        print(pq)

        return output[::-1]



        