import 'package:cloud_firestore/cloud_firestore.dart';
class Note {
 String uid;
 String note;
Note({required this.uid,required this.note,});

Map<String, dynamic> toJson(){
return{
'uid' : uid ,
'note' : note ,
};}
static Note fromJson(Map<String,dynamic> json) => Note(uid: json['uid'],note: json['note'],);

}