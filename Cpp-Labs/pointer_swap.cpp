#include <iostream>
using namespace std;

void swap(int* a, int* b) {
  int temp = *a;    // Temporarily save the address of num1 value
  *a = *b;          // Change the value of the num1 to num2
  *b = temp;        // Change the value of num2 from saved temp variable
}

void printArray(int *ptr, int size) {
	cout << "{ ";
	for (int i = 0; i < size; i++) {
		cout << *(ptr + i) << " ";
	}
	cout << "}";
}

int main() {
	int num1{};
	int num2{};
  
  int data[] = {64, 34, 25, 12, 22, 11, 90};
  int n = 7;
    
  cout << "Welcome to interger swapper with pointers.\n\n";
	cout << "Your array has a size of " << n << " items.\n" << endl;
	cout << "Your array: ";
	
	printArray(data, n);
	
	cout << endl << endl; // new line for redability in CLI
    
  do {
    	
		cout << "Enter 'first' number index to swap (starting from index 0): ";
    cin >> num1;
    	
    cout << endl; // new line for redability in CLI
		
	} while (num1 > n || num1 < 0);
	
	do {

		cout << "Enter 'second' number index to swap (starting from index 0): ";
    cin >> num2;
  
		cout << endl; // new line for redability in CLI	
	
	} while (num2 > n || num2 < 0);
	
	swap(*(data + num1), *(data + num2)); // *(data + num1) similar to data[num1] in Python
	
	cout << "Your new array: ";
	
	printArray(data, n);
	    
  return 0;
}
