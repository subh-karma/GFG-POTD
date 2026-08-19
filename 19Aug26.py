geeksforgeeks
Search...
Courses
Tutorials
Practice
Jobs

99+
avatar



Discussions
( 34 Threads )

Most Recent
User





Commenting as Subhasish karmakar

Comment Anonymously
Submit
💡
Discussion Guidelines
×
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.
User
Sunil Kumar
(Edited)
8 minutes agoAug 19, 2026 07:43 (GMT +5:30)

Step-by-step logic


Sort the array so binary search can be used.
Pick two elements arr[i] and arr[j].
Calculate their sum:
s = arr[i] + arr[j]
The third element must satisfy:
l - s <= arr[k] <= r - s
Use:
bisect_left() → first valid k
bisect_right() → position after last valid k
Make sure k > j.
Add the number of valid k values to ans.
..... see more

0

Reply
User
Jingyi Wang
2 hours agoAug 19, 2026 05:46 (GMT +5:30)

class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        # code here
        from bisect import bisect_left, bisect_right
        arr.sort()
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                s = arr[i]+arr[j]
                k1 = bisect_left(arr, l-s)
                k1 = max(k1, j+1)
                k2 = bisect_right(arr, r-s)
                #k2 = min(k2, n)
                ans += max(0, k2-k1)
        return ans
 

..... see less

1

Reply
User
Mateusz Dereniowski
6 hours agoAug 19, 2026 01:21 (GMT +5:30)

    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        n = len(arr)
        arr.sort()

        def at_most(maxi: int) -> int:
            count = 0
            for i in range(n - 2):
                j, k = i + 1, n - 1
                while j < k:
                    if arr[i] + arr[j] + arr[k] <= maxi:
                        count += k - j
                        j += 1
                    else:
                        k -= 1
            return count

        return at_most(r) - at_most(l - 1)
..... see more

3

Reply
User
JAI ALWIN M
7 hours agoAug 19, 2026 00:43 (GMT +5:30)

Approach:
1. Sort the array.
2. Count the number of triplets having sum <= x using two pointers.
3. For each fixed element arr[i], use left and right pointers.
4. If arr[i] + arr[left] + arr[right] <= x, then all elements
   between left and right form valid triplets, so add (right - left).
5. Otherwise, decrease right.
6. The required answer is:
      count(sum <= r) - count(sum <= l - 1).

Time Complexity: O(n^2)
Space Complexity: O(1) auxiliary space

class Solution {
public:
    long long countLessEqual(vector<int>& arr, int x) {
        int n = arr.size();
        long long count = 0;

        for (int i = 0; i < n - 2; i++) {
            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                int sum = arr[i] + arr[left] + arr[right];

                if (sum <= x) {
                    count += right - left;
                    left++;
                } else {
                    right--;
                }
            }
        }

        return count;
    }

    int countTriplets(vector<int>& arr, int l, int r) {
        sort(arr.begin(), arr.end());

        return countLessEqual(arr, r) -
               countLessEqual(arr, l - 1);
    }
};

..... see more

1

Reply
User
Thirumurugan
7 hours agoAug 19, 2026 00:31 (GMT +5:30)

class Solution:
    def solve(self, arr, n):
        t = 0
        for i in range(len(arr)):
            l, r = i + 1, len(arr) - 1
            need = n - arr[i]
            while l < r:
                if arr[l] + arr[r] <= need:
                    t += r - l
                    l += 1
                else:
                    r -= 1
        return t

    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        # code here
        arr.sort()
        return self.solve(arr, r) - self.solve(arr, l - 1)
 

..... see more

1

Reply
User
Anamika
7 hours agoAug 19, 2026 00:09 (GMT +5:30)

 

class Solution {
public:
    long long countT(vector<int>& arr, int n, long long x) {
        long long ans = 0;
        for (int i = 0; i < n - 2; i++) {
            int j = i + 1 , k = n - 1;
            while (j < k) {
                long long sum = (long long)arr[i] + arr[j] + arr[k];
                if (sum <= x) {
                    ans += (k - j);
                    j++;
                } 
                else {
                    k--;
                }
            }
        }
        return ans;
    }
    long long countTriplets(vector<int>& arr, int l, int r) {
        int n = arr.size();
        sort(arr.begin(), arr.end());
        return countT(arr, n, r) - countT(arr, n, (long long)l - 1);
    }
};
 

..... see more

0

Reply
User
Anonymous_Geek
7 hours agoAug 19, 2026 00:08 (GMT +5:30)

//C++ Perfect Solution 




class Solution {
  public:

    long long countLessEqual(vector<int>& arr, int x) {
        int n = arr.size();
        long long count = 0;

        for (int i = 0; i < n - 2; i++) {
            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                long long sum = (long long)arr[i] + arr[left] + arr[right];

                if (sum <= x) {
                    count += right - left;
                    left++;
                } else {
                    right--;
                }
            }
        }

        return count;
    }

    int countTriplets(vector<int> &arr, int l, int r) {
        sort(arr.begin(), arr.end());

        return countLessEqual(arr, r) - countLessEqual(arr, l - 1);
    }
};

..... see more

0

Reply
User
Amit Maurya
7 months agoJan 09, 2026 09:33 (GMT +5:30)

import java.util.Arrays;

class Solution {

    static int solve(int[] arr, int n, int X) {
        Arrays.sort(arr);
        int count = 0;

        for (int i = 0; i < n - 2; i++) {
            int j = i + 1;
            int k = n - 1;

            while (j < k) {
                if (arr[i] + arr[j] + arr[k] <= X) {
                    count += (k - j);
                    j++;
                } else {
                    k--;
                }
            }
        }
        return count;
    }

    static int countTriplets(int[] Arr, int N, int L, int R) {
        return solve(Arr, N, R) - solve(Arr, N, L - 1);
    }
}---------------Optimize APPROACH 

..... see more

1

Reply
User
Amit Maurya
7 months agoJan 09, 2026 09:19 (GMT +5:30)

class Solution {
    static int countTriplets(int Arr[], int N, int L, int R) {
        int count=0;
        Arrays.sort(Arr);
        for(int i=0;i<Arr.length;i++){
          for(int j=i+1;j<Arr.length;j++){
              for(int k=j+1;k<Arr.length;k++){
                  int sum=Arr[i]+Arr[j]+Arr[k];
                  if(sum>=L && sum<=R){
                      count++;
                  }
              }
          }
        }
          return count;
        
        
    }
}

..... see more

1

Reply
User
Mukesh Kumar Pathak
11 months agoSep 12, 2025 19:25 (GMT +5:30)

class Solution {
  public:
    int countT(int arr[], int n, int x){
        int ans = 0;
        for(int i=0;i<n-2;i++){
            int j = i+1;
            int k = n-1;
            
            while(j<k){
                if((arr[i]+arr[j]+arr[k]) <= x){
                    ans += (k-j);
                    j++;
                }else{
                    k--;
                }
                
            }
            
        }
        return ans;
    }
  
    int countTriplets(int Arr[], int N, int L, int R) {
        // code here
        sort(Arr, Arr+N);
        return countT(Arr, N, R) - countT(Arr, N, L-1);
    }
};

..... see more

0

Reply
Output Window
Your program took more time than expected.
Hint : Please optimize your code and submit again.

Geek Tip:
Your code is taking more time than expected. Reduce its time complexity by optimising your code.
You can access the hint section to get an idea about what is expected of you. Please note that this will impact your score.
Python3



            # code here
            



Custom Input
