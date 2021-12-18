#include <stdio.h>
#include <string.h>

int main()
{
    int nStr, nPrefix;
    char** pStr;
    char** pPrefix;

    int nAnswer=0;

    scanf("%d %d", &nStr, &nPrefix);

    pStr = new char*[nStr];
    pPrefix = new char*[nPrefix];
    for(int i=0; i<nStr; i++)
    {
        pStr[i] = new char[500];
        scanf("%s", pStr[i]);
    }
    for(int i=0; i<nPrefix; i++)
    {
        pPrefix[i] = new char[500];
        scanf("%s", pPrefix[i]);
    }

    for(int i=0; i<nPrefix; i++)
    {
        for(int j=0; j<nStr; j++)
        {
            if(!strncmp(pPrefix[i], pStr[j], strlen(pPrefix[i])))
            {
                nAnswer++;
                break;
            }
        }
    }

    printf("%d", nAnswer);
    
    for(int i=0; i<nStr; i++)
        delete[] pStr[i];
    for(int i=0; i<nPrefix; i++)
        delete[] pPrefix[i];

    delete pStr;
    delete pPrefix;

    return 0;
}

//5 10
//baekjoononlinejudge
//startlink
//codeplus
//sundaycoding
//codingsh
//baekjoon
//star
//start
//code
//sunday
//coding
//cod
//online
//judge
//plus