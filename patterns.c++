#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(){

    int row; int col;
    cout<<"row: ";
    cin>>row;
    cout<<"col: ";
    cin>>col;

   //rectangle pattern

    
    // for (int i = 0; i < row; i++){
    //     for(int j = 0; j < col; j++){
    //         if (j > 0 && j < col-1 && i > 0 && i < row-1){
    //             cout<<"  ";
    //         }
    //         else{
    //             cout<<"* ";
    //         }
    //     }
    //     cout<<endl;
    // }

    // inverted half pyramid
    for (int i = row; i >= 1; i--){
        for (int j = 1; j <= i; j++){
            cout<<"* ";
        }
        cout<<endl;
    }
   return 0;
}
