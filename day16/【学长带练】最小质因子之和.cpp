#include <bits/stdc++.h>
#define ll long long

const int N = 3e6, sqrtN = 1733;

ll factors[N + 1], sum[N + 1];
bool is_prime[N + 1];

int main() {
    memset(is_prime, true, sizeof(is_prime));

    for (int p = 2; p < N + 1; ++p) {
        if (is_prime[p])
            factors[p] = p;

        for (int i = p * p; p < sqrtN && i < N + 1; i += p) {
            is_prime[i]= false;

            if (factors[i] == 0)
                factors[i]= p;
        }
    }
    for (int i = 2; i < N + 1; ++i)
        sum[i] = sum[i - 1] + factors[i];

    int t, n;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        scanf("%d", &n);
        printf("%lld\n", sum[n]);
    }
    return 0;
}