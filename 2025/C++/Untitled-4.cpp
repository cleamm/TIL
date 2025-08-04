#include <iostream>
#include <vector>
using namespace std;

int main() {
    // https://www.mycompiler.io/ko/new/cpp
    // 위 주소에서 코딩 연습함

    // 잊어버려서 다시 복습함;;
    cout<< "hello" << endl;
    int age = 25;
    double weight = 88.3;
    char grade = 'A';
    string name = "Choi";
    bool isStudent = true;

    cout << "나이 " << age << ", 자료형:" << typeid(age).name() << endl;
    cout << "체중 " << weight << ", 자료형:" << typeid(weight).name() << endl;
    cout << "학점 " << grade << ", 자료형:" << typeid(grade).name() << endl;
    cout << "이름 " << name << ", 자료형:" << typeid(name).name() << endl;
    cout << "학생여부 " << isStudent << ", 자료형:" << typeid(isStudent).name() << endl;
    cout << sizeof(name) << "바이트" << endl;
    cout << sizeof(grade) << "바이트" << endl;


    // if문
    int score;
    cout << "점수를 입력하세요: " << endl;
    cin >> score;
    cout << score << endl;
    if (score > 80) cout << 'A';
    else if (score > 70) cout << 'B';
    else cout << 'C';
    cout << endl;

    if (score % 2 == 1) cout << "홀수" ;
    else cout << "짝수";
    cout << endl;

    // for 문
    for (int i = 0; i < 5; i++) {
        cout << i << " ";
    }
    cout << endl;

    int numSum = 0;
    int n = 10;
    for(int j = 0; j < n; j++){
        numSum += j;
    }
    cout << numSum << endl;

    // while 문
    int k = 0;
    while(true){
        if(k == n) break;
        else k += 1;
    }
    cout << "k = " << k << endl;

    
    // hello
    // 나이 25, 자료형:i
    // 체중 88.3, 자료형:d
    // 학점 A, 자료형:c
    // 이름 Choi, 자료형:NSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
    // 학생여부 1, 자료형:b
    // 32바이트
    // 1바이트
    // 점수를 입력하세요: 
    // 74
    // B
    // 짝수
    // 0 1 2 3 4 
    // 45
    // k = 10

    // vector<int> nums = {5,2,8,1};
    // for (int i = 0; i<nums.size(); i++){
    //  cout << nums[i] << " ";   
    // }
    // cout << endl;

    // 연습문제
    // int *nums = new int[5]; // 동적 메모리 할당
    // for (int i = 0; i < 5; i++){
    //     cin >> nums[i] ;
    // }
    
    // for (int j = 0; j < 5; j ++){
    //     cout << nums[j] << " " << endl;
    // }
    // cout << nums[0]<< endl;
    // cout << sizeof(nums)<< endl;

    int nums[5]; // 정적 배열 == 포인터를 사용하지 않고 배열을 생성
    for (int i = 0; i< 5; i++){
        cin >> nums[i];
    }
    for (int i = 0; i < 5; i++){
        cout << nums[i];
    }
    cout << endl;
    cout << "배열의 길이는 "<< sizeof(nums)/sizeof(int) <<endl;


    // 배열 주소 및 데이터 출력하기
    int arr[5] = {10,20,30,40,50};
    cout << arr << endl; // 주소를 출력
    cout << &arr << endl; // 위와 동일한 주소
    cout << &arr[0] << endl; // 위와 동일한 주소2
    cout << arr[0] << endl; // 값을 출력
    cout << *(arr + 1) << endl; // 1번째 인덱스 포인터 호출
    cout << *(arr + 0) << endl; // 0번째 인덱스 포인터 호출

    // 포인터와 new 비교하기
    int *p = new int[5];
    for (int i = 0; i<5; i++){
        p[i] = i * 10;
    }
    cout << sizeof(p) << endl; // 포인터 크기 출력(윈도우64비트 => 8바이트)
    cout << p[2] << endl; // 20을 출력

    // 잠시 의문 정리
    // include(헤더)를 사용해야 기본 기능들(cin, cout, endl)을 사용할 수 있음
    // 그러나 std에서 가져와서 사용하므로 std::cin과 같은 형식으로 사용하게 됨
    // std::cin과 같이 사용하기엔 글이 너무 길어지므로 이에 대한 약자가 필요하여
    // 기본값으로 using namespace std;와 같은 문구를 추가하여 코드를 간편하게 작성토록 함
    // vector또한 마찬가지로 include <vector>라는 것을 사용하여 std::vector가 사용 가능해짐
    // 그래서 using을 사용하여 vector<int> nums(5)와 같은 문법을 사용가능해짐
    // 추가로 위와 같은 문법들은 현대식 C++문법이라고 할 수 있음

    // vector로 같은 작업해보기
    vector<int> nums(5);
    for (int i=0; i< 5; i++)cin >> nums[i];
    for (int val : nums) cout << val << " ";
    cout << endl;

    // 연습하기
    vector<string> datas(5);
    string arr1[5] = {"apple","banana","mango","watermelon","blueberry"};
    for (int i=0; i<5; i++) datas[i] = arr1[i];
    for (string v : datas) cout << v << endl;


    // // 정수 N개가 주어졌을 때, 배열의 총합을 출력하세요.
    // // 입력: 5 1 2 3 4 5 → 출력: 15
    // int n;
    // cin >> n;
    // int sumNum = 0;
    // vector<int> nums(n);
    // for (int i=0; i<n; i++) cin >> nums[i];
    // for (int i=0; i<n; i++) sumNum += nums[i];
    // cout << sumNum << endl;
    
    
    // // 배열에서 가장 큰 값과 그 인덱스를 출력하세요.
    // // 입력: 10 5 3 9 2 → 출력: 10 0
    // vector<int> nums;
    // int resIdx = 0, idx = 0, num;
    // while(cin >> num) nums.push_back(num); // 파이썬에서 list에 append하는 것과 같은 역할
    // int maxNum = nums[0];
    // for (int x: nums) {
    //     if (x > maxNum) {
    //         maxNum = x;
    //         resIdx = idx ;
    //     }
    //     idx ++;
    // };
    // cout << maxNum << " " << resIdx << endl;

    // // 배열을 거꾸로 출력하세요.
    // // 입력: 1 2 3 4 → 출력: 4 3 2 1
    // vector<int> nums;
    // int num;
    // while(cin >> num) nums.push_back(num);
    // for(int i=nums.size()-1; i >= 0; i--) cout << nums[i] << " ";


    // // 배열에서 짝수인 숫자만 출력하세요.
    // // 입력: 1 4 7 2 6 → 출력: 4 2 6
    // vector<int> nums;
    // int num;
    // while(cin >> num) nums.push_back(num);
    // for (int n : nums) if (n % 2 == 0) cout << n << " "; 
    // cout << endl;


    // // 배열에서 숫자 x가 몇 번 나오는지 출력하세요.
    // // 입력: 1 2 3 2 2 5, x = 2 → 출력: 3
    // vector<int> nums;
    // int n;
    // int res = 0;
    // while(cin >> n) nums.push_back(n);
    // int cnt = nums[nums.size()-1];
    // for (int i=0; i<nums.size()-1;i++) {
    //     if (nums[i] == cnt) res ++;
    // }cout << res << endl;




    return 0;
}