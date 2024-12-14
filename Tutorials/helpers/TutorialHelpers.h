#ifndef ORCASDK_TUTORIAL_HELPERS
#define ORCASDK_TUTORIAL_HELPERS

#include <iostream>
#include <string>

//Requests and returns a number from stdin, complaining and exiting if it is not a number, or is negative
int obtain_serial_port_number();

//Blocks and waits for a number from stdin
int get_int_from_stdin();

#endif