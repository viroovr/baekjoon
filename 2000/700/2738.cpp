#include <stdio.h>
#include <stdlib.h>

int main(){
  int n, m;
  scanf("%d %d",&n, &m);
  int A[n][m];
  int **B = (int **)malloc(n * sizeof(int *));
  for (int i = 0; i < n; i++)
  {
    B[i] = (int *)malloc(m * sizeof(int));
  }

  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      scanf("%d",&A[i][j]);
    }
  }
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      scanf("%d",&B[i][j]);
    }
  }
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      printf("%d ",A[i][j]+B[i][j]);
    }
    puts("");
  }

  for (int i = 0; i < n; i++)
  {
    free(B[i]);
  }
  free(B);
  
  
}