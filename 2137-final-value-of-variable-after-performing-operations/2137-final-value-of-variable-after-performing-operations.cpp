class Solution {
public:
    int finalValueAfterOperations(vector<string>& ope) {

        int track=0;
        
        for(int i = 0; i < ope.size(); i++){
            if(ope[i] == "--X" || ope[i] == "X--"){
                track--;
            }
            else if (ope[i] == "++X" || ope[i] == "X++"){
                track++;
            }
        }
        return track;
    }
};