'''

LINUX / MAC TERMINAL LESSON COREY SCHAFER

VIDEO 1 
Linux/Mac Terminal Tutorial: Navigating your Filesystem

'''

(base) MacBook-di-Federico:~ Federico$ pwd
#codice per mostrare la folder in cui ci si trova
#result:
#/Users/air

(base) MacBook-di-Federico:~ Federico$ ls
#codice per mostrare il contenuto della cartella in cui ci si trova

Applications	Desktop		Documents	Downloads	
Dropbox		Library		Movies		Music		Pictures	Public

(base) MacBook-di-Federico:~ Federico$ cd Downloads
#codice per navigare in una cartella della mia directory

(base) MacBook-di-Federico:Downloads Federico$ ls
20220914_ASPECT_aa_rc1_Median_FM_v2.xlsx
Sublime Text.app
Versione Finale.mp4
data.csv
~$S 2020 Abstract_Association of Genotype and Structural Lung Disease in a Cohort of Children with PCD_012820.docx

(base) MacBook-di-Federico:Downloads Federico$ ls -a
#codice per mostrare anche i file nascosti della mia cartella
.
..
.DS_Store
.localized
20220914_ASPECT_aa_rc1_Median_FM_v2.xlsx
Sublime Text.app
Versione Finale.mp4
data.csv
~$S 2020 Abstract_Association of Genotype and Structural Lung Disease in a Cohort of Children with PCD_012820.docx

(base) MacBook-di-Federico:Downloads Federico$ ls -l
#codice per mostrare tutte le informazioni dei file nella mia cartella

total 513032
-rw-r--r--@ 1 Federico  staff      32890 Sep 14 22:45 20220914_ASPECT_aa_rc1_Median_FM_v2.xlsx
drwxrwxr-x@ 3 Federico  staff         96 Dec 21  2021 Sublime Text.app
-rw-r--r--@ 1 Federico  staff  255966560 Nov 26  2021 Versione Finale.mp4
-rw-r--r--@ 1 Federico  staff    4001520 Sep 30 16:26 data.csv
-rw-r--r--@ 1 Federico  staff        162 Jun  1  2020 ~$S 2020 Abstract_Association of Genotype and Structural Lung Disease in a Cohort of Children with PCD_012820.docx

(base) MacBook-di-Federico:Downloads Federico$ ls -la
#codice per mostrare tutte le informazioni anche dei file nascosti nella cartella

total 513048
drwx------+  9 Federico  staff        288 Sep 30 16:26 .
drwxr-xr-x+ 39 Federico  staff       1248 Sep 30 16:54 ..
-rw-r--r--@  1 Federico  staff       6148 Sep 30 15:45 .DS_Store
-rw-------   1 Federico  staff          0 Mar 14  2017 .localized
-rw-r--r--@  1 Federico  staff      32890 Sep 14 22:45 20220914_ASPECT_aa_rc1_Median_FM_v2.xlsx
drwxrwxr-x@  3 Federico  staff         96 Dec 21  2021 Sublime Text.app
-rw-r--r--@  1 Federico  staff  255966560 Nov 26  2021 Versione Finale.mp4
-rw-r--r--@  1 Federico  staff    4001520 Sep 30 16:26 data.csv
-rw-r--r--@  1 Federico  staff        162 Jun  1  2020 ~$S 2020 Abstract_Association of Genotype and Structural Lung Disease in a Cohort of Children with PCD_012820.docx

(base) MacBook-di-Federico:Downloads Federico$ pwd

/Users/air/Downloads

(base) MacBook-di-Federico:Downloads Federico$ cd ..
#codice per tornare una directory indietro

(base) MacBook-di-Federico:~ Federico$ pwd
/Users/air

(base) MacBook-di-Federico:~ Federico$ ls Downloads/
#codice per mostrare direttamente il contenuto di una specifica directory

20220914_ASPECT_aa_rc1_Median_FM_v2.xlsx
Sublime Text.app
Versione Finale.mp4
data.csv
~$S 2020 Abstract_Association of Genotype and Structural Lung Disease in a Cohort of Children with PCD_012820.docx

(base) MacBook-di-Federico:~ Federico$ pwd
/Users/air

(base) MacBook-di-Federico:~ Federico$ cd Downloads/
#codice per navigare direttamente in una specifica directory

(base) MacBook-di-Federico:Downloads Federico$ pwd
/Users/air/Downloads

(base) MacBook-di-Federico:Downloads Federico$ cd ../..
#codice pe tornare due directory indietro rispetto a dove mi trovo

(base) MacBook-di-Federico:Users Federico$ pwd
/Users
