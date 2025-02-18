class Solution {
public:
    string truncateSentence(string s, int k) {
        int count = 0;
        string ans;
        
        for(int i = 0; i < s.size(); i++) {
            if (s[i] == ' ') { 
                count++; // Increase word count on space
                if (count == k) break; // Stop after k words
            }
            ans += s[i]; // Append characters normally
        }
        
        return ans;
    }
};
