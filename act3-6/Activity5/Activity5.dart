import 'dart:io';

void main()
{

bool testing = true;

do 
{
  print("What do you want to do? ");
  print("1. Write a File ?");
  print("2. Read the file made ?");
  print("3. terminate ?");

  String choice = stdin.readLineSync() ?? '';


  switch(choice)
  {
    case '1':
      user();
      break;
    case '2':
      reader();
      break;
    default :
      testing = false;
      break;
  }
} while (testing);

  
}


void user()
{
  stdout.write("Write the file you want to make, include .txt extension \n");
  String fileName = stdin.readLineSync() ?? 'default.txt';

  //Create the File
  var file = File(fileName);

  file.createSync();

  if(file.existsSync())
  {
    print("File created ");

    //Write something to the file
    print("Enter what you want to write to the file");
    String letter = stdin.readLineSync() ?? '';

    var writeFile = file.openWrite();
    writeFile.write(letter);

    writeFile.close();

    print("Done writing");
    print("---------------------------");

  }else
  {
    print("file not created or it already exist");
  }

}

void reader()
{
   String currentDirectory = Directory.current.path;

  // List all files in the current directory
  Directory(currentDirectory)
      .listSync()
      .where((entity) => entity is File && entity.path.endsWith('.txt'))
      .forEach((file) => print(file.path.split(Platform.pathSeparator).last));

   print("Enter the file you want to read");
   String fileName = stdin.readLineSync() ?? '';

   File file = File(fileName);

   if(file.existsSync())
   {
    print("It exist");
    Future<List<String>> lines = file.readAsLines();

    lines.then((List<String> lines){
    lines.forEach((line) {
      print(line);
    });
    }).catchError((e) {
          print('Error reading file: $e');
       });

   }else{
    print("file doesnt exist");
    print("---------------------------");
   }

}