#include <iostream>
#include <list>
void print(std::list<int> a) {
    for(std::list<int>::iterator it=a.begin();
            it!=a.end(); it++)
        std::cout << ' ' << *it;
    std::cout << '\n';
};
int main() {
    std::list<int> a;
    // put 9,8,7,6,5,4,3,2,1 onto the list.
    for(int i=0; i<9;++i)
        a.push_back(9-i);
    print(a); // here the list contains (9,8,7,6,5,4,3,2,1).
    a.sort(); // in the <list> library!
    print(a); // here the list contains (1,2,3,4,5,6,7,8,9).
};
