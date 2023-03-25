from getpass import getpass
from mysql.connector import connect, Error
import os 

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="inptreservation",
    ) as connection:
        print(connection)
except Error as e:
    print(e)


        
if connection.user=="admin" :
    while True : 
        print("Veuillez choisir un nombre pour l'opération à effectué :")
        print("1--> Ajouter des étudiants")
        print("2--> Supprimer des étudiant")
        print("3--> Ajouter des assistants")
        print("4--> Supprimer des assistants")
        print("5--> Ajouter des locaux")
        print("6--> Supprimer des locaux")
        print("7--> Ajouter des spécialités")
        print("8--> Ajouter des réservations")
        print("9--> Afficher tous les étudiants")
        print("10-> Afficher tous les assistants")
        print("11-> Afficher toutes les réservations")
        print("12-> Afficher les réservations d'un étudiant spécifique: ")
        print("12-> Afficher les réservations d'un assistant spécifique: ")
        print("0--> Quitter le programme ! ")
        x=int(input())
        if x==1 : 
            lis=[]
            nb = int(input("combien d'etudiant vous voullez inserer : "))
            for i in range(nb) :
                etu=(input("CIN: "), input("nom: "), input("prenom: "), input("numero de telephone: "))
                print("---------------------------------------------------------------------------------------------")
                lis.append(etu)
            connection.reconnect()
            try : 
                with connection.cursor() as mycursor:
                    sql = "INSERT INTO etudiant  VALUES (%s, %s, %s, %s)"
                    mycursor.executemany(sql, lis)
                    connection.commit()
                    print("l'opération à été bien effectué !")
            except Error as e:
                print(e)
        elif x==2 : 
            lis=[]
            nb = int(input("combien d'etudiant vous voullez supprimer : "))
            for i in range(nb) :
                cin=(input("Saisir le CIN : "),)
                print("---------------------------------------------------------------------------------------------")
                connection.reconnect()
                try : 
                    with connection.cursor() as mycursor:
                        sql = "delete from etudiant  where CIN_etu= %s "
                        mycursor.execute(sql, cin)
                        connection.commit()
                        print("l'opération à été bien effectué !")
                except Error as e:
                    print(e)
        elif x==3 : 
            lis=[]
            nb = int(input("combien d'assistant vous voullez inserer : "))
            for i in range(nb) :
                assis=(input("CIN: "), input("nom: "), input("prenom: "), input("numero de telephone: "), input("fonction :"))
                print("---------------------------------------------------------------------------------------------")
                lis.append(assis)
            connection.reconnect()
            try : 
                with connection.cursor() as mycursor:
                    sql = "INSERT INTO assistant  VALUES (%s, %s, %s, %s , %s)"
                    mycursor.executemany(sql, lis)
                    connection.commit()
                    print("l'opération à été bien effectué !")
            except Error as e:
                print(e)

        elif x==4 : 
            lis=[]
            nb = int(input("combien d'assistant vous voullez supprimer : "))
            for i in range(nb) :
                cin=(input("Saisir le CIN : "),)
                print("---------------------------------------------------------------------------------------------")
                connection.reconnect()
                try : 
                    with connection.cursor() as mycursor:
                        sql = "delete from assistant  where CIN_etu= %s "
                        mycursor.execute(sql, cin)
                        connection.commit()
                        print("l'opération à été bien effectué !")
                except Error as e:
                    print(e)
                    
        elif x==5 : 

            lis=[]
            nb = int(input("combien de local vous voullez inserer : "))
            for i in range(nb) :
                local=(input("id local: "), input("type local(salle ou terrain): "), input("id de specialité: "))
                print("---------------------------------------------------------------------------------------------")
                lis.append(local)
            connection.reconnect()
            try : 
                with connection.cursor() as mycursor:
                    sql = "INSERT INTO local  VALUES (%s, %s, %s )"
                    mycursor.executemany(sql, lis)
                    connection.commit()
                    print("l'opération à été bien effectué !")
            except Error as e:
                print(e)
        
        elif x==6 : 
            lis=[]
            nb = int(input("combien de locaux vous voullez supprimer : "))
            for i in range(nb) :
                id=(input("Saisir le id local : "),)
                print("---------------------------------------------------------------------------------------------")
                connection.reconnect()
                try : 
                    with connection.cursor() as mycursor:
                        sql = "delete from local  where CIN_etu= %s "
                        mycursor.execute(sql, id)
                        connection.commit()
                        print("l'opération à été bien effectué !")
                except Error as e:
                    print(e)
            
        elif x==7 : 
            lis=[]
            nb = int(input("combien de specialité vous voullez inserer : "))
            for i in range(nb) :
                spe=(input("id: "), input("libelle: "))
                print("---------------------------------------------------------------------------------------------")
                lis.append(spe)
            connection.reconnect()
            try : 
                with connection.cursor() as mycursor:
                    sql = "INSERT INTO specialite  VALUES (%s, %s)"
                    mycursor.executemany(sql, lis)
                    connection.commit()
                    print("l'opération à été bien effectué !")
            except Error as e:
                print(e)
                
        elif x==8 : 
            spe=(input("id local: "), input("date de debut(YYY-MM-JJ HH-MM-SS) "), input("date de fin: "), input("CIN d'etudiant: ") , input("CIN de l'assistant(optionnel): "))
            print("---------------------------------------------------------------------------------------------")
            connection.reconnect()
            try : 
                with connection.cursor() as mycursor:
                    sql = "INSERT INTO reservation(id_local , date_deb , date_fin , CIN_etu , CIN_as)  VALUES (%s, %s,%s, %s,%s)"
                    mycursor.execute(sql, lis)
                    connection.commit()
                    print("l'opération à été bien effectué !")
            except Error as e:
                print(e)
        
        elif x==9 :
            connection.reconnect()
            try :
                with connection.cursor() as mycursor:
                    sql = "SELECT * FROM etudiant "
                    mycursor.execute(sql)
                    results = mycursor.fetchall()
                    for ligne in results:
                        print(ligne)
            except Error as e:
                print(e)
        
        elif x==10 :
            connection.reconnect()
            try :
                with connection.cursor() as mycursor:
                    sql = "SELECT * FROM assistant "
                    mycursor.execute(sql)
                    results = mycursor.fetchall()
                    for ligne in results:
                        print(ligne)
            except Error as e:
                print(e)
        
        elif x==11 :
            connection.reconnect()
            try :
                with connection.cursor() as mycursor:
                    sql = "SELECT * FROM reservation "
                    mycursor.execute(sql)
                    results = mycursor.fetchall()
                    for ligne in results:
                        print(ligne)
            except Error as e:
                print(e)
        
        elif x==12 :
            connection.reconnect()
            try :
                cin=(input("entrer le cin de l'etudiant concerné: "),)
                with connection.cursor() as mycursor:
                    sql = "SELECT * FROM reservation where CIN_etu=%s"
                    mycursor.execute(sql,cin)
                    results = mycursor.fetchall()
                    if len(results)==0 :
                        print("aucune reservation ! ")
                    for ligne in results:
                        print(ligne)
            except Error as e:
                print(e)
            
        elif x==13 : 
            connection.reconnect()
            try :
                cin=(input("entrer le cin de l'assistant concerné: "),)
                with connection.cursor() as mycursor:
                    sql = "SELECT * FROM reservation where CIN_as=%s"
                    mycursor.execute(sql,cin)
                    results = mycursor.fetchall()
                    if len(results)==0 :
                        print("aucun reservation ! ")
                    for ligne in results:
                        print(ligne)
            except Error as e:
                print(e)
                
        elif x==0 : 
            print("à bientot ! ")
            break
            
            
        else :
            print("veuillez saisir un nombre existant !!!! ")

        os.system("cls")

    
        
                    
        
       
       
            
            
    