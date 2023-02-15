#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 1010, M = 10010;

int n, m, k;
int d[N];
int t[M], a[M], b[M];
int last[N], sum[N];
int tm[N], reduce[N];

int main()
{
    scanf("%d%d%d", &n, &m, &k);

    for (int i = 1; i < n; i++) scanf("%d", &d[i]);
    for (int i = 0; i < m; i++)
    {
        scanf("%d%d%d", &t[i], &a[i], &b[i]);
        last[a[i]] = max(last[a[i]], t[i]);
        sum[b[i]] ++;
    }

    for (int i = 1; i <= n; i++) tm[i] = max(tm[i - 1], last[i - 1]) + d[i - 1];

    while (k--)
    {
        for (int i = n; i >= 2; i--)
        {
            reduce[i - 1] = sum[i];
            if (tm[i] > last[i]) reduce[i - 1] += reduce[i];
        }

        int p = 0;
        for (int i = 1; i <= n; i++)
            if (d[i] && reduce[p] < reduce[i])
                p = i;
        d[p] --;

        for (int i = p; i <= n; i++) tm[i] = max(tm[i - 1], last[i - 1]) + d[i - 1];
    }

    int res = 0;
    for (int i = 0; i < m; i++) res += tm[b[i]] - t[i];

    printf("%d\n", res);

    return 0;
}