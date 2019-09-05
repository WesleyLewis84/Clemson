from socket import *    # This import statement allows us to create sockets, and use the various constants defined by the socket library
                        # Your IDE may suggest that there is an error in this import statement. This is a warning that we are importing more
                        # components from the socket library than we are actually using in our code, and can be ignored for this assignment.
from struct import *    # This import statement allows us to use the pack/unpack functions
import time             # This import statement allows us to get the current time, which we will use for latency measurements
import argparse         # This import statement allows us to pass in command line arugments to our program

# NOTE: DO NOT CHANGE THE NAME OF THIS CLASS
class LatencyTest:
    def __init__(self, server_host='3600cpsc.computing.clemson.edu', server_port=3611):
        # HINT: Make sure all variables you create here are initialized as part of self, so that you can access them from
        #       other functions defined in this class
        #       e.g. define variables as 'self.new_variable = ....', not as 'new_variable = ....'
        #       Variables that are not initialized as part of self are local to this function only 

        # TODO: Establish a TCP connection with server 
        self.tcpClient = socket(AF_INET, SOCK_STREAM)
        
        # TODO: Connect to the server at the specified port and hostname using our new socket
        self.tcpClient.connect(server_host, server_port)
        
    def measure_real_latency(self, num_tests = 25, test_message='abcdefghijklmnopqrstuvwxyz'):
        # TODO: Send the command to the server that we're ready to begin measuring real latencies
        #       The command is '!!!begin_real_latency_measurement', and the server is expecting 
        #       the message to be encoded using the ascii encoding
        
        # TODO: Listen for a response from the server confirming that it has successfully received the command
        #       The expected response is the string 'OK', in the ascii encoding
        
        if (response == "OK"):
            # Initialize a list to store the test results
            test_rtts = []

            # Perform all of the tests
            for i in range(num_tests):
                # TODO: Encode the test message using the ascii encoding.                
                
                # TODO: Record the current time, for use in latency calculations
                
                # TODO: Send the test message to the server using the socket created in __init__
                
                # TODO: Listen for a response from the server. The server will echo back whatever it is sent.
                
                # TODO: Record the current time, for use in latency calculations
                
                # TODO: Compute the RTT for this test.

                # TODO: Append the computed RTT to the test_rtts list that was initialized before beginning the tests for loop
                
                # Pass is included here because no code has been written yet for this loop, and Python requires that some code exist
                # in all defined functions, loops, etc. You can remove pass once you have written your code, or ignore it and leave it here.
                pass

            # Compute and return the average RTT. We do this by summing all of the values in the test_rtts list, 
            # and then dividing this value by the length of the test_rtts list
            total_RTT = sum(test_rtts)
            return total_RTT/len(test_rtts))
    
    def compute_simulated_latency(self, num_tests = 25):
        # TODO: Send the command to the server that we're ready to begin simulating latencies
        #       The command is '!!!begin_simulated_latency_measurement', and the server is expecting 
        #       the message to be encoded using the ascii encoding
        
        # TODO: Listen for a response from the server confirming that it has successfully received the command
        #       The expected response is the string 'OK', in the ascii encoding
        
        if (response == "OK"):
            # Initialize a list to store the test results
            test_simulations = []
            
            # Perform all of the tests
            for i in range(num_tests):
                # TODO: Send a request to the server for simulated latency values. The server will respond with 
                #       simulated latency values to ALL received messages, so long as it is in the correct state.
                #       Any message can be used to request the simulated latency values, so long as the server
                #       is in the correct state.

                # TODO: Listen for a response from the server. The server will send back a byte array containing the simulated latency values
                
                # TODO: Unpack the response from the server. The response format is as follows
                # - int: the length of simulated packet, in bits
                # - int: the simulated bandwidth, in bits per second
                # - double: the simulated distance between hosts
                # - double: the speed of data in the simulated medium
                # - double: the total processing delay
                # - double: the total queuing delay
                
                # TODO: Compute the simulated latency, based on the values received from the server

                # TODO: Send this result to the server as a float value. Do NOT send this as an ascii-encoded string, 
                #       like we've done for previous messages. You will need to use pack to send it as a float
                
                # TODO: Listen for a response from the server. The server will respond with a byte array containing a single bool, 
                # indicating where our response was correct or not.

                # TODO: Unpack the response from the server. The response format is as follows
                # - bool: whether or not your calculated latency agreed with the server's calculated latency
                # HINT: Remember unpack returns a list of values, even if you're only unpacking a single value.

                # TODO: Append the server's response to the test_simulations list that was initialized before beginning the tests for loop

            # Return the results of the simulated latency tests
            return test_simulations
        
if __name__ == "__main__":
    # Augment parser allows us to pass in arguments via the command line. The code below allows you to specify 
    # the hostname and the port number for the server your program communicates with.
    # If no arguments are provided, the program will default to connecting to ada1.computing.clemson.edu and port 3601
    # You can use the arguments as follows:
    # >> python main.py --host [your_host_name.edu] --port [your_port_number]
    parser = argparse.ArgumentParser(description='CPSC3600 Fall 2019 assignment #1.')
    parser.add_argument('-H', '--host', help='The hostname to connect to', default='cpsc3600.computing.clemson.edu')
    parser.add_argument('-P','--port', type=int, help='The port to connect to', default=3611)
    args = parser.parse_args()

    # Create an instance of the LatencyTest class, using the specified hostname and port
    l = LatencyTest(server_host=args.host, server_port=args.port)
    # Call the measure_real_latency function to measure the real latency in communications between this program and the server.
    # We use a large test_message to increase the length of the latency
    real_rtt = l.measure_real_latency(test_message = "abcdefghiklmnopqrstuvwxyz")
    
    # Print out the results of latency measurements
    print("Real RTT: " + str(real_rtt))
        
    # Call compute_simulated_latency to compute simulated latency values based on values created by the server
    simulated_latency = l.compute_simulated_latency()

    # Print out the results of simulated latency measurements
    print("Simulated Latency: " + str(simulated_latency))