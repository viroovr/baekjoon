#include<iostream>
int main(){
  int count=3;
  int a[count];std::cin>>a[0]>>a[1]>>a[2];
  for (int i = 0; i < count-1; i++)
    for (int j = i+1; j < count; j++)
    {
      int temp;
      if(a[i]>a[j]){temp=a[i];a[i]=a[j];a[j]=temp;}
    }
  if(a[0]+a[1]<=a[2])
    std::cout<<2*(a[0]+a[1])-1 <<std::endl;
  else std::cout<<a[0]+a[1]+a[2]<<std::endl;
}