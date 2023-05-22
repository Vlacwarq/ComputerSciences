#include <cstdlib>
#include <iostream>
using std::cout;
using std::endl;
// ------------------------------- Function prototypes
void seq_fill(int n, int *arr);
void arrShift(int n, int *arr);
void arrShuffle(int n, int *arr);
void arrPrint(int n, int *arr);

int main() {
  // ------------------ Working socket
  int array[10] = {};
  seq_fill(3, array);
  arrShuffle(3, array);
  arrPrint(3, array);
  
  
}
// --------------------------------- Function definition
void seq_fill(int n, int *arr){
  for(int i = 0; i < n; i++){
    arr[i] = i+1;
  }
}

void arrPrint(int n, int *arr){
  for(int i = 0; i < n; i++){
    cout<<arr[i]<<" ";
  }
  cout<<endl;
}

void arrShift(int n, int *arr){
  int a = arr[0];
  for(int i = 1; i <= n-1; i++){
    arr[i-1] = arr[i];
    
  }
  arr[n-1] = a;
}

void arrShuffle(int n, int *arr){
  arrPrint(3, arr);
  int a = n - 1;
  while(a != 0){
    arrShift(a+1, arr);
    if(arr[a]!=a){
      arrPrint(3, arr);
      a = n - 1;
    }
    else{
      a--;
    }
  }
  
}

// 123
// 231
// 132
// 321
// 213
// 312