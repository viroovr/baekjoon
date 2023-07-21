#include <iostream>
#include <queue>

using namespace std;

int main() {
    int num;
    cin >> num;
    queue<int> q;
    for (int i = 1; i <= num; i++)
    {
        q.push(i);
    }
    while ( q.size() > 1)
    {
        q.pop();
        int i = q.front();
        q.pop();
        q.push(i);
    }
    cout << q.back() << endl;
    
    
}