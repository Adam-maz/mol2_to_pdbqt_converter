library(glue)
path = getwd()

for (element in dir(path)){
  if (grepl('.mol2', element)){
    full_element_path = file.path(path, element)
    converted_name = sub("mol2", "pdbqt", element)
    full_converted_name = file.path(path, converted_name)
    
    expression = glue('obabel "{full_element_path}" -O "{full_converted_name}"')
    system(expression)}
  else{
  }
}





