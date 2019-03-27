#include <bits/stdc++.h>
using namespace std;

const int MAXN = 875714;

vector<int> graph[MAXN];
vector<int> reversedGraph[MAXN];

int graphVisited[MAXN];
int reversedVisited[MAXN];

int finishTime;
int currentLeader = -1;

int finishTimes[MAXN];
int leaders[MAXN];

map<int, int> ans;

void dfsOnGraph(int current)
{
    graphVisited[current] = 1; // visited
    leaders[current] = currentLeader;
    for (int i = 0; i < graph[current].size(); ++i)
    {
        int nextNode = graph[current][i];
        if (!graphVisited[nextNode])
        {
            dfsOnGraph(nextNode);
        }
    }
}

void dfsOnReversed(int current)
{
    reversedVisited[current] = 1; // visited
    for (int i = 0; i < reversedGraph[current].size(); ++i)
    {
        int nextNode = reversedGraph[current][i];
        if (!reversedVisited[nextNode])
        {
            dfsOnReversed(nextNode);
        }
    }

    finishTimes[finishTime++] = current; // to check
}

void kosaraju()
{
    for (int i = MAXN - 1; i >= 0; i--)
    {
        if (!reversedVisited[i])
        {
            dfsOnReversed(i);
        }
    }

    for (int i = MAXN - 1; i >= 0; i--)
    {
        int possibleLeader = finishTimes[i];
        if (!graphVisited[possibleLeader])
        {
            currentLeader = i;
            dfsOnGraph(possibleLeader);
        }
    }
    cout << "aqui llegue" << endl;
}

void saveGraphs()
{
    freopen("SCC.txt", "r", stdin);
    int u, v;
    while (cin >> u >> v)
    {
        u--;
        v--;
        graph[u].push_back(v);
        reversedGraph[v].push_back(u);
    }
}

void countAndPrintComponets()
{
    for (int i = 0; i < MAXN; ++i)
    {
        ans[leaders[i]]++;
    }

    vector<pair<int, int>> vector(ans.begin(), ans.end());

    std::sort(vector.begin(), vector.end(),
              [](const auto &lhs, const auto &rhs) { return lhs.second > rhs.second; });


    for (int i = 0; i < 5 ; ++i)
        cout << vector[i].first << ": " << vector[i].second << std::endl;
}

int main()
{
    saveGraphs();
    kosaraju();
    countAndPrintComponets();

    return 0;
}
