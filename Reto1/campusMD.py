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
        #try:
            print ("1. Gestión de pacientes","2. Gestión de veterinarios","3. Gestión de cítas médicas","4. Salir",sep="\n")
            opc = int(input("> "))
            if opc == 1:
                pac.MainMenu()
            elif opc == 2:
                vet.MainMenu()
            elif opc == 3:
                citas.MainMenu()
            elif opc == 4:
                run = False
            else:
                print("Opción no valida")
        #except Exception as e:
        #    print("Se ha producido un Error : \n",e)
            os.system("sleep 3")