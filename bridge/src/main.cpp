#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>
#include <cstring>
#include <iostream>

int main()
{
    int sock = socket(AF_INET, SOCK_DGRAM, 0); // Create a IPv4 UDP socket

    sockaddr_in addr{}; // Create socket struct
    addr.sin_family = AF_INET;  // Tell it it is IPv4
    addr.sin_port = htons(9021);

    inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr);

    bind(sock, (sockaddr*)&addr, sizeof(addr));

    std::cout << "Listening on 127.0.0.1:9021...\n";

    char buffer[1024];
    while(true)
    {
        sockaddr_in sender{};
        socklen_t len = sizeof(sender);
        ssize_t n = recvfrom(sock, buffer, sizeof(buffer) - 1, 0, (sockaddr*)&sender, &len);
        
        buffer[n] = '\0';

        std::cout << "Received: " << buffer << "\n";
    }
    close(sock);
}