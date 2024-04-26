#include <iostream>

void set_min(int *list, int i, int j){
  if(i < j){
    list[5] = i;
  }
  else{
    list[5] = j;
  }
  
}

int main(){
  // x, y, w, h
  int distance_list[5];
  distance_list[5] = INT32_MAX;
  int d,d2;
  for (int i = 0; i < 4; i++)
  {
    std::cin >> distance_list[i];
  }

  distance_list[5] = abs(distance_list[0] - distance_list[2]);
  set_min(distance_list, distance_list[5], distance_list[0]);
  set_min(distance_list, distance_list[5], abs(distance_list[1] - distance_list[3]));
  set_min(distance_list, distance_list[5], distance_list[1]);

  std::cout << distance_list[5] <<std::endl;
  
  
}