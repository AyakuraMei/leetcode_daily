#include <vector>
using namespace std;

int trap(vector<int> &height)
{
    int left = 0;
    int right = height.size() - 1;
    int leftMax, rightMax = 0;
    int ans = 0;
    while(left < right)
    {
        if(height[left] < height[right])
        {
            height[left] >= leftMax ? leftMax = height[left] : ans += leftMax - height[left];
            left++;
        }
        else
        {
            height[right] >= rightMax ? rightMax = height[right] : ans += rightMax - height[right];
            right--;
        }
    }
    return ans;
}