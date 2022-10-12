'''
VIDEO 3

'''

(base) MacBook-di-Federico:~ Federico$ pwd
/Users/air

(base) MacBook-di-Federico:~ Federico$ cd Downloads/

(base) MacBook-di-Federico:Downloads Federico$ ls
20220914_ASPECT_aa_rc1_Median_FM_v2.xlsx
Linux_Mac_Terminal_Tutorial.py
Mac_Linux_Terminal_Dict.py
Preferences.sublime-settings.py
TerminalTest
Versione Finale.mp4
data.csv
terminal2.py
untitled.hidden-color-scheme.py
~$S 2020 Abstract_Association of Genotype and Structural Lung Disease in a Cohort of Children with PCD_012820.docx

(base) MacBook-di-Federico:Downloads Federico$ ls -lah
#codice per mostrare il contenuto di una cartella con tutti i byte
total 513104
drwx------+ 14 Federico  staff   448B Oct  8 19:55 .
drwxr-xr-x+ 40 Federico  staff   1.3K Oct 12 21:37 ..
-rw-r--r--@  1 Federico  staff    10K Oct  8 19:23 .DS_Store
-rw-------   1 Federico  staff     0B Mar 14  2017 .localized
-rw-r--r--@  1 Federico  staff    32K Sep 14 22:45 20220914_ASPECT_aa_rc1_Median_FM_v2.xlsx
-rw-r--r--@  1 Federico  staff   3.5K Oct  5 20:34 Linux_Mac_Terminal_Tutorial.py
-rw-r--r--@  1 Federico  staff   1.6K Oct  8 19:55 Mac_Linux_Terminal_Dict.py
-rw-r--r--@  1 Federico  staff   4.0K Oct  8 19:00 Preferences.sublime-settings.py
drwxr-xr-x   4 Federico  staff   128B Oct  8 19:28 TerminalTest
-rw-r--r--@  1 Federico  staff   244M Nov 26  2021 Versione Finale.mp4
-rw-r--r--@  1 Federico  staff   3.8M Sep 30 16:26 data.csv
-rw-r--r--@  1 Federico  staff   4.2K Oct  8 19:46 terminal2.py
-rw-r--r--@  1 Federico  staff   1.9K Oct  8 19:02 untitled.hidden-color-scheme.py
-rw-r--r--@  1 Federico  staff   162B Jun  1  2020 ~$S 2020 Abstract_Association of Genotype and Structural Lung Disease in a Cohort of Children with PCD_012820.docx

(base) MacBook-di-Federico:Downloads Federico$ find . -type f
#codice per trovare tutti i file nella directory

./Preferences.sublime-settings.py
./~$S 2020 Abstract_Association of Genotype and Structural Lung Disease in a Cohort of Children with PCD_012820.docx
./Versione Finale.mp4
./.DS_Store
./TerminalTest/.DS_Store
./TerminalTest/OrigDir/moved_file.txt
./.localized
./terminal2.py
./untitled.hidden-color-scheme.py
./data.csv
./20220914_ASPECT_aa_rc1_Median_FM_v2.xlsx
./Linux_Mac_Terminal_Tutorial.py
./Mac_Linux_Terminal_Dict.py

(base) MacBook-di-Federico:Downloads Federico$ find . -type d
#codice per trovare tutte le directory nella directory
.
./TerminalTest
./TerminalTest/OrigDir
./TerminalTest/OrigDir/SubDir1

(base) MacBook-di-Federico:Downloads Federico$ find . -empty
#codice per trovare tutti le directory o i file vuoti
./TerminalTest/OrigDir/SubDir1
./.localized

(base) MacBook-di-Federico:Downloads Federico$ find . -perm
find: -perm: requires additional arguments

(base) MacBook-di-Federico:Downloads Federico$ find . -perm 777
#codice per trovare le i file con permission 777
#le directory devono essere 775 ed i file 664


(base) MacBook-di-Federico:Downloads Federico$ find . -type f -iname 'term*'
#codice per trovare i file con nome contenente 'ter'
./terminal2.py

(base) MacBook-di-Federico:Downloads Federico$ find . -type f -iname '*.py'
#codice per trovare i file con nome contenente '.py' quindi le estenzioni
./Preferences.sublime-settings.py
./terminal2.py
./untitled.hidden-color-scheme.py
./Linux_Mac_Terminal_Tutorial.py
./Mac_Linux_Terminal_Dict.py

