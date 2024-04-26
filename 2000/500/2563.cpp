#include <stdlib.h>
#include <stdio.h>

void get_color_paper_number(int *n){
  //n에다가 색종이의 수 저장
  scanf("%d", n);
}


int main(){
  int color_paper_number;
  get_color_paper_number(&color_paper_number);

  int N = 100;

  int drawing_paper[N][N];
  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < N; j++)
    {
      drawing_paper[i][j] = 0;
    }
    
  }
  
  for ( int i = 0; i < color_paper_number; i++)
  {
    int x, y;
    scanf("%d %d",&x,&y);
    for ( int inc_y = y; inc_y < y+10; inc_y++)
    {
      for (int inc_x = x; inc_x < x+10; inc_x++)
      {
        if(drawing_paper[inc_y][inc_x] == 1) continue;
        drawing_paper[inc_y][inc_x] = 1;
      }
    }
    
  }
  int sum = 0;
  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < N; j++)
    {
      int k = drawing_paper[i][j];
      //printf("%d", k);
      if ( k == 1){
        sum ++;
      }
    }
    //printf("\n");
  }
  printf("%d\n", sum);

}


