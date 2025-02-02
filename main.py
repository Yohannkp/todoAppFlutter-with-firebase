#Creation de classes
import os;

def Menu():
     print("Menu\n1-Authentification\n2-CRUD")


Menu()
choix = input("Que voulez vous faire : ")

if choix == "1":
        #Model D'authentification
    with open("Model/user.dart","w") as u:
        u.write("class AppUser")
        u.write("{\n")
        u.write("\n")
        u.write("String uid;\n\n")
        u.write("AppUser(")
        u.write("{\n")
        u.write("required this.uid")
        u.write("\n")
        u.write("});")
        u.write("\n")
        u.write("}")

    with open("Repository/Authentification.dart","w") as h :
        h.write("import 'package:cloud_firestore/cloud_firestore.dart';\nimport 'package:firebase_auth/firebase_auth.dart';\nimport 'package:flutter/material.dart';\nimport 'package:locationdemaison/Model/Personne.dart';\nimport 'package:locationdemaison/Model/Post.dart';\nimport 'package:locationdemaison/Model/user.dart';\n")
        h.write("\n\n")
        h.write("Class AuthentificationService")
        h.write("{\n")
        h.write("final FirebaseAuth _auth = FirebaseAuth.instance;\n\n")
        h.write("AppUser? _userFromFireBaseUser(User? user)")
        h.write("{\n")
        h.write("return user != null ? AppUser(uid: user.uid) : null;")
        h.write("")
        h.write("\n}\n\n")
        h.write("Stream<AppUser?> get user{\n\nreturn _auth.authStateChanges().map(_userFromFireBaseUser);\n\n}\n\n")
        h.write("Future signInWithEmailAndPassword(String email,String password) async{\ntry{\n\t_auth.authStateChanges().listen((User? user) {\n\tif (user == null) {\n\tprint('User is currently signed out!');\n\t}else {\n\tprint('User is signed in!');\n}\n});\n\n")
        h.write("UserCredential result =await _auth.signInWithEmailAndPassword(email: email, password: password);")
        h.write("User? user = result.user;\nreturn _userFromFireBaseUser(user);\n\n}")
        h.write("catch(exeption){")
        h.write("print(exeption.toString());\n}\n}\n\n")
        h.write("Future registerInWithEmailAndPassword(String email,String password) async{\ntry{\n\tprint('Inscription')\n;_auth.authStateChanges().listen((User? user) \n{\nif (user == null) {\nprint('User is currently signed out!');\n} else \n{\nprint('User is signed in!');\n}\n});\n\n")
        h.write("UserCredential result =await _auth.createUserWithEmailAndPassword(email: email, password: password);\nUser? user = result.user;\nreturn _userFromFireBaseUser(user);\n}\ncatch(exeption){\nprint(exeption.toString());\n}\n\n}\n\n")
        h.write("Future signOut() async{\ntry{\n\treturn await _auth.signOut():\n}catch(exeption){\nprint(exeption.toString());\nreturn null;\n}\n}")
        
        
        
        
        
        
        
        h.write("\n}")
        

