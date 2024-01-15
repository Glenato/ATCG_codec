# ATCG_codec
Transforms binary and strings into quaternary (ATCG) or the other way around
When transformed to quaternary, a special syntaxe is used : 

The formatted sentence of "This is a secret message" becomes "This IS#a&secrEt§meSsAgE".

Also to make sure we know where the message starts and stops, I encapsulated the message between "START" and "STOP". Therefore the previous sentence "This is a secret message" actually becomes "STARTThis IS#a&secrEt§meSsAgESTOP".

This is a chart showing how quaternary is codded in binary :

| DNA  | Binary |
| ------------- | ------------- |
| A  | 00  |
| C  | 01  |
| G  | 10  |
| T  | 11  |


This project was inspired and uses some code from : https://github.com/Amagash/dna_encoding
