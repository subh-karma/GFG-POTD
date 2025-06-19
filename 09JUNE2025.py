class Solution:
    def caseSort(self,s):
        #code here
        l1=sorted([i for i in s if i.isupper()])
        l2=sorted([i for i in s if i.islower()])
        x=y=0
        l=[]
        for i in s:
            if i.islower():
                l.append(l2[x])
                x+=1
            else:
                l.append(l1[y])
                y+=1
        return ''.join(l)
        #code here
