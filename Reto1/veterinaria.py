import os
import pacientes as pac
import veterinarios as vet
import citas

if __name__ == '__main__':
    opc = 0
    run = True
    while run:    
        os.system('clear')
        print ('+','-'*55,'+')
        print ('|{:^57}|'.format('CENTRO VETERINARIO CAMPUSMD'))
        print ('+','-'*55,'+')
        print ("1. Gestión de pacientes","2. Gestión de veterinarios","3. Gestión de cítas médicas","4. Salir",sep="\n")
        opc = int(input("> "))
        if opc == 1:
            pac.MainMenu()
