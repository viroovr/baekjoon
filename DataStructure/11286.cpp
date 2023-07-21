#include <iostream>
#include <queue>
//백준에서 컴파일 에러발생.
using namespace std;

struct PairCompare{
    bool operator()(const pair<int, int>& p1, const pair<int, int>& p2){
        if(p1.first < p2.first)
            return false;
        else if(p1.first > p2.first)
            return true;
        else
            return p1.second > p2.second;

    }
};

int main(){
    priority_queue<vector<pair<int, int>>, vector<pair<int, int>>, PairCompare> q;
    int num;
    cin >> num;
    for (int i = 0; i < num; i++)
    {
        int d;
        cin >> d;
        if (d == 0)
        {
            if (q.empty())
            {
                cout << 0 << endl;
            } else{
                cout << q.top().second << endl;
                q.pop();
            }
            
        }
        else{
            q.push(make_pair(abs(d), d));
        }
        
    }
    
}