class Solution {
  public:
    int nonLisMaxSum(vector<int>& arr) {
        int n = arr.size();
        vector <int> tailIdx(n, 0);
        vector <int> prevIdx(n, -1);
        
        int length = 1;
        
        for(int i = 0; i < n; i++){
            if(arr[i] < arr[tailIdx[0]]) tailIdx[0] = i;
            else if(arr[i] > arr[tailIdx[length - 1]]){
                prevIdx[i] = tailIdx[length - 1];
                tailIdx[length++] = i;
            }
            else{
                int l = -1, r = length - 1;
                while(r-l > 1){
                    int m = l + (r-l)/2;
                    if(arr[tailIdx[m]] >= arr[i]) r = m;
                    else l = m;
                }
                
                if(arr[i] <= arr[tailIdx[r]]){
                    if(r > 0) prevIdx[i] = tailIdx[r - 1];
                    tailIdx[r] = i;
                }
            }
        }
        
        int sum = accumulate(arr.begin(), arr.end(), 0);
        int idx = tailIdx[length - 1];
        
        while(idx >= 0){
            sum -= arr[idx];
            idx = prevIdx[idx];
        }
        
        return sum;
    }
};
