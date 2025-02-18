class Solution {
public:
    string interpret(string command) {
    string ans;

    for (int i = 0; i < command.size(); i++)
    {
        if (command[i] == '(' && command[i + 1] == ')')
        {
            ans.push_back('o');
        }
        else if (command[i] == '(' && command[i + 1] == 'a')
        {
            ans.append("al");
        }
        else if (command[i] == 'G')
        {
            ans.push_back('G');
        }
    }
    return ans;

    }
};