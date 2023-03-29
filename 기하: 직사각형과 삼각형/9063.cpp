#include <iostream>
int main(){
  int N; std::cin >> N;
  int x_point[N], y_point[N];
  int x_max = INT32_MIN, x_min = INT32_MAX;
  int y_max = INT32_MIN, y_min = INT32_MAX;
  for (int i = 0; i < N; i++)
  {
    std::cin >> x_point[i] >> y_point[i];
    if(x_point[i] > x_max)
      x_max = x_point[i];
    if(x_point[i] < x_min)
      x_min = x_point[i];
    if(y_point[i] > y_max)
      y_max = y_point[i];
    if(y_point[i] < y_min)
      y_min = y_point[i];
  }
  std::cout << (x_max-x_min) * (y_max-y_min) << std::endl;
}