if choix == "2":
    try:
            os.mkdir("Model")
            os.mkdir("Repository")
    except:
            print("Dossier déjà existant")

    print("Entrer le nom de votre classe")
    nom_classe = input()
    print("Combien d'attributs avez vous ?")
    nombre_attributs = int(input())
    attributs = ["uid"]
    for i in range(0,nombre_attributs):
        print("Entrer l'attribut : ",nombre_attributs)
        attribut = input("")
        attributs.append(attribut)
    print(attributs[0])
    with open('Model/{}.dart'.format(nom_classe), 'w') as f:
        f.write("import 'package:cloud_firestore/cloud_firestore.dart';\nclass {} {}".format(nom_classe,"{\n"))
    with open('Model/{}.dart'.format(nom_classe),'a') as g:
                for i in range(0,len(attributs)):
                    g.write(" String ")
                    g.write(attributs[i])
                    g.write(";\n")
                g.write("{}({}".format(nom_classe,"{"))
                for i in range(0,len(attributs)): 
                    g.write("required this.")
                    g.write(attributs[i])
                    g.write(",")
                g.write("});")
                g.write("\n\n")
                g.write("Map<String, dynamic> toJson(){\nreturn{\n")
                for i in range(0,len(attributs)):
                    g.write("'{}' : {} ,\n".format(attributs[i],attributs[i]))
                g.write("};")

                g.write("}")
                g.write("\n")
                g.write("static {} fromJson(Map<String,dynamic> json) => {}(".format(nom_classe,nom_classe))
                for i in range(0,len(attributs)):
                    g.write("{}: json['{}'],".format(attributs[i],attributs[i]))
                g.write(");")
                g.write("\n\n")
                g.write("}")

    #Creer le repository

    nomRpository = "{}Repository".format(nom_classe)
    nomFichier = "Repository/{}Repository.dart".format(nom_classe)
    with open("{}".format(nomFichier),'w') as r:
        r.write("import 'dart:io';\nimport 'package:cloud_firestore/cloud_firestore.dart';\nimport 'package:firebase_auth/firebase_auth.dart';\nimport 'package:firebase_storage/firebase_storage.dart';\nimport 'package:firebase_storage/firebase_storage.dart';\nimport 'package:path/path.dart' as Path;\nclass {}".format(nomRpository))
        r.write("{")
        r.write("\n\n")
        r.write("read{}({} {}) async\n".format(nom_classe,nom_classe,nom_classe.lower()))
        r.write("{")
        r.write("final doc{} = FirebaseFirestore.instance.collection('{}').doc({}?.uid);\n".format(nom_classe,nom_classe,nom_classe.lower()))
        r.write("final snapshot = await doc{}.get();".format(nom_classe))
        r.write("if(snapshot.exists){\n")
        r.write("return {}.fromJson(snapshot.data()!);\n".format(nom_classe))
        r.write("}")
        r.write("}")
        r.write("\n") 
        r.write("\nStream<List<{}>> readAll{}()=>FirebaseFirestore.instance.collection('{}').snapshots().map((snapshot) => snapshot.docs.map((doc) =>{}.fromJson(doc.data())).toList());\n".format(nom_classe,nom_classe,nom_classe,nom_classe))
        r.write("\n\n")
        r.write("Future Update{}({} {}) async".format(nom_classe,nom_classe,nom_classe))
        r.write("{\n")
        r.write("\n\n")
        r.write("final doc{} = FirebaseFirestore.instance.collection('{}').doc({}.uid);".format(nom_classe,nom_classe,nom_classe))
        r.write("\n\n")
        r.write("\n doc{}.update(".format(nom_classe))
        r.write("{")
        for i in range(1,nombre_attributs+1):
            r.write("'{}' : {}.{},".format(attributs[i],nom_classe,attributs[i]))
        r.write("}")
        r.write(");")
        r.write("\n\n")
        r.write("}")
        r.write("\n\n\n")

        r.write("delete{}({} {}) async ".format(nom_classe,nom_classe,nom_classe))
        r.write("{")
        r.write("\nfinal doc{} = FirebaseFirestore.instance.collection('{}').doc({}.uid);".format(nom_classe,nom_classe,nom_classe))
        r.write("\n doc{}.delete();".format(nom_classe))
        r.write("\n}")

        r.write("\n\n\n")

        r.write("Future<String?> Ajout{}({} {}) async".format(nom_classe,nom_classe,nom_classe))
        r.write("{\n")
        r.write("final doc{} = FirebaseFirestore.instance.collection('{}').doc();\n".format(nom_classe,nom_classe))
        r.write("String path = doc{}.path.split('/')[1];\n".format(nom_classe))
        r.write("{}.uid = path;\n".format(nom_classe))
        r.write("final data = {}.toJson();\n".format(nom_classe))
        r.write("doc{}.set(data);\nreturn path;".format(nom_classe))
        r.write("\n}\n\n")
        r.write("}")

     


#Creation de la partie Authentification

"""

"""
