# Description

These scripts allow users to convert ligands with `.mol2` extension to `.pdbqt` files, which are the input files for AutoDock Vina.  
Scripts must be stored in the same directory as `.mol2` files because they use `getwd()` (in R) and `os.getcwd()` (in Python) functions.  
It is worth mentioning that users can freely edit strings to adjust scripts to convert various molecule files.  

---

# Dependencies  

1. Installed **OpenBabel**.  
2. Installed **glue()** package for R script:  

    ```r
    install.packages("glue")
    ```

---

# References  

1. **OpenBabel** - [OpenBabel Documentation](http://openbabel.org/docs/Installation/install.html)
