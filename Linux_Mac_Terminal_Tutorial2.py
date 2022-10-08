'''

LINUX / MAC TERMINAL LESSON COREY SCHAFER

VIDEO 1 
Linux/Mac Terminal Tutorial: How To Use The find Command

'''

(base) MacBook-di-Federico:~ Federico$ pwd
/Users/air

(base) MacBook-di-Federico:~ Federico$ cd Downloads/

(base) MacBook-di-Federico:Downloads Federico$ ls
20220914_ASPECT_aa_rc1_Median_FM_v2.xlsx
Linux_Mac_Terminal_Tutorial.py
Preferences.sublime-settings.py
TerminalTest
Versione Finale.mp4
data.csv
untitled.hidden-color-scheme.py
~$S 2020 Abstract_Association of Genotype and Structural Lung Disease in a Cohort of Children with PCD_012820.docx

(base) MacBook-di-Federico:Downloads Federico$ cd TerminalTest

(base) MacBook-di-Federico:TerminalTest Federico$ mkdir TestDir
#codice per creare una directory  dal terminale 

(base) MacBook-di-Federico:TerminalTest Federico$ ls
TestDir

(base) MacBook-di-Federico:TerminalTest Federico$ cd TestDir/

(base) MacBook-di-Federico:TestDir Federico$ touch test_file.txt
#codice per creare un file dal terminale

(base) MacBook-di-Federico:TestDir Federico$ ls
test_file.txt

(base) MacBook-di-Federico:TestDir Federico$ open test_file.txt
#codice per aprire un file dal terminale con il software predefinito

(base) MacBook-di-Federico:TestDir Federico$ cp test_file.txt copy_file.txt
#codice per copiare un file dal terminale

(base) MacBook-di-Federico:TestDir Federico$ ls
copy_file.txt	test_file.txt

(base) MacBook-di-Federico:TestDir Federico$ mv test_file.txt orig_file.txt
#codice per spostare o rinominare file o directory 

(base) MacBook-di-Federico:TestDir Federico$ ls
copy_file.txt	orig_file.txt

(base) MacBook-di-Federico:TestDir Federico$ mkdir SubDir1

(base) MacBook-di-Federico:TestDir Federico$ mv orig_file.txt SubDir1/

(base) MacBook-di-Federico:TestDir Federico$ ls
SubDir1		copy_file.txt

(base) MacBook-di-Federico:TestDir Federico$ ls SubDir1/
orig_file.txt

(base) MacBook-di-Federico:TestDir Federico$ ls
SubDir1		copy_file.txt

(base) MacBook-di-Federico:TestDir Federico$ cd SubDir1

(base) MacBook-di-Federico:SubDir1 Federico$ ls
orig_file.txt

(base) MacBook-di-Federico:SubDir1 Federico$ mv orig_file.txt ../moved_file.txt

(base) MacBook-di-Federico:TerminalTest Federico$ cd TestDir

(base) MacBook-di-Federico:TestDir Federico$ ls
SubDir1		copy_file.txt	moved_file.txt

(base) MacBook-di-Federico:TestDir Federico$ rm copy_file.txt
#codice per eliminare un file dal terminale

(base) MacBook-di-Federico:TestDir Federico$ ls
SubDir1		moved_file.txt

(base) MacBook-di-Federico:TestDir Federico$ cd ..

(base) MacBook-di-Federico:TerminalTest Federico$ ls
TestDir

(base) MacBook-di-Federico:TerminalTest Federico$ man cp
#codice per leggere la documentazione di un comando dal terminale 

(base) MacBook-di-Federico:TerminalTest Federico$ cp -R TestDir/ CopyDir/
#codice per copiare una directory dal terminale

(base) MacBook-di-Federico:TerminalTest Federico$ ls
CopyDir	TestDir

(base) MacBook-di-Federico:TerminalTest Federico$ ls CopyDir/
SubDir1		moved_file.txt

(base) MacBook-di-Federico:TerminalTest Federico$ ls
CopyDir	TestDir

(base) MacBook-di-Federico:TerminalTest Federico$ mv TestDir OrigDir

(base) MacBook-di-Federico:TerminalTest Federico$ ls
CopyDir	OrigDir

(base) MacBook-di-Federico:TerminalTest Federico$ mv CopyDir/ OrigDir/

(base) MacBook-di-Federico:TerminalTest Federico$ ls
OrigDir

(base) MacBook-di-Federico:TerminalTest Federico$ ls OrigDir/
CopyDir		SubDir1		moved_file.txt

(base) MacBook-di-Federico:TerminalTest Federico$ ls
OrigDir

(base) MacBook-di-Federico:TerminalTest Federico$ cd OrigDir/

(base) MacBook-di-Federico:OrigDir Federico$ ls
CopyDir		SubDir1		moved_file.txt

(base) MacBook-di-Federico:OrigDir Federico$ mv CopyDir/ ../Copy_test

(base) MacBook-di-Federico:OrigDir Federico$ ls
SubDir1		moved_file.txt

(base) MacBook-di-Federico:OrigDir Federico$ cd ..

(base) MacBook-di-Federico:TerminalTest Federico$ ls
Copy_test	OrigDir

(base) MacBook-di-Federico:TerminalTest Federico$ rm -R Copy_test/
#codice per rimuovere na directory dal terminale

(base) MacBook-di-Federico:TerminalTest Federico$ ls
OrigDir

(base) MacBook-di-Federico:TerminalTest Federico$ 
