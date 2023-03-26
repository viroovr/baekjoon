#include <iostream>
#include <string.h>

int main(){
  int num1, num2;
  char ret_str[30];
  while(1){
    //10000이 넘지 않는 두 자연수, 두수가 같은 경우 없음
    std::cin >> num1;
    std::cin >> num2;
    if(num1 == 0 && num2 == 0) break;

    //첫 번째 숫자가 두번째 숫자의 약수
    if( num2 % num1 == 0){
      strcpy(ret_str, "factor");
    }
    //첫번쨰 숫자가 두번째 숫자의 배수
    else if(num1 % num2 == 0){
      strcpy(ret_str, "multiple");
    }
    else 
      strcpy(ret_str, "neither");
    std::cout << ret_str << std::endl; 
  }
}