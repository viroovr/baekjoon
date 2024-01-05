#include <iostream>
#include <math.h>

bool is_prime(int n){
  if(n == 1){
    return false;
  }
  int limit = sqrt(n);
  for (int i = 2; i <= limit; i++)
  {
    if(n % i == 0){
      return false;
    }
  }
  return true;
}

int main(){
  int N;
  std::cin >> N;
  int input[N];

  for (int i = 0; i < N; i++)
  {
    std::cin >> input[i];
  }
  int prime_num = 0;
  for (int i = 0; i < N; i++)
  {
    if(is_prime(input[i]))
      prime_num++;
  }
  std::cout << prime_num << std::endl;
}