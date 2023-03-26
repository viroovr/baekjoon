#include <iostream>

struct divisor
{
  int number;
  int divisor_list[10000];
};

void get_divisor_list(int n, struct divisor* output_divisor){
  int i=0,j;
  for ( j = 1; j < n; j++)
  {
    if(n % j == 0){
      output_divisor->divisor_list[i]=j;
      i++;
    }
  }
  output_divisor->number = i;
  
}

int get_sum_divisor_list(struct divisor* n_divisor){
  int n = n_divisor->number;
  int sum = 0;
  for (int i = 0; i <n; i++)
  {
    sum += n_divisor->divisor_list[i];
  }
  return sum;
}


int main(){
  int n;
  int sum;
  while(1){
  std::cin >> n;
  if(n==-1) break;

  struct divisor n_divisor; 
  get_divisor_list(n, &n_divisor);
  if((sum = get_sum_divisor_list(&n_divisor)) == n){
    std::cout << sum << " = ";
    for (int i = 0; i < n_divisor.number; i++)
    {
      if(i == n_divisor.number-1){
        std::cout << n_divisor.divisor_list[i] << std::endl;
        break;
      }
      std::cout << n_divisor.divisor_list[i] << " + ";
    }
    
  }
  else{
    std::cout<< n << " is NOT perfect." << std::endl;
  }
  }

}