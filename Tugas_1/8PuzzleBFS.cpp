#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define fr front
#define fi first
#define sc second
#define endl '\n'

//Implementasi dari bfs ini merupakan hasil referensi dan 
//diskusi dengan kelompok X, yang beranggotakan Nadif, Nizam, dan yoyo,  dengan modifikasi penambahan fitur untuk mencetak path


set<string> visited;
map<string, string> prevStr;

int getPos(int zeroidx, int dest)
{
    int row = zeroidx / 3;
    int col = zeroidx % 3;

    if (dest == 0)
        return (col == 0 ? -1 : 3 * row + col - 1);      // Left
    else if (dest == 1)
        return (col == 2 ? -1 : 3 * row + col + 1);      // Right
    else if (dest == 2)
        return (row == 0 ? -1 : 3 * (row - 1) + col);    // Top
    else
        return (row == 2 ? -1 : 3 * (row + 1) + col);    // Bottom
}

void bfs(string start, string finish)
{
    queue<pair<string, int>> q;
    q.push(mp(start, 0));

    while (!q.empty())
    {
        string cur = q.fr().fi;
        int step = q.fr().sc;

        if (!visited.count(cur))
        {
            visited.insert(cur);
        }
        q.pop();

        if (cur == finish)
        {
            cout << step << endl;

            vector<string> path;
            string state = cur;

            while (state != start)
            {
                string prev = prevStr[state];
                int posDiff = (int)prev.find('0') - (int)state.find('0');

                if (posDiff == -1)
                    path.push_back("RIGHT");
                else if (posDiff == 1)
                    path.push_back("LEFT");
                else if (posDiff == -3)
                    path.push_back("DOWN");
                else if (posDiff == 3)
                    path.push_back("UP");

                state = prev;
            }

            reverse(path.begin(), path.end());

            for (auto move : path)
            {
                cout << move << " ";
            }
            cout << endl;

            return;
        }

        int kosong = -1;

        for (int i = 0; i < 9; ++i)
        {
            if (cur[i] == '0')
            {
                kosong = i;
                break;
            }
        }

        for (int i = 0; i < 4; ++i)
        {
            string nextStr = cur;
            int nextPos = getPos(kosong, i);

            if (nextPos != -1)
            {
                swap(nextStr[kosong], nextStr[nextPos]);

                if (!visited.count(nextStr))
                {
                    visited.insert(nextStr);
                    prevStr[nextStr] = cur;
                    q.push(mp(nextStr, step + 1));
                }
            }
        }
    }
}

int main()
{
	string start = "123456078";
	string finish ="123456780";
	
	bfs(start, finish);
	return 0;
}
