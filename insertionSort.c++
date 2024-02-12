#include<iostream>
using namespace std;
// int main(){                                     //1.  Define a function that returns an integer value
//     int n;                                      //2.  Define an integer of name n
//     cin>>n;                                     //3.  Take input of size "n";
//     int arr[n];                                 //4.  Define an array of size n
//     for (int i = 0; i < n; i++){                //5.  From 0 to 1 less than the size of index, increment 
//         cin>>arr[i];                            //6.  Add the values until the condition is met.
//     }                                   
//     for (int i = 1; i < n; i++){                //7.  Loop for insertion starting from index 1;
//         int current = arr[i];                   //8.  Take the current element to be the second element in an array
//         int j = i-1;                            //9.  Initialize the 0th index by j
//         while (current < arr[j] && j >= 0){     //10. While the current is smaller than the eleent of the array in the first index and while the index is greater or equal to 0, traverse 
//             arr[j+1] = arr[j];                  //11. In the place of higher index, put the value from lower index. --> shifting from left to right
//             j--;                                //12. Traverse. j is dependent with the value of i. J will have the value 1 less than that of i. So, it will iterate until i.
//         }                                       
//         arr[j+1] = current;                     //13. Always choose the value above the j value to be current
//     }
//     for (int i = 0; i < n; i++){                //14. Print until all the numbers are printed.
//         cout<<arr[i]<<" ";
//     }
//     cout<<endl;
//     return 0;
// }
int main(){
    int n;
    cout<<"n: ";
    cin>>n;
    int arr[n];
    for (int i = 0; i < n; i++){
        cin>>arr[i];
    }
    for (int i = 1; i<n; i++){
        int current = arr[i];
        int j = i-1;
        while (current < arr[j] && j >= 0){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = current;
    }
    for (int i = 0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}