#include <stdio.h>
int main(){
  int a[3];
  while(scanf("%d%d%d",a,a+1,a+2)==3){
    if(a[0]==0&&a[1]==0&&a[2]==0) break;
    int max[2];max[0]=-1;int sum=0;
    for (int i = 0; i < 3; i++)
      if(a[i] > max[0]) {max[0] = a[i];max[1]=i;}
    for (int i = 0; i < 3; i++)
      if(i != max[1]) sum+=a[i];
    if(sum<=max[0]) {printf("Invalid\n");continue;}
    if(a[0]==a[1]&&a[1]==a[2])printf("Equilateral\n");
    else 
      if(a[0]==a[1]||a[1]==a[2]||a[0]==a[2])printf("Isosceles\n");
      else printf("Scalene\n");
  }
}