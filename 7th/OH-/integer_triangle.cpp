#include <vector>
using namespace std;
// C Style
#if 1
#include <string.h>
int solution(vector<vector<int>> triangle)
{
    int i, j, size;
    int ans = 0;
    int** arr;
    size = triangle.size();

    // Memory Allocation & Memory Rst
    arr = new int*[size];
    for (i=0; i<size; i++)
    {
        arr[i] = new int[i+1];
        memset(arr[i], 0, sizeof(int)*(i+1));
    }

    arr[0][0] = triangle[0][0];
    for (i = 1; i < size; i++)
    {
        arr[i][0] = arr[i-1][0] + triangle[i][0];
        arr[i][i] = arr[i-1][i-1] + triangle[i][i];

        for (j = 1; j < i; j++)
            arr[i][j] = max(arr[i-1][j-1], arr[i-1][j]) + triangle[i][j];
//            arr[i][j] = arr[i-1][j-1] > arr[i-1][j] ? (arr[i-1][j-1]+triangle[i][j]) : (arr[i-1][j]+triangle[i][j]);
    }

    // Calculate answer & Delete Memory
    for (int i = 0; i < size; i++)
    {
        ans = max(ans, arr[size-1][i]);
//        ans = arr[size-1][i] > ans ? arr[size-1][i] : ans;
        delete arr[i];
    }
    delete arr;

    return ans;
}
/*
정확성  테스트
테스트 1 〉	통과 (0.01ms, 4.33MB)
테스트 2 〉	통과 (0.01ms, 3.68MB)
테스트 3 〉	통과 (0.01ms, 4.32MB)
테스트 4 〉	통과 (0.01ms, 4.33MB)
테스트 5 〉	통과 (0.03ms, 4.33MB)
테스트 6 〉	통과 (0.02ms, 4.33MB)
테스트 7 〉	통과 (0.04ms, 4.32MB)
테스트 8 〉	통과 (0.02ms, 4.32MB)
테스트 9 〉	통과 (0.01ms, 4.32MB)
테스트 10 〉통과 (0.01ms, 4.33MB)
효율성  테스트
테스트 1 〉	통과 (0.54ms, 8.1MB)
테스트 2 〉	통과 (0.45ms, 6.84MB)
테스트 3 〉	통과 (0.65ms, 8.61MB)
테스트 4 〉	통과 (0.56ms, 8.05MB)
테스트 5 〉	통과 (0.57ms, 7.86MB)
테스트 6 〉	통과 (0.59ms, 8.52MB)
테스트 7 〉	통과 (0.55ms, 8.39MB)
테스트 8 〉	통과 (0.49ms, 7.54MB)
테스트 9 〉	통과 (0.52ms, 7.79MB)
테스트 10 〉통과 (0.63ms, 8.29MB)
*/

// CPP style
#else
int solution(vector<vector<int>> triangle)
{
    int i, j;
    int ans = 0;
    vector<vector<int>> arr(triangle.size(), vector<int>(triangle.size(), 0));

    arr[0][0] = triangle[0][0];
    for (i = 1; i < arr.size(); i++)
    {
        arr[i][0] = arr[i - 1][0] + triangle[i][0];
        arr[i][i] = arr[i - 1][i - 1] + triangle[i][i];
        for (j = 1; j < i; j++)
            arr[i][j] = max(arr[i - 1][j - 1], arr[i - 1][j]) + triangle[i][j];
    }

    for (int i = 0; i < arr.size(); i++)
        ans = max(ans, arr[arr.size() - 1][i]);

    return ans;
}
/*
정확성  테스트
테스트 1 〉	통과 (0.01ms, 4.33MB)
테스트 2 〉	통과 (0.01ms, 4.32MB)
테스트 3 〉	통과 (0.01ms, 4.32MB)
테스트 4 〉	통과 (0.01ms, 4.27MB)
테스트 5 〉	통과 (0.05ms, 4.32MB)
테스트 6 〉	통과 (0.02ms, 3.66MB)
테스트 7 〉	통과 (0.07ms, 4.27MB)
테스트 8 〉	통과 (0.02ms, 4.32MB)
테스트 9 〉	통과 (0.01ms, 4.38MB)
테스트 10 〉통과 (0.01ms, 4.26MB)
효율성  테스트
테스트 1 〉	통과 (0.82ms, 8.36MB)
테스트 2 〉	통과 (0.65ms, 7.24MB)
테스트 3 〉	통과 (0.92ms, 8.99MB)
테스트 4 〉	통과 (0.80ms, 8.63MB)
테스트 5 〉	통과 (0.69ms, 8.14MB)
테스트 6 〉	통과 (0.86ms, 9.05MB)
테스트 7 〉	통과 (0.90ms, 8.88MB)
테스트 8 〉	통과 (0.73ms, 7.77MB)
테스트 9 〉	통과 (0.74ms, 8.11MB)
테스트 10 〉통과 (0.89ms, 8.81MB)
*/
#endif