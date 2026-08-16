class Solution {
  public:
    int minProd(vector<int>& arr) {
        // code here
        int n = arr.size();

        // If all are +ve numbers
        int minnum = INT_MAX;
        bool flag = true; // No -ve
        for(int i=0;i<n;i++){
            if(arr[i]<0){
                flag = false;
                break;
            }
            else minnum = min(minnum,arr[i]);
        }
        if(flag) return minnum;

        // For -ve numbers
        int count = 0;
        for(int i=0;i<n;i++)    if(arr[i]<0) count++;
        int prod = 1;

        if(count % 2 != 0){ // Odd number of -ve numbers
            for(int i=0;i<n;i++){
                if(arr[i]==0) continue;
                else    prod *= arr[i];

            }
            return prod;
        }
        else{ // Even number of -ve numbers
            vector<int>v;
            for(int i=0;i<n;i++) if(arr[i]<0) v.push_back(arr[i]);
            sort(v.begin(),v.end());

            for(int i=0;i<n;i++){
                if(arr[i]==0) continue;
                else if(arr[i]>0) prod *= arr[i];

            }
            for(int i=0;i<v.size()-1;i++) prod *= v[i];

            return prod;
        }


    }
};
