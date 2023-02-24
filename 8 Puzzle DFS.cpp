#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define fi first
#define sc second
#define endl '\n'

// implementasi dari dfs ini merupakan hasil referensi
// dan diskusi dengan kelompok X, yang beranggotakan Nadif, Nizam, dan yoyo,  dengan modifikasi penambahan fitur untuk mencetak path


set <string> visited;

int getPos(int idx, int dest)
{
    int row = idx / 3;
    int col = idx % 3;
    
    if(dest == 0)
        return (row == 0 ? -1 : 3 * (row - 1) + col);    // Top       
    else if(dest == 1)
        return (col == 2 ? -1 : 3 * row + col + 1);       // Right
    else if(dest == 2)
        return (row == 2 ? -1 : 3 * (row + 1) + col);    // Bottom
    else
        return (col == 0 ? -1 : 3 * row + col - 1);       // Left
}

void dfs(string start, string finish)
{
    stack <pair<string, int> > st;
    map<string, string> path;
    st.push(mp(start, 0));
    path[start] = "";

    while(!st.empty())
    {
        string cur = st.top().fi;
        int step = st.top().sc;
        st.pop();
        
        if(!visited.count(cur))
            visited.insert(cur);
        
        if(cur == finish){
            cout << step << endl << path[cur] << endl;
            return;
        }
        int kosong = -1;
        
        for(int i = 0; i < 9; ++i){
            if(cur[i] == '0'){
                kosong = i;
                break;
            }
        }
        for(int i = 0; i < 4; ++i)
        {
            string nextStr = cur;
            int nextPos = getPos(kosong, i);
            
            if(nextPos != -1){
                swap(nextStr[kosong], nextStr[nextPos]);
            }
            if(!visited.count(nextStr))
            {
                visited.insert(nextStr);
                st.push(mp(nextStr, step + 1));
                if(i == 0)
                    path[nextStr] = path[cur] + " UP";
                else if(i == 1)
                    path[nextStr] = path[cur] + " RIGHT";
                else if(i == 2)
                    path[nextStr] = path[cur] + " DOWN";
                else
                    path[nextStr] = path[cur] + " LEFT";
            }
        }
    }   
}

int main()
{
    string start = "123456078";
    string finish ="123456780";
    
    dfs(start, finish);
    return 0;
}
