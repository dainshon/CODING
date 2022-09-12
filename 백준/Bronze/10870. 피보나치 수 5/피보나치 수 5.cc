#include <iostream>
using namespace std;

int main() {
  int num;
  scanf("%d",&num);
  int array[num+1];
  array[0]=0;
  array[1]=1;
  for(int i=2;i<=num;i++){
    int p=i-1;
    int q=i-2;

    array[i] = array[p]+array[q];
  }
  printf("%d",array[num]);

}

