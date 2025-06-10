#include <iostream>
using namespace std;

// Function to add two numbers
int addNumbers(int a, int b) {
    return a + b;
}

int main() {
    int num1 = 5, num2 = 3;
    int sum = addNumbers(num1, num2);
    
    cout << "The sum is: " << sum << endl;
    return 0;
}
