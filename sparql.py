from SPARQLWrapper import SPARQLWrapper, JSON,XML

def get_properties(P_ID):
	sparql = SPARQLWrapper("https://query.wikidata.org/bigdata/namespace/wdq/sparql")
	sparql.setQuery("""
	    SELECT DISTINCT ?v
		WHERE{
	      ?x wdt:""" + P_ID + """?v .
	      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
	    }
	    LIMIT 10
	""")
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	res = results["results"]["bindings"]
	#results["results"]["bindings"][0]["v"]["value"]
	for r in res:
		print(r["v"]["value"])

def write_file():
	continue
	##todo

def get_identifiers():
	sparql = SPARQLWrapper("https://query.wikidata.org/bigdata/namespace/wdq/sparql")
	sparql.setQuery("""
		SELECT DISTINCT ?P_ID ?P_IDLabel
		WHERE
		{
		  ?P_ID wdt:P31/wdt:P279* wd:Q19847637 .
		  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
		}
		ORDER BY DESC(?P_ID)
	""")
if __name__ == "__main__":
	#get_properties("P212")