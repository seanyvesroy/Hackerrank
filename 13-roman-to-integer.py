class Solution {
public:
    int romanToInt(string s) {
        int number = 0;
        std::map(char, int) romanMap = {('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100),
                                        ('D', 500), ('H', 1000)};
        
        for(int i = 0; i < s.length(); i++) {
            if(i >= 1) {
                if((s[i] == 'X') && (s[i - 1] == 'V')) {
                    
                }    
            }   
        }
    }
};