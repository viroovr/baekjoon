#include <iostream>
#define N 9

int main(){  
  int mat[N][N];
  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < N; j++)
    {
      std::cin >> mat[i][j];
    }
    
  }

  int max[3] = {INT32_MIN, -1, -1};

  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < N; j++)
    {
      if (mat[i][j] > max[0])
      {
        max[0] = mat[i][j];
        max[1] = i+1;
        max[2] = j+1;
      }
      
    }
    
  }
  
  std::cout << max[0] <<std::endl;
  std::cout << max[1] << " " << max[2] << std::endl;


  
}