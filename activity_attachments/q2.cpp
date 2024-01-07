#include <iostream>
using namespace std;

int main(){
    char * name[5] = {"J. Kim", "K. Son", "K. Lee", "M. Hong", "J. Park"};
    int score[5][3];
    int totalScore[5];

    for(int i = 0; i < 5; i++){
        int total = 0;
        cout << "선수 " << i << ": " << name[i] << endl;
        for(int j = 0; j < 3; j++){
            cout << "심판" << j << " 점수: ";
            int s;
            cin >> s;
            score[i][j] = s;
            total += s;
        }
        cout << "total: " << total << endl;
        totalScore[i] = total;
    }

    //최고 최저 찾기
    int max = score[0][0];
    int maxStudent = 0;
    int min = score[0][0];

    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 3; j++){
            //최고점 찾기
            if(score[i][j] > max){
                max = score[i][j];
                maxStudent = i;
            }
            //최저점 찾기
            if(score[i][j] < min){
                min = score[i][j];
            }
        }
    }

    //평균 구하기
    int sum = 0;
    for(int i = 0; i < 5; i++){
        sum += totalScore[i];
    }

    cout << "최고점: " << max << endl;
    cout << "최저점: " << min << endl;
    cout << "최고점 선수: " << name[maxStudent] << endl;
    cout << "평균: " << sum/4.0 << endl;
}