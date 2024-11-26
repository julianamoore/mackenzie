#each son is -1000
#todo valor de saude pode ser deduzido
#pessoas co idade acima de 65 anos tem 20% a mais de deducao sobre o valor ja deduzido
#gere um arquivo com o CPF e o total de dudcao de cada funcionario
#usar diccionario, fatiamento, arquivos, e funcoes

#dictionary with fixed values of codes and the deduction
code_value = {"AB12":1000, "CD34":1500, "EF56":2000, "GH78":500}

#input to hard code
#02847890764 28/05/2003 AB12;4000;Son1;Son2;Son3
#86332577892 16/01/2001 CD34;1000;Son1;Son2
#07784277126 01/12/1954 EF56;500
#94628347628 21/08/2002 GH78;2500;Son1

def income_tax():
    #defining the code to value dictionary
    code_value = {"AB12":1000, "CD34":1500, "EF56":2000, "GH78":500}

    #setting initial variables
    cont = "y"
    dict_data = {}
    today = [27, 11, 2024]

    #while loop so the user can continue adding data
    while cont == "y":
        data = input("Input the data of the employee (CPF, Birthdate, Code;Value;Children) ")
        cont = input("Do you want to continue? (y/n) ")

        #add data into a dictionary, with the key being CPF and the data everything after
        dict_data[data[:11]] = data[12:]
    
#02847890764 28/05/2003 AB12;4000;Son1;Son2;Son3
#     28 = 12      A = 23

    #for loop to go through every key in the dictionary with all the data
    for key in dict_data:
        #assigning initial values to helper variables and data of the employees
        tax = 0
        cpf = key
        birth = (dict_data[key])[:10]
        alldata = (dict_data[key])[11:]
        alldata = alldata.split(";")
        code = alldata[0]
        value = int(alldata[1])
        children = len(alldata) - 2

        #calculating the age, splitting the birthdate into a list and turning it into an integer so i can calculate the age
        birthdate = birth.split("/")
        age = int(today[2]) - int(birthdate[2])

        #if statement to check if the birthday hasnt happened yet
        if (int(today[1]) < int(birthdate[1])) or (int(today[1]) == int(birthdate[1]) and int(today[0]) < int(birthdate[0])):
            age = age - 1

        #to add value to the tax corresponding to the already given dictionary value-data stuff
        if code in code_value:
            tax += code_value[code]
        
        #adding 1k for every children
        if children > 0:
            tax += (children * 1000)
        
        #adding the value already given in teh data
        tax += value

        #if the age is 65 or above, add 20% to the deductible
        if age >= 65:
            tax *= 1.2
        
        #open a new file, write the ammounts, and append it to said new file
        with open("income_tax.txt", "a") as income_tax_file:
            income_tax_file.write(f"Employee {cpf} has {tax} ammount of tax deduction. \n")

#running the function
income_tax()