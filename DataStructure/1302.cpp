#include <iostream>
#include <map>

using namespace std;

int main(){
    map<string, int> m;
    int num;
    cin >> num;
    for ( int i = 0; i < num; i++)
    {
        string s;
        cin >> s;
        m[s]++;
        // cout << s << m[s] << endl;
    }
    int max = -1;
    string max_str = "";
    for (auto p: m){
        if (max_str.empty()){
            max_str = p.first.c_str();
            max = p.second;
        }
        // cout << "max_str and max : "<< max_str << max << endl;
        // cout << p.first.c_str() << p.second <<p.first.compare(max_str) << endl;
        if(p.second > max){
            max = p.second;
            max_str = p.first.c_str();
        }
        else if (p.second == max && p.first.compare(max_str) < 0){
            max_str = p.first.c_str();
        }
    }
    cout << max_str << endl;
}