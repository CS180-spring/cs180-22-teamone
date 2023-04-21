#ifndef RECORD_H
#define RECORD_H

#include <string>
#include <map>
#include <json/json.h>

struct Record{
    std::string id;
    std::map <std::string, Json::Value> fields; 
};

#endif