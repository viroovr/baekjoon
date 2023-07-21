#include <stdio.h>
#include <vector>
#include <list>
#include <iostream>
#include <stack>
#include <map>
#include <set>
#include <queue>
using namespace std;

void set_ex(void){
    printf("set example\n");
    set<int> s;
    s.insert(456);
    s.insert(12);
    s.insert(456);
    s.insert(7890);
    s.insert(7890);
    s.insert(456);
    printf("size: %ld\n", s.size());
    for(auto i : s)
        printf("%d\n", i);
}

void map_ex(void){
    printf("map  example\n");
    map<string, int> m;
    m["Hyeonwon"] = 40;
    m["Sky"] = 100;
    m["Jerry"] = 50;
    printf("size : %ld\n", m.size());
    for ( auto p : m)
        printf("%s, %d\n", p.first.c_str(), p.second);
}

void prior_queue_ex(void){
    printf("priority queue(max-heap) example\n");
    priority_queue<int> pq;
    pq.push(456);
    pq.push(123);
    pq.push(789);
    printf("size: %ld\n", pq.size());
    while(!pq.empty()){
        printf("%d\n", pq.top());
        pq.pop();
    }
}

void queue_ex(void){
    printf("queue example\n");
    queue<int> q;
    q.push(123);
    q.push(456);
    q.push(789);
    printf("size : %ld", q.size());
    while(!q.empty()){
        printf("%d\n", q.front());
        q.pop();
    }
}

void stack_ex(void){
    printf("stack example\n");
    stack<int> s;
    s.push(123);
    s.push(456);
    s.push(789);
    printf("size : %ld\n", s.size());
    while (!s.empty()) {
        printf("%d\n", s.top());
        s.pop();
    }
}

void linked_list(void){
    printf("linked list example\n");
    list<int> l;
    l.emplace_back(0);
    l.emplace_back(1);
    l.emplace_back(2);
    l.emplace_back(3);
    printf("size: %ld\n", l.size());
    for (auto i : l)
        printf("%d\n", i);
}

void vector_ex(void){
    printf("vector example\n");
    vector<pair<int, int>> v;
    v.push_back(make_pair(123,456));
    v.emplace_back(789, 987);
    printf("size: %ld\n", v.size());
    for (auto p : v)
        printf("%d, %d\n", p.first, p.second);
}
int main(){
    // vector_ex();
    // linked_list();
    // stack_ex();
    // queue_ex();
    // prior_queue_ex();
    map_ex();
}