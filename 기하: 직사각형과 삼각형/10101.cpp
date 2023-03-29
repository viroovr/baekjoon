#include <iostream>
using namespace std;

int main(){
  int x,y,z; cin >> x >> y >> z;
  if (x+y+z != 180)
    cout << "Error" << endl;
  else
    if(x==y && y == z) cout << "Equilateral" << endl;
    else
      if(x==y || y==z || x == z) cout << "Isosceles" <<endl;
      else cout << "Scalene" << endl;
}