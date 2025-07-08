#include <iostream>
using namespace std;

int main(){ // 배열
    int a = 1;
    int b = 2;
    int c = 3;

    // cout << a << b << c << endl;

    // int my_arr[3] = {1,2,3};
    // cout << my_arr[0] << ' '
    //      << my_arr[1] << ' ' // 이런 식으로 출력하는 경우는 띄어쓰기를 포함하여 출력하게됨
    //      << my_arr[2] << endl; // 띄어쓰기와 숫자는 다른 타입이지만 cout은 동적 타입을 가지고 출력하므로 가능함

    // int my_arr2[10] = {1,2,3};
    // cout << my_arr2 << endl; // 메모리 주소를 출력

    // for (int i=0; i<10; i++){
    //     cout << my_arr2[i] << endl; // 데이터가 없으면 0으로 채워지는 듯함
    // }

    // int my_arr3[100];

    // for (int i=0; i<100; i++){
    //     cout << my_arr3[i] << endl; // 초기화되지 않은 배열은 쓰레기값을 출력함
    // }

    // cout << my_arr3[400] << endl;



    char name[100] = "children hello!"; // 캐릭터 타입은 1바이트 단위로 메모리 사용
    cout << name << sizeof(name) << endl; // 당연히 name의 값과 name배열의 크기인 100이 붙어서 출력

    name[0] = 'A';
    name[1] = 'B';
    name[2] = 'C';
    cout << name << endl;
    name[2] = '\0'; // null 문자열(C-string)이라고 함
    cout << name << sizeof(name) << endl; // name[2]에서 문자열 종료하여 뒷내용이 사라짐
    cout << name[99] << endl; // 빈('')값을 출력

    return 0;
}

