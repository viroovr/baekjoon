#include <iostream>

int main(){
  int N, K;

  //두 개의 자연수 N,K
  // 1 <= N <= 10000, 1<= K <= N
  std::cin >> N;
  std::cin >> K;

  //i는 약수의 번지수. j는 약수로 대입될 값
  int i = 0,j = 1;
  
  while (1){
    if (N % j == 0)
    {
      i++;
      if(i == K) break;
      j++;
    }
    else{
      if(j>=N) {j = 0; break;}
      j++;
    }
  }

  std::cout << j << std::endl;
}