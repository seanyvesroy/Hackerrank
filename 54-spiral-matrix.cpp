class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> output;
        int horizontal = matrix[0].size();
        int vertical = matrix.size();
        int left = 0;
        int right = horizontal - 1;
        int top = 0;
        int bottom = vertical - 1;
        int direction = 0;
        
        while(left <= right && top <= bottom) {
            if(direction == 0) {
                for(int j = left; j <= right; j++) {
                    output.push_back(matrix[top][j]);
                }
                top++;
                direction = 1;
            }
            else if(direction == 1) {
                for(int i = top; i <= bottom; i++) {
                    output.push_back(matrix[i][right]);
                }    
                right--;
                direction = 2;
            }
            else if(direction == 2) {
                for(int j = right; j >= left; j--) {
                    output.push_back(matrix[bottom][j]);
                }
                bottom--;
                direction = 3;
            }
            else if(direction == 3) {
                for(int i = bottom; i >= top; i--) {
                    output.push_back(matrix[i][left]);
                }
                left++;
                direction = 0;
            }
        }
        return output;
    }
};