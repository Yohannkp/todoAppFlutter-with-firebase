import 'package:firebase_storage/firebase_storage.dart';
import 'package:flutter/material.dart';
import 'package:todoapp/Repository/NoteRepository.dart';

import 'Model/Note.dart';
class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {


  //Service Firestore
  final NoteRepository noteRepository = NoteRepository();
  //text Controller
  final TextEditingController notecontroller = TextEditingController();
  
  
  
  void openbox(Note? docid){
    docid != null ? notecontroller.text = docid!.note : null;
    showDialog(context: context, builder: (context)=>
        AlertDialog(
          content: TextField(
            controller: notecontroller,
            
          ),
          actions: [
            TextButton(onPressed: (){
              //On ajoute la note a la base de données
              Note note = Note(uid: "", note: notecontroller.text);
              docid?.note = notecontroller.text;
              docid == null ? noteRepository.AjoutNote(note) : noteRepository.UpdateNote(docid);

              //On decharge le text controller
              notecontroller.clear();

              //On ferme le pop up
              Navigator.pop(context);
            }, child: docid == null ? Text("Ajouter") : Text("Mise a jour")),

          ],
          
        ));
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("NOTES",style: TextStyle(color: Colors.white,fontWeight: FontWeight.bold,fontSize: 30),),
        centerTitle: true,
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,),
      
      body: StreamBuilder(stream: noteRepository.readAllNote(), builder: (context,snapshot){
        if(!snapshot.hasData){
          return Text("Vide");
        }
        return ListView.builder(
            itemCount: snapshot.data?.length,
            itemBuilder: (context,index){
          return Padding(
            padding: const EdgeInsets.all(12.0),
            child: Card(
              child: ListTile(
                title: Text("${snapshot.data?[index].note}",style: TextStyle(fontSize: 20),),
                trailing: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    IconButton(onPressed: (){
                      openbox(snapshot.data?[index]);
                    }, icon: Icon(Icons.edit),color: Colors.green,),

                    IconButton(onPressed: (){
                      noteRepository.deleteNote(snapshot.data![index]);
                    }, icon: Icon(Icons.delete),color: Colors.red,),
                  ],
                ),
              ),
            ),
          );
        });
      }),
      floatingActionButton: FloatingActionButton(onPressed: (){
        openbox(null);
      },child: Text("+"),),
    );
  }
}
