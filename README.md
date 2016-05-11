# Loktara_Interview

Problem : Python URI

Used regular expression to get scheme, netlocalation,path, query, fragment string value.
First regex object is responsible for getting all scheme, netlocalation,path, query, fragment string from URL
Second regex object used to retrieve domain name from netlocation string.

In this program,
1. Netloc is requiered so input mus be prefixed by [scheme:]//. for example http://abc.def.co.au/, //abc.def.co.au
2. scheme, path,query,fragment is optional.
3. 
