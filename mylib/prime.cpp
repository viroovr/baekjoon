#include "prime.h"

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