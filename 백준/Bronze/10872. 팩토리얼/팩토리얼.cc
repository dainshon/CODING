#include <iostream> //직사각형 탈
using namespace std;

int main() { 
  int num;
  scanf("%d",&num);
  int result=1;
  if(num==0)
    printf("1");
  else{
    for(int i=1;i<=num;i++){
      result*=i;
    }
    printf("%d",result);
  }
} 