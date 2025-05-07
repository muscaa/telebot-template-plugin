#include <iostream>

extern "C" void plugin_main() {
    std::cout << "Plugin main function called." << std::endl;
}
