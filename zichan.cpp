#include <stdio.h>
#include <algorithm>

typedef struct {
    int fi;
    int se;
}PII;

PII task[10000001];
int Machine[10000001];

void Swap(long long& a, long long& b)
{
    long long temp;
    temp = a;
    a = b;
    b = temp;
}

void QuickSort_increase(long long array[][2], int l, int r)
{
    int pivot = l;
    int i = pivot + 1;
    int j = r;
    if (l >= r)
    {
        return;
    }
    while (i <= j)
    {
        while (array[i][0] <= array[pivot][0] && i <= r)
        {
            i++;
        }
        while (array[j][0] >= array[pivot][0] && j > l)
        {
            j--;
        }
        if (i > j)
        {
            Swap(array[j][0], array[pivot][0]);
            Swap(array[j][1], array[pivot][1]);
        }
        else
        {
            Swap(array[i][0], array[j][0]);
            Swap(array[i][1], array[j][1]);
        }
        QuickSort_increase(array, l, j - 1);
        QuickSort_increase(array, j + 1, r);
    }

}

bool CheckMachine(PII task[], long long& num, long long i, long long t)
{
    long long k = 0;
    for (long long j = 0; j < t; j++) //기계 개수만큼 실행
    {
        if ((Machine[k] != 0) && (task[i].fi >= Machine[k])) //k번째 기계를 사용할 수 있는경우
        {
            num = k; //k번째 기계를 사용해라.
            return true;
        }
        
        k++;
    }
     //새로운 기계를 사용해야 하는 경우
    
     num = k; //k번째 기계를 추가해라.
     return false;
}

long long TskSch(PII task[], long long N)
{
    long long able_machine = 0;
    long long total_machine_num = 0;
    for (long long i = 0; i < N; i++)
    {
        if (CheckMachine(task, able_machine, i, total_machine_num)) //사용 가능한 기계가 있는 경우
        {
            Machine[able_machine] = task[i].se;
        }

        else //새로운 기계를 추가해야 하는 경우
        {
            Machine[able_machine] = task[i].se;
            total_machine_num++;
        }
    }
    return total_machine_num;
}

using namespace std;

int main()
{
   long long N = 0;
   scanf("%d", &N);
    long long answer = 0;

   for (long long i = 0; i < N; i++)
   {
      scanf("%d %d", &task[i].fi, &task[i].se);
   }
    // QuickSort_increase(task, 0, N - 1);
    sort(task, task+N, [&](auto l, auto r){
        return l.fi<r.fi;
    });

    answer = TskSch(task, N);
    printf("%lld", answer);
    return 0;
}