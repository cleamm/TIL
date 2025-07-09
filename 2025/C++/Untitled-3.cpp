#include <iostream>
using namespace std;

int main(){

    // char user_input[100];

    // cout << "원하는 문장" << endl;
    // cout << "입력: ";

    // cin.getline(user_input, sizeof(user_input));
    // cout << "메아리: " << user_input << endl;


    // int num = -1;

    // cin >> num;
    // cout << num << endl;

    // cin.ignore(100, '\n');
    // cin >> num;

    // cout << user_input << " " << num << endl;



    // 분기
    int num;
    cout << "숫자를 입력하세요:";
    cin >> num; 
    if (num > 10){
        cout << "10보다 큽니다." << endl;
    
    }else{
        cout << "10보다 작습니다." << endl;
    }
    return 0;
}