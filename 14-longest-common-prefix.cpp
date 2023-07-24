class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string output = "";
        int shortest = strs[0].size();
        for(int i = 0; i < strs.size();i++) {
            if(strs[i].size() < shortest) {
                shortest = strs[i].size();
            }
        }
        char curr = strs[0][0];
        for(int col = 0; col < shortest; col++) {
            for(int row = 0; row < strs.size(); row++) {
                if(strs[row][col] != curr) {
                    return output;
                }
            }
            output.push_back(curr);
            curr = strs[0][col + 1];
        }
        return output;
    }
};