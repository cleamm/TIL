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



    // 분기1 if문
    // int num;
    // cout << "숫자를 입력하세요:";
    // cin >> num; 
    // if (num > 10){
    //     cout << "10보다 큽니다." << endl;
    // }else if ( num == 10){
    //     cout << "10입니다." << endl;
    // }else{
    //     cout << "10보다 작습니다." << endl;
    // }

    // 분기2 : 삼항 연산자
    // cout << (num % 2 == 0 ? "짝수임." : "홀수임.") << endl;
    

    // 분기3 : switch - case
    // int num = 10;
    // switch(num){ // 해당 조건과 같은지만 case에서 비교하게 됨
    //     case 0:
    //         cout << "0입니다." << endl;
    //         break; // break가 없으면 모든 case를 실행할 수도 있으니 주의
    //     case 1:
    //         cout << "1입니다." << endl;
    //         break;
    //     case 2:
    //         cout << "2입니다." << endl;
    //         break;
    //     default:
    //         cout << "예상 외의 값임" << endl;
    //         // 마지막 break는 생략이 가능함
    // }


    // 반복문1 for문
    // for (int i = 0; i < 10; i++){
    //     cout << i;
    // }cout << endl;

    // int arr[] = {1,2,3,3,4,3,3,3,4,5,5,6}; // 배열 길이 구하기
    // printf("%d", sizeof(arr)/sizeof(int));
    // for (int i = 0; i < sizeof(arr)/sizeof(int); i++){
    //     cout << arr[i];
    // }
    // cout << endl;


    char my_str[] = "im steel hungry...";
    for (int i = 0; i < sizeof(my_str)/sizeof(char); i++){
        printf("%c", my_str[i]);
        printf("%d", i);
        printf("\n");
    }
    return 0;
}