Used for documentation of the Problem Description/Psecudo code

Problem Description:
- We are given an input file that on each line will have the following format
	- <timestamp>|<satellite-id>|<red-high-limit>|<yellow-high-limit>|<yellow-low-limit>|<red-low-limit>|<raw-value>|<component>
- Given this file we have to produce an output file based on alerts. These alerts will be triggered based on rules listed below
- Rules
	- If for the same satellite there are three battery voltage readings that are under the red low limit within a five minute interval.
	- If for the same satellite there are three thermostat readings that exceed the red high limit within a five minute interval.
- Notes From Rules
	- Even though yellow readings are not used now, they should still be configurable
	- Since we base rules off of consecutive readings we will have to tempoarily store the latest readings from the satelitte
	- Since the satelittes all have an unique id, we can use a dictinary to store them


Implementation Description:
1. Start with a class that will iterate through the input file one line at a time
2. Each line will be passed to a class which will check for the alerts being generated
3. This class will check the input that it has been passed, and determine if output needs to be created
4. If output needs to be created, then a file writter class will be called to write to the output file
5. Once file reading is complete the application will close


Class Tree:



Tools Used:
- Git/Git Hub: For pushing data and storing the information
	- Git Kracked is used as a tool to simplify the Git interface
- Python 3.6: For implementation of the code
	- No Modules are used
	
	
Additional implementation wishes:
- If time permits then a nice GUI to help the user view the input data and output will be useful
- Make the GUI able to view the data processing in real time
- Allow for error handling (Even though the original assignment says this is not required, who doesn't want error handling)
