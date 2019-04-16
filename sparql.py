from SPARQLWrapper import SPARQLWrapper, JSON,XML
import re
from collections import defaultdict

def get_properties(P_ID, filename):
	#sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
	sparql = SPARQLWrapper("http://sitaware.isi.edu:8080/bigdata/namespace/wdq/sparql")
	#sparql.setTimeout(1000)
	sparql.setQuery("""
	    SELECT DISTINCT ?v ?x
		WHERE{
	      ?x wdt:""" + P_ID + """?v .
	      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
	    }
	    limit 20
	""")
	sparql.setReturnFormat(JSON)
	try:
		results = sparql.query().convert()
		res = results["results"]["bindings"]
		f = open("./results_4.0/"+filename,"w+")
		for r in res:
			f.write((r["v"]["value"]+r["x"]["value"]))
			f.write("\n")
		f.close()
	except:
		print(filename)


def get_identifiers():
	global id_label
	#sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
	sparql = SPARQLWrapper("http://sitaware.isi.edu:8080/bigdata/namespace/wdq/sparql")
	#sparql.setTimeout(1000)
	sparql.setQuery("""
		SELECT DISTINCT ?P_ID ?P_IDLabel
		WHERE
		{
		  ?P_ID wdt:P31/wdt:P279* wd:Q19847637 .
		  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
		}
		ORDER BY DESC(?P_ID)
		limit 20
	""")
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	res = results["results"]["bindings"]
	for r in res:
		try:
			id = re.search(r'[A-Za-z][0-9]+',r["P_ID"]["value"]).group()
			label = r["P_IDLabel"]["value"]
			id_label[id]=label
		except:
			continue	
if __name__ == "__main__":
	id_label = defaultdict()#get_properties("P212")
	get_identifiers()
	for id,label in id_label.items():
		get_properties(id,id+"_"+label+".txt")
