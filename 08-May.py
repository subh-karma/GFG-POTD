class Solution {
    public int findMissing(int[] arr) {
        // code here
        int a=-1,b=-1,aCnt=0,bCnt=0;
        for(int i=1;i<arr.length;i++){
            int diff=arr[i]-arr[i-1];
            if(a==-1){
                a=diff;
                aCnt++;
            }else if(a==diff) aCnt++;
            else if(b==-1){
                b=diff;
                bCnt++;
            }else bCnt++;
        }
        
        if(b==-1) return arr[arr.length-1]+a;
        if(aCnt>bCnt){
            for(int i=1;i<arr.length;i++){
                int diff=arr[i]-arr[i-1];
                if(diff!=a) return arr[i-1]+a;
            }
        }else{
            for(int i=1;i<arr.length;i++){
                int diff=arr[i]-arr[i-1];
                if(diff!=b) return arr[i-1]+b;
            }
        }
        return -1;
    }
}
