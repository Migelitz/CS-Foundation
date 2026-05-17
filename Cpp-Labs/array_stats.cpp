#include <iostream>
#include <vector>
#include <sstream>
#include <limits>
#include <string>
#include <algorithm>
#define MAX_ARR_SIZE 100
#define MIN_ARR_SIZE 1
using namespace std;

// Sum function
int sum(vector<int> arr, int arr_size){
	int sum = 0;
	for (int i = 0; i < arr_size; i++) {
		sum += arr[i];
	}
	return sum;	
}
 
int main()
{
	int arr_size, num;
	string arr_val;
	vector<int> arr;

  // Get array size
	do 
	{
		cout << "How many numbers (MAX 100): " << endl;
		cin >> arr_size;
    cin.ignore();
		
		if (arr_size > 100 || arr_size < 1) {
			cout << "Please choose between 1-100." << endl;
		} else if (cin.fail()) {
			cerr << "Please enter integers only." << endl;
			cin.clear();
			cin.ignore();
		}
	} while (arr_size > MAX_ARR_SIZE || arr_size < MIN_ARR_SIZE);

  // Get array input data
	cout << "Enter " << arr_size << " number/s:" << endl;
	getline(cin, arr_val);

    stringstream ss(arr_val);
  
    while (ss >> num) {
        arr.push_back(num);
    }

    sort(arr.begin(), arr.end());

    cout << endl;
    cout << endl;
    
    cout << "Maximum: " << arr[0] << endl;
    cout << "Minimum: " << arr[arr_size - 1] << endl;
    cout << "Sum: " << sum(arr, arr_size) << endl;

	return 0;
}
