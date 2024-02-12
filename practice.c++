#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

//53. Maximum Subarray
// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: The subarray [4,-1,2,1] has the largest sum 6.
// Example 2:

// Input: nums = [1]
// Output: 1
// Explanation: The subarray [1] has the largest sum 1.
// Example 3:

// Input: nums = [5,4,-1,7,8]
// Output: 23
// Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSub = nums[0];
        int currSum = 0;

        for (int n : nums) {
            if (currSum < 0) {
                currSum = 0;
            }
            currSum += n;
            maxSub = max(maxSub, currSum);
        }

        return maxSub;
    }
};

string reverse(string word){

    string wrd = "";
    for (int letter = 0; letter < word.size(); letter++){
        //cout<<word[letter]<<endl;
        wrd = wrd+ word[letter];
        cout<<wrd<<endl;

    }  
    return wrd;
}


int main() {
    // Example usage
    // Solution solution;
    // vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};

    // // int result = solution.maxSubArray(nums);

    // cout << "Maximum Subarray Sum: " << result << endl;
    cout<<reverse("sugam");

    return 0;
}





