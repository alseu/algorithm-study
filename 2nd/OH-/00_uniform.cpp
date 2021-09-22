#include <string>
#include <vector>
#include <cstring>
//efine DEBUG
#ifdef DEBUG
#include <iostream>
#endif

using namespace std;



int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = n;
    int* tmp;
    tmp = new int[n];
    memset(tmp, 0, n*sizeof(int));
    for(int i=0; i<lost.size(); i++)
        tmp[lost[i]-1]--;
#ifdef DEBUG
for(int i=0; i<n;i++)   cout << tmp[i] << ',';
cout << endl;
#endif
    for(int i=0; i<reserve.size(); i++)
        tmp[reserve[i]-1]++;
    
#ifdef DEBUG
for(int i=0; i<n;i++)   cout << tmp[i] << ',';
cout << endl;
#endif
    
    for(int i=0; i<n; i++)
    {
        if (tmp[i] < 0)
        {
            if((i>0)&&(tmp[i-1]==1))
            {
                tmp[i-1]--;
                tmp[i]++;
                continue;
            }
            if((i<n-1)&&(tmp[i+1] == 1))
            {
                tmp[i+1]--;
                tmp[i]++;
                continue;
            }
        }
    }
#ifdef DEBUG
for(int i=0; i<n;i++)   cout << tmp[i] << ',';
cout << endl;
#endif
    for(int i=0; i<n; i++)
        if(tmp[i]<0) answer--;
    
    delete tmp;
    return answer;
}

/***************************************************/
//                                                 //
//      테스트 1 〉	    통과 (0.01ms, 3.65MB)       //
//      테스트 2 〉	    통과 (0.01ms, 4.33MB)       //
//      테스트 3 〉	    통과 (0.01ms, 3.68MB)       //
//      테스트 4 〉	    통과 (0.01ms, 4.25MB)       //
//      테스트 5 〉	    통과 (0.01ms, 4.25MB)       //
//      테스트 6 〉	    통과 (0.01ms, 4.32MB)       //
//      테스트 7 〉	    통과 (0.01ms, 4.26MB)       //
//      테스트 8 〉	    통과 (0.01ms, 3.66MB)       //
//      테스트 9 〉	    통과 (0.01ms, 4.33MB)       //
//      테스트 10 〉	통과 (0.01ms, 3.69MB)       //
//      테스트 11 〉	통과 (0.01ms, 4.26MB)       //
//      테스트 12 〉	통과 (0.01ms, 4.25MB)       //
//      테스트 13 〉	통과 (0.01ms, 4.32MB)       //
//      테스트 14 〉	통과 (0.01ms, 4.26MB)       //
//      테스트 15 〉	통과 (0.01ms, 3.73MB)       //
//      테스트 16 〉	통과 (0.01ms, 3.74MB)       //
//      테스트 17 〉	통과 (0.01ms, 4.25MB)       //
//      테스트 18 〉	통과 (0.01ms, 4.25MB)       //
//      테스트 19 〉	통과 (0.01ms, 4.2MB)        //
//      테스트 20 〉	통과 (0.01ms, 4.32MB)       //
//                                                 //
/***************************************************/