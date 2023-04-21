#include <iostream>
#include <fstream>
#include <map>
#include <json/json.h>
#include "record.h"
using namespace std;

int main(){
    //temp file name we can add functionality to have multiple databases
    //rightnow it has 1 database and it can add and remove different records from it. 
    string filename = "database.json";
    int choice;
    cout << "1. Create record" << endl;
    cout << "2. Read record" << endl;
    cout << "3. Update record" << endl;
    cout << "4. Delete record" << endl;
    cout << "5. Exit" << endl;


    map<std::string, Json::Value> fields;
    string id;
    string field;
    string value;
    Record record;

    while (true)
    {
        cout << "Enter your choice: "; 
        cin >> choice;

        switch(choice){
            case 1:
                cout << "Enter ID: ";
                cin >> record.id;
                
                cout << "Enter field name (type exit to stop): ";

                while(true){
                    cin >> field;
                    if(field == "exit"){
                        break;
                    }

                    cout << "Enter value for " << field << ": ";
                    cin >> value; 
                    fields[field] = Json::Value(value);
                }
                record.fields = fields;
                createRecord(record, filename);
                break;

            case 2:
                cout << "Enter ID: ";
                cid >> id;
                readRecord(id, filename);
                break;
            
            case 3:
                cout << "Enter ID: ";
                cin >> id; 
                cout << "Enter field name (type exit to stop): ";
                while(true){
                    cin >> field;
                    if(field == "exit"){
                        break;
                    }

                    cout << "Enter value for " << field << ": ";
                    cin >> value; 
                    fields[field] = Json::Value(value);
                }
                updateRecord(id, fields, filename);
                break;
            
            case 4:
                cout << "Enter ID: ";
                cin >> id; 
                deleteRecord(id, filename);
                break;
            
            case 5:
                return 0;
            
            default:
                cout << "Invalid choice." << std::endl;
        }

        fields.clear();
        cout << endl;

    }
    return 0;
 }