#include <stdio.h>
#include <stdlib.h>
#include <iostream>

class Stack{
  int N;
  int top;
  int *stack;

  public:
  Stack(int *stack, int N): top(-1), N(N), stack(stack){}
  /* Stack(int N): top(-1) {
    stack = new int[N];
  }
  ~Stack(){
    delete[] stack;
  } */
  void push(int n){
    top++;
    if (top >= N)
    {
      std::cout << "stack is full" << std::endl;
      top--;
      return;
    }
    stack[top] = n;
  } 

  int pop(){
    if(top < 0) {
      std::cout << "stack is empty" << std::endl;
      return -1;
    }
    return stack[top--];
  }

  void print_stack(){
    for (int i = 0; i < N; i++)
    {
      std::cout << stack[i] << ", ";

    }
    
  }
};

void print_output(int *o, int n){
  for (int i = 0; i < n; i++)
    std::cout << o[i] << std::endl;
  
}
int main(){

  int N;
  scanf("%d",&N);
  int stack[N];
  int output[N];
  Stack mystack(stack, N);

  for (int i = 0; i < N; i++)
  {
    mystack.push(i+1);
  }

  mystack.print_stack();
  /*     
  int given_array[N];
  int input_array[N];
  int output_array[N];
  
  for (int i = 0; i < N; i++)
    scanf("%d",given_array + i);
  

  for (int i = 0; i < N; i++)
    input_array[i] = 1+i;
  
   */

}