(base) MacBook-di-Federico:Downloads Federico$ open -t find . -type f -name 'terminal2.py'
open: invalid option -- y
Usage: open [-e] [-t] [-f] [-W] [-R] [-n] [-g] [-h] [-s <partial SDK name>][-b <bundle identifier>] [-a <application>] [filenames] [--args arguments]
Help: Open opens files from a shell.
      By default, opens each file using the default application for that file.  
      If the file is in the form of a URL, the file will be opened as a URL.
Options: 
      -a                Opens with the specified application.
      -b                Opens with the specified application bundle identifier.
      -e                Opens with TextEdit.
      -t                Opens with default text editor.
      -f                Reads input from standard input and opens with TextEdit.
      -F  --fresh       Launches the app fresh, that is, without restoring windows. Saved persistent state is lost, excluding Untitled documents.
      -R, --reveal      Selects in the Finder instead of opening.
      -W, --wait-apps   Blocks until the used applications are closed (even if they were already running).
          --args        All remaining arguments are passed in argv to the application's main() function instead of opened.
      -n, --new         Open a new instance of the application even if one is already running.
      -j, --hide        Launches the app hidden.
      -g, --background  Does not bring the application to the foreground.
      -h, --header      Searches header file locations for headers matching the given filenames, and opens them.
      -s                For -h, the SDK to use; if supplied, only SDKs whose names contain the argument value are searched.
                        Otherwise the highest versioned SDK in each platform is used.

(base) MacBook-di-Federico:Downloads Federico$ cd ..

(base) MacBook-di-Federico:~ Federico$ open -a 'Sublime Text' ~/Downloads/terminal2.py
(base) MacBook-di-Federico:~ Federico$ open -a 'VLC' ~/Desktop/MARINO.mov
#codice per aprire con una app specifica uno specifico file presente in una specifica directory


(base) MacBook-di-Federico:~ Federico$ touch 'file.txt'

(base) MacBook-di-Federico:~ Federico$ ls
Applications	Documents	Dropbox		Movies		Pictures	file.txt
Desktop		Downloads	Library		Music		Public

(base) MacBook-di-Federico:~ Federico$ rm file.txt

(base) MacBook-di-Federico:~ Federico$ ls
Applications	Desktop		Documents	Downloads	Dropbox		Library		Movies		Music		Pictures	Public

(base) MacBook-di-Federico:~ Federico$ cd Downloads/

(base) MacBook-di-Federico:Downloads Federico$ touch file.txt

(base) MacBook-di-Federico:Downloads Federico$ ls
20220914_ASPECT_aa_rc1_Median_FM_v2.xlsx
Linux_Mac_Terminal_Tutorial.py
Mac_Linux_Terminal_Dict.py
Preferences.sublime-settings.py
TerminalTest
Versione Finale.mp4
data.csv
file.txt
terminal2.py
untitled.hidden-color-scheme.py
~$S 2020 Abstract_Association of Genotype and Structural Lung Disease in a Cohort of Children with PCD_012820.docx

(base) MacBook-di-Federico:Downloads Federico$ open -t file.txt

(base) MacBook-di-Federico:Downloads Federico$ open -t file.txt

(base) MacBook-di-Federico:Downloads Federico$ find . -type f -name '*py'
./Preferences.sublime-settings.py
./terminal2.py
./untitled.hidden-color-scheme.py
./Linux_Mac_Terminal_Tutorial.py
./Mac_Linux_Terminal_Dict.py

(base) MacBook-di-Federico:Downloads Federico$ find . -type d
.
./TerminalTest
./TerminalTest/OrigDir
./TerminalTest/OrigDir/SubDir1

(base) MacBook-di-Federico:Downloads Federico$ find . -type d -maxdepth 1
#codice per trovare tutte le directory di primo grado presenti nella mia directory
.
./TerminalTest

(base) MacBook-di-Federico:Downloads Federico$ cd ..

(base) MacBook-di-Federico:~ Federico$ ls
Applications	Desktop		Documents	Downloads	Dropbox		Library		Movies		Music		Pictures	Public

(base) MacBook-di-Federico:~ Federico$ open -t ~/Downloads/file.txt

(base) MacBook-di-Federico:~ Federico$ 