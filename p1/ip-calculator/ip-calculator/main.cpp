//  CS 331 - Professor Li
//  Project 1
//  main.cpp
//  ip-calculator
//  Created by Benjamin Webb on 9/17/19.
//

#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <limits>

int main() {
    // Define Variables: ip is the IPv4 address; a, b, c, and d are the bytes of the address
    // prefix is the length of the prefix; ma, mb, mc, and md are the mask bytes of the address
    char ip[16];
    unsigned short a, b, c, d;
    int prefix, ma, mb, mc, md;
    
    // Request IP address and parse
    std::cout << "Enter IP Address: ";
    std::cin >> ip;
    sscanf(ip, "%hu.%hu.%hu.%hu", &a, &b, &c, &d);
    // Error Checking for IP
    while(1){
        if(std::cin.fail() || 0>a or a>255 || 0>b or b>255 || 0>c or c>255 || 0>d or d>255) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
            std::cout << "You have entered a wrong input";
            std::cout << "\nPlease enter a valid IPv4 address: ";
            std::cin >> ip;
            sscanf(ip, "%hu.%hu.%hu.%hu", &a, &b, &c, &d);
        }
        if(!std::cin.fail() && a>=0 and a<=255 && b>=0 and b<=255 && c>=0 and c<=255 && d>=0 and d<=255)
            break;
    }
    
    // Request prefix
    std::cout << "Enter prefix length: ";
    std::cin >> prefix;
    // Error Checking for prefix
    while(1){
        if(std::cin.fail() or prefix < 0 or prefix > 32) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
            std::cout << "You have entered a wrong input";
            std::cout << "\nPlease enter a valid prefix between 0 and 32: ";
            std::cin >> prefix;
        }
        if(!std::cin.fail() and prefix >= 0 and prefix <= 32)
            break;
    }
    // Find mask from prefix
    ma = 256 - pow(2, 8 - std::min(prefix,8));
    if (prefix > 8)  {mb = 256 - pow(2, 8 - std::min(prefix-8,8)); } else {mb = 0;}
    if (prefix > 16) {mc = 256 - pow(2, 8 - std::min(prefix-16,8));} else {mc = 0;}
    if (prefix > 24) {md = 256 - pow(2, 8 - std::min(prefix-24,8));} else {md = 0;}
    
    std::cout << "\nSubnet Address: " << (a & ma) << '.' <<  (b & mb) << '.' << (c & mc) << '.' <<  (d & md);
    std::cout << "\nFirst Host: " << (a & ma) << '.' <<  (b & mb) << '.' << (c & mc) << '.' <<  (d & md) + 1;
    std::cout << "\nBroadcast Address: " << ((a & ma)|(255^ma)) << '.' <<  ((b & mb)|(255^mb)) << '.' << ((c & mc)|(255^ mc)) << '.' <<  (255^md);
    std::cout << "\nLast Host: " << ((a & ma)|(255^ma)) << '.' <<  ((b & mb)|(255^mb)) << '.' << ((c & mc)|(255^ mc)) << '.' <<  (255^md) - 1;
    std::cout << "\nSubnet Mask: " << ma << '.' << mb << '.' << mc << '.' << md << "\n\n";
    std::cin >> prefix;
    return 0;
}
