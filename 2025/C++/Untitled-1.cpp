#include <iostream> // 헤더를 포함함(입출력 기능)
using namespace std; // 네임스페이스가 있어야 std::cout이 사용 가능

// int i = 12345;

int main(){
    // // 정수 다루기 + cin + cout
    // int a = 2;
    // cout << a+3 << endl;
    // char user_input[100];
    // cin >> user_input;
    // cout << user_input << endl;

    // // 문자열 다루기 + scanf + printf
    // char input_user[20]; // 배열이기 때문에 scanf에서 &input_user를 안해도 됨 = 단순 변수라면 &가 붙음
    // scanf("%s", input_user);
    // printf("%s\n", input_user);
    // printf("입력한 내용은 %s 입니다.", input_user);


    // int a, b, c, d;
    // // cin >> a >> b;
    // // cout << "a"<< b << endl;

    // scanf("%d, %d", &a, &b); // 틀에 맞게 입력해줘야 함. 1, 2
    // printf("%d, %d가 입력됨", a, b);
    // scanf("%d %d", &c, &d); // 틀에 맞게 입력해줘야 함. 1 2
    // printf("%d %d가 입력됨", c, d);

    // int i = 123;
    // cout << i << ' ' << sizeof(i) << endl; // int - 4byte이므로 4가 출력됨
    // cout << float(i) << ' ' << sizeof(float(i)) << endl; // float - 4byte이므로 8이 출력됨
    // cout << double(i) << ' ' << sizeof(double(i)) << endl; // double - 8byte이므로 8이 출력됨
    
    // char str[] = "hello world!"; // std::string
    // string ss = "stringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstring";
    // string sss = "strin";
    // cout << sizeof(ss) << endl; // 32 string 타입은 32byte
    // cout << sizeof(sss) << endl; // 32 
    // cout << sizeof(str) << endl; // 12 문자열 + 1 길이
    // cout << sizeof("abcde") << endl; // 6 문자열 + 1 길이

    // int i = 98.323; // int 타입에 소수 데이터가 들어가면 전부 버림
    // i += 100;
    // i ++ ;
    // cout << i << endl;

    // bool b = false;
    // cout << false << endl; // 0이 출력됨
    // cout << boolalpha << true << endl; // true가 출력됨
    // cout << noboolalpha << true << endl; // 1이 출력됨(기본값)

    // cout << noboolalpha << endl;
    // cout << (true && true) << endl;
    // cout << (true || false) << endl;

    // cout << (1>3) << endl;
    // cout << (3==3) << endl;
    // cout << ('a'!='c') << endl;
    // cout << ('a'!='a') << endl;

    // 영역(scope)
    int i = 123;
    { // 좁은 영역의 다른 변수가 됨
        int i = 345;
        cout << i << endl; // 당연히 가장 안쪽의 괄호 안에 있는 코드부터 작동하며 안의 변수 선언은 증발
        // cout << ::i << endl; 
    }
    cout << i << endl;
    return 0;
}