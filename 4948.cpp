#include <iostream>
#include "mylib/prime.h"

int getPrimeNum(int n)
{
  int count = 0;
  for (int i = n+1; i <= 2*n; i++)
  {
    if (isPrime(i))
    {
      count ++;
    }
  }
  return count;
}

int main()
{
  int num = 1;
  while (1 )
  {
    std::cin >> num;
    if(num == 0)
      break;
    std::cout << getPrimeNum(num) << std::endl;
  }
  
}