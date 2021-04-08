#include <iostream>
#include <algorithm>



using namespace std;

int getSum(int scores[], const int count){
    int sum = 0;
    for(int i = 0; i < count; i++){
        sum += scores[i];
    }
    return sum;
}

int main(){
    cout << "Enter the score count: ";
    int maxSize;
    cin >> maxSize;

    int* const scores = new int[maxSize];
    int count = 0;
    while(true){
        cout << "Enter command: (add, sum, average, list, quit) ";
        string com;
        cin >> com;
        transform(com.begin(), com.end(), com.begin(), ::toupper);

        int i;
        if (com == "ADD"){
            if (maxSize == i){
                cout << "Too many scores" << endl;
                continue;
            }

            cout << "Enter score: ";
            int add_s;
            cin >> add_s;
            if (add_s < 0 || add_s > 100){
                cout << "Score should be between 0 and 100" << endl;
            }
            else{
                scores[i++] = add_s;
                cout << add_s << " added" << endl;

            }
        }
        else if(com == "SUM"){
            
            cout << "Sum: " << getSum(scores, count) << endl;
        }
        else if(com == "LIST"){
            int j = 0;
            for (j = 0; j < i; j++){
                cout << scores[j] << " ";
            }
            cout << endl;
        }
        else if(com == "AVERAGE"){
            int j = 0;
            float sum = 0.0;
            for (j = 0; j < i; j++){
                sum += scores[j];
            }
            const float avg = sum / static_cast<float>(j);
            cout << "Average: " << avg << endl;
        }
        else if(com == "QUIT"){
            cout << "Bye" << endl;
            break;
        }
    }
    delete[] scores;
    return 0;
}