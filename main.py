from conversion import Conversion


#for input type - b is binary
#               - s is string
#               - q is quaternary (dna)

input_type = ""
output_type = ""
user_input = ""

def transform(input_of_user, input_type, output_type):
    #sets to fonction_name the name of the fonction the input and output type correspond in the conversion class
    #if the output type is String_reverse or String_format the fonction name is String_reverse or String_format
    if output_type not in ("String_reverse", "String_format"):
        fonction_name = f"{input_type}_to_{output_type}"

    else:
        if output_type == "String_reverse":
            fonction_name = "String_reverse"
        else:
            fonction_name = "String_format"

    #creats an instance of conversion to run the __init__ fonction
    conversion_instance = Conversion()

    #from the instance already running search for the Conversion class search for the fonction fonction_name
    conversion_fonction = getattr(conversion_instance, fonction_name)
    #after having found the fonction give it as input the user input 
    result = conversion_fonction(str(input_of_user))

    return result
    

def convert_user_inputs(input_of_user):
    run = False
    #sets the user input to lower case and remove all white space
    input_of_user=input_of_user.lower().strip()

    #check is the user input is binary
    if input_of_user in ("b", "binary"):
        input_of_user = "Binary"
        print ("User input has been set to binary\n")
        run = True

    #check is the user input a string
    elif input_of_user in ("s","str","string"):
        input_of_user = "String"
        print ("User input has been set to string\n")
        run = True

    #check is the user input dna
    elif input_of_user in ("quaternary", "q", "dna"):
        input_of_user = "DNA"
        print ("User input has been set to quaternary\n")
        run = True
    
    #check is the user input is a string format
    elif input_of_user in ("string_format", "sf"):
        input_of_user = "String_format"
        print ("User input has been set to string format\n")
        run = True

    #check is the user input a string reverse
    elif input_of_user in ("string_reverse", "sr"):
        input_of_user = "String_reverse"
        print ("User input has been set to string reverse\n")
        run = True

    #if the user input is invalide or not recognisable print invalide input
    else:
        print ("The input you gave is invalid")

    return input_of_user, run

if __name__ == "__main__":
    while True:

        run = False
        while run == False:
            input_type = input("Input type : ")
            input_type, run = convert_user_inputs(input_type)

        run = False
        while run ==False:
            output_type_user = input("Output type : ")
            output_type, run = convert_user_inputs(output_type_user)

        user_input = input("What would you like to convert to " + output_type_user + " : ")

        converted = transform(user_input, input_type, output_type)

        print (converted)