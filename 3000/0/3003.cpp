#include <iostream>


int main(){
  //킹, 퀸, 룩, 비숍, 나이트, 폰 개수
  //각 1, 1, 2, 2, 2, 8개있어야 함
  int chess[6];
  for (int i = 0; i < 6; i++)
  {
    std::cin >> chess[i];
  }
  int original[6] = {1,1,2,2,2,8};
  int output[6];

  for (int i = 0; i < 6; i++)
  {
    output[i] = original[i] - chess[i];
    std::cout << output[i] << " ";
  }

  
  
  
   
}