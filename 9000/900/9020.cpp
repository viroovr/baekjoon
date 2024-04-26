#include <iostream>
#include "math.h"

bool isPrime(int num){
  int limit = sqrt(num);
  for (int i = 2; i <= limit; i++)
  {
    if (num % i == 0)
    {
      return false;
    }
  }
  return true;
}

void printGoldBach(int num)
{
  for (int i = num/2; i > 1; i--)
  {
    if (isPrime(i) && isPrime(num-i))
    {
      std::cout << i << " " << num-i << std::endl;
      return;
    }
    
  }
  

}

int main(){
  int test_num;
  std::cin >> test_num;
  int num_array[test_num];
  for (int i = 0; i < test_num; i++)
  {
    std::cin >> num_array[i]; 
    if (num_array[i] < 4 || 10000< num_array[i])
    {
      exit(1);
    }
    
  }
  for (int i = 0; i < test_num; i++)
  {
    printGoldBach(num_array[i]);
  }

  
}