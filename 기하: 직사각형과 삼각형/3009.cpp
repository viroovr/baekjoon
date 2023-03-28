#include <iostream>

typedef struct _point
{
  int x;
  int y;
}point;


int main(){
  int size = 4;
  point point_list[size];
  point last_point;
  for (int i = 0; i < size-1; i++)
  {
    std::cin >> point_list[i].x;
    std::cin >> point_list[i].y;
  }

  if (point_list[0].x == point_list[1].x)
    last_point.x = point_list[2].x;
  else if (point_list[0].x == point_list[2].x)
    last_point.x = point_list[1].x;
  else
    last_point.x = point_list[0].x;

  if (point_list[0].y == point_list[1].y)
    last_point.y = point_list[2].y;
  else if (point_list[0].y == point_list[2].y)
    last_point.y = point_list[1].y;
  else
    last_point.y = point_list[0].y;

  std::cout << last_point.x << " " << last_point.y << std::endl;
  
}
