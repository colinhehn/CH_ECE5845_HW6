## ECE:5845 Modern Databases HW6
Here's my MongoDB & Python CLI for our Homework 6 assignment. Instructions for operation can be found below.

### Instructions:
1. Ensure that you have MongoDB installed and running on your machine, specifically at port 27017. If the port is different, please modify the code in chehn-hw6.py to fit your port (can be found under the main function).
2. Running the CLI
   1. The program can be run from the command line with "python chehn-hw6.py [ARGUMENTS]" when cd'd into the same directory as the file.
      1. If you are running python3 on your machine, please replace "python" with "python3" in the above command.
   2. The arguments to execute each function are as follows:
      1. FUNCTION -> The first argument is which function you want to run. A list of functions can be found in the next README section below.
      2. FLAGS -> using -lat, -lon, and -id allows you to specify what parameters should be put into said function. These aren't required for all of them, and you can see how they're used for each specific function below.
      3. A correct use of the format looks like this *"python chehn-hw6.py closest_businesses -lat 38.48373 -lon 58.20294"*
3. Parameters for each function
   1. Search for the three closest businesses to a given location (lat/long).
      1. "python chehn-hw6.py closest_businesses -lat [LATITUDE] -lon [LONGITUDE]"
      2. Takes -lat to specify latitude to search at, takes -lon to specify the longitude to search at.
   2. Submit a review for a business, given its ID.
      1. "python chehn-hw6.py submit_review -id [BUSINESS_ID]"
      2. Takes -id to specify the business_id to submit the review for. There should only be one business for every business_id.
      3. Once executed, you will be asked to give a rating 1-5 stars. Please enter a number between 1 and 5, inclusive.