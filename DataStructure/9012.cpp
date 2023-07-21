#include <stdio.h>
#include <iostream>
#include <stack>
using namespace std;

int main(){
    int num;
    cin >> num;
    for(int i=0; i<num; i++) {
        stack<char> s;
        string ps;
        cin >> ps;
        for ( char i : ps){
            if (i == '(')
                s.push(i);
            else {
                if (!s.empty() && s.top() == '(')
                    s.pop();
                else {
                    s.push(i);
                    break;
                }
            }
        }
        if ( s.empty())
            cout << "YES" <<endl;
        else
            cout << "NO" << endl;
    }
}