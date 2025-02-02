import 'dart:io';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_storage/firebase_storage.dart';
import 'package:firebase_storage/firebase_storage.dart';
import 'package:path/path.dart' as Path;

import '../Model/Note.dart';
class NoteRepository{

readNote(Note note) async
{final docNote = FirebaseFirestore.instance.collection('Note').doc(note?.uid);
final snapshot = await docNote.get();if(snapshot.exists){
return Note.fromJson(snapshot.data()!);
}}

Stream<List<Note>> readAllNote()=>FirebaseFirestore.instance.collection('Note').snapshots().map((snapshot) => snapshot.docs.map((doc) =>Note.fromJson(doc.data())).toList());


Future UpdateNote(Note note) async{


final docNote = FirebaseFirestore.instance.collection('Note').doc(note.uid);


 docNote.update({'note' : note.note,});

 print("Update");

}


deleteNote(Note Note) async {
final docNote = FirebaseFirestore.instance.collection('Note').doc(Note.uid);
 docNote.delete();
}


Future<String?> AjoutNote(Note Note) async{
final docNote = FirebaseFirestore.instance.collection('Note').doc();
String path = docNote.path.split('/')[1];
Note.uid = path;
final data = Note.toJson();
docNote.set(data);
return path;
}

}