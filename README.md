#Description
These scripts allow user to convert ligands with .mol2 extension to .pdbqt files, which are the input files for AutoDock Vina. 
Scripts must be stored in the same directory as .mol2 files, beacuse they use getwd() (in R) and os.getcwd() (in Python) function. 
It is worth mentioning that user can freely edit string to adjust scripts to convert various molecule files.



#Dependecies:
1) Installed **OpenBabel**
2) Installed **glue()** packet for R script:
    ```r
       install.packages("glue")
    ```

#References:
1) **OpenBabel** - https://open-babel.readthedocs.io/en/latest/Command-line_tools/babel.html
