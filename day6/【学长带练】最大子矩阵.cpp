#include <bits/stdc++.h>

using namespace std;

class MonotonicQueue {
public:
    deque<int> queue;
    bool max;

    MonotonicQueue(bool max) {
        this->max = max;
    }

    int value() {
        return queue.front();
    }

    void pop(int x) {
        if (value() == x) {
            queue.pop_front();
        }
    }

    bool not_value(int x) {
        return (queue.back() >= x) == max;
    }

    void push(int x) {
        while (!queue.empty()) {
            if (not_value(x)) {
                break;
            }

            queue.pop_back();
        }

        queue.push_back(x);
    }
};

class Pair {
public:
    MonotonicQueue max_queue;
    MonotonicQueue min_queue;

    Pair() : max_queue(true), min_queue(false) {}

    void pop(int x) {
        max_queue.pop(x);
        min_queue.pop(x);
    }

    void push(int x) {
        max_queue.push(x);
        min_queue.push(x);
    }

    int max() {
        return max_queue.value();
    }

    int min() {
        return min_queue.value();
    }
};

class Window {
public:
    vector<vector<int>> matrix;
    int limit;
    int up;
    int down;
    int width;
    int length;
    vector<Pair> queues_list;

    Window(vector<vector<int>> matrix, int limit, int up, int down) {
        this->matrix = matrix;
        this->limit = limit;
        this->up = up;
        this->down = down;
        this->width = down - up + 1;
        this->queues_list = vector<Pair>(width);

        this->length = 0;
    }

    int size() {
        return length * width;
    }

    void pop(int k) {
        length--;

        for (int i = 0; i < width; i++) {
            queues_list[i].pop(matrix[i + up][k]);
        }
    }

    void push(int k) {
        length++;

        for (int i = 0; i < width; i++) {
            queues_list[i].push(matrix[i + up][k]);
        }
    }

    bool not_stable() {
        if (length == 0) {
            return false;
        }

        vector<int> max_list(width);
        vector<int> min_list(width);

        for (int i = 0; i < width; i++) {
            max_list[i] = queues_list[i].max();
            min_list[i] = queues_list[i].min();
        }

        return *max_element(max_list.begin(), max_list.end()) - *min_element(min_list.begin(), min_list.end()) > limit;
    }
};

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> matrix(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }

    int limit;
    cin >> limit;

    int M = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            Window window(matrix, limit, i, j);

            for (int k = 0; k < m; k++) {
                window.push(k);

                while (window.not_stable()) {
                    window.pop(k - window.length + 1);
                }

                M = max(M, window.size());
            }
        }
    }

    cout << M;
}