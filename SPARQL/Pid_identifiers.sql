SELECT DISTINCT ?v
WHERE
{
  ?x wdt:P212 ?v .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}

SELECT DISTINCT ?P_ID ?P_IDLabel
WHERE
{
  ?P_ID wdt:P31/wdt:P279* wd:Q19847637 .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
ORDER BY DESC(?P_ID)

//select Qnodes and Identifiers for some property(P288)
SELECT ?x ?v WHERE { ?x wdt:P232 ?v. }

//select all properties.
select ?p where {
		?p wikibase:propertyType wikibase:ExternalId .
		}
    //official endpoint
sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    //siteware endpoint
sparql = SPARQLWrapper("http://sitaware.isi.edu:8080/bigdata/namespace/wdq/sparql")
