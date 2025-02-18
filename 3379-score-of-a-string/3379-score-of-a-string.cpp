#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int scoreOfString(string s) {
        int f = 0;
        for (int i = 0; i < s.size() - 1; i++) {
            f += abs(s[i] - s[i + 1]);  // Directly update f with the absolute difference
        }
        return f;
    }
};
