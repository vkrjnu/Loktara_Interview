# Loktara_Interview

Problem : Python URI

Regular expression is used to get scheme, netlocalation,path, query, fragment value from URL. 

In this program, 
First regular expression object used to get all scheme, authority,path, query, fragment string from URL and 
Second regular expression object used to retrieve domain name from netlocation string.

1. Authority is requiered so input must be prefixed by [scheme:]//. for example http://abc.def.co.au/, //abc.def.co.au
2. scheme, path,query,fragment is optional.
