class Solution:
    def countDistinct(self, arr, k):
        from collections import Counter
        counter = Counter(arr[:k])
        answer = [len(counter)]
        for i in range(len(arr) - k):
            counter[arr[i + k]] += 1
            if counter[arr[i]] == 1:
                del counter[arr[i]]
            else:
                counter[arr[i]] -= 1
            answer.append(len(counter))
        return answer
        
        
