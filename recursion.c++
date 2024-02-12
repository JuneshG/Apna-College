#include <iostream>
using namespace std;

// replace pi with 3.14
void replacePi(string s){
    if (s.length()== 0){ //base case
        return;
    }
    if (s[0] == 'p' && s[1] == 'i'){

        cout<<"3.14";
        replacePi(s.substr(2));
    }
    else{

        cout<<s[0];
        replacePi(s.substr(1));
    }
}


// tower of Hanoi

void toh(int n, char src, char dest, char help){

    if (n == 0){
    return;    
    }

    toh(n-1, src, help, dest);
    cout<<"Move "<<src<<" to "<<dest<<endl;
    toh(n-1, help, dest, src);
}


//remove duplicate characters

string removeDup(string s){
    if (s.length() == 0){
        return "";
    }

    char ch = s[0];
    string ans = removeDup(s.substr(1));

    if (ch == ans[0]){
        return ans;
    }
    return ch + ans;
}

string C();
string B(){
    return " my " + C();
}
string A(){
    return "hello " + B();
}
string C(){
    return " friend";
}

// string reversal

void reverseStr(string s){
    if (s.length() == 0){
        return;
    }

    string ros = s.substr(1);
    reverseStr(ros);
    cout<<s[0];
}


int main(){
    // replacePi("pipipipppiiipiiixxpi000");
    // toh(3,'A','C', 'B');
    // cout<<removeDup("Juneeesh Gaaaautaaam");
    // cout<<A();
    reverseStr("PADAM GAUTAM");
    return 0;
}

