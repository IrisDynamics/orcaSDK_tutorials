#include "TutorialHelpers.h"

#include <iostream>
#include <string>

//Requests and returns a number from stdin, complaining and exiting if it is not a number, or is negative
int obtain_serial_port_number() {
	std::cout << "Please input the serial port of your connected motor." << std::endl;

	int com_port = get_int_from_stdin();

	while (com_port < 0) {
		std::cout << "Please enter a positive value for your serial port.\n" << std::endl; 
		com_port = get_int_from_stdin();
	}

	return com_port;
}

int get_int_from_stdin()
{
	std::string com_port_str;
	std::cin >> com_port_str;

	int com_port = -1;
	try {
		com_port = stoi(com_port_str);
	}
	catch (std::exception& e) {
		std::cout << "Was unable to read the input. Error message: " << e.what() << std::endl;
	}

	return com_port;
}