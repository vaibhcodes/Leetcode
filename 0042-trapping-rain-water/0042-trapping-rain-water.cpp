#include <vector>
#include <stack>
#include <algorithm>

class Solution {
public:
    int trap(std::vector<int>& height) {
        std::stack<int> st;
        int water_trapped = 0;
        
        for (int i = 0; i < height.size(); i++) {
            while (!st.empty() && height[i] > height[st.top()]) {
                // Pop the bottom of the valley
                int bottom = st.top();
                st.pop();
                
                // If there's no left wall, no water can be trapped
                if (st.empty()) {
                    break;
                }
                
                // Get the boundaries
                int left = st.top();
                int right = i;
                
                // Calculate dimensions
                int h = std::min(height[left], height[right]) - height[bottom];
                int w = right - left - 1;
                
                // Add to total water
                water_trapped += h * w;
            }
            
            // Push the current bar's index
            st.push(i);
        }
        
        return water_trapped;
    }
};
