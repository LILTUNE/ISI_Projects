# ISI_Projects
Author: Tong Liu
USC Information Sciences Institute
Supervisor: Pedro Szekely

## sparql.py
generate all identifiers for all property, then store each property's identifers in txt files.
File name follow the format 'PropertyID_PropertyName.txt'

## minHash.py
Build a list for all MinHash objects. Give a file, it will return the top 5 silimiar items and their similarity scores.

## error.log
Contain all files generate manully. Some files are empty, we didn't store it in final result.

## results_3.0.zip
Contain all 'PropertyID_PropertyName.txt' files, each files contains all identifiers for some property.
Small files(contain less that 15 identifiers) are filters, they are not included here.

## test.txt
Test file for minHash.py. Generated form ‘P5942_Protected objects Ostbelgien ID.txt’. If run minHash.py, it will return
similarity : 0.65625 name: P5942_Protected objects Ostbelgien ID.txt
similarity : 0.046875 name: P860_e-archiv.li ID.txt
similarity : 0.046875 name: P4879_World Rugby Women's Sevens Series player ID.txt
similarity : 0.03125 name: P557_DiseasesDB.txt
similarity : 0.03125 name: P4696_CIQUAL2017 ID.txt
