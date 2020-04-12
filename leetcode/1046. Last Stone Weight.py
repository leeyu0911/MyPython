'''
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
'''
import heapq
class Solution:
    def lastStoneWeight(self, stones: 'List[int]') -> 'int':
        if stones is None:
            return 0

        while len(stones) > 1:
            heapq._heapify_max(stones)
            s1 = heapq._heappop_max(stones) 
            s2 = heapq._heappop_max(stones)
            if s1 != s2:
                # 找不到 max heap push method
                stones.append(s1 - s2)  # s1 > s2 
        
        return stones[0] if stones else 0

print(Solution.lastStoneWeight(0, None))
print(Solution.lastStoneWeight(0, [2,7,4,1,8,1]))
print(Solution.lastStoneWeight(0, [2,2]))

           

# 要求最大值可以將每個值取負號 然後用 min heap pop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_list = [-x for x in stones]
        heapq.heapify(new_list)
        while len(new_list) > 1:
            y = heapq.heappop(new_list)
            x = heapq.heappop(new_list)
            if y != x:
                heapq.heappush(new_list, y-x)
        if len(new_list):
            return -heapq.heappop(new_list)
        return 0
