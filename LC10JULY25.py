class Solution():
    def longestString(self, arr):
        # code here
        
        dic = {}
        ans = ''
        # res= []
        for i in arr:
            dic[i]=1
        n = len(arr)
        for i in arr:
            s= ''
            l = len(i)
            for j in i:
                s+=j
                if dic.get(s,0)==0:
                    l=0
                    break
            # print(ans,l,i)
            l_ans =len(ans)
            if l_ans<=l: 
                if l_ans == l:
                    ans = min (ans,i)
                else:
                    ans = i
                # res.append(i)
                
        return ans 
        # code here
        
        
