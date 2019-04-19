from SPARQLWrapper import SPARQLWrapper, JSON,XML
import re,json

def get_properties(P_ID, filename):
	#sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
	cur_json = {}
	sparql = SPARQLWrapper("http://sitaware.isi.edu:8080/bigdata/namespace/wdq/sparql")
	#sparql.setTimeout(1000)
	sparql.setQuery("""
	    SELECT DISTINCT ?v ?x
		WHERE{
	      ?x wdt:""" + P_ID + """?v .
	      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
	    }
	""")
	sparql.setReturnFormat(JSON)
	try:
		results = sparql.query().convert()
		for result in results["results"]["bindings"]:
			id = result["v"]["value"]
			Q = re.search(r'Q[0-9]+',result["x"]["value"])
			if Q:
				cur_json[id] = Q.group(0)
	except:
		print(filename)
	return cur_json


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
	id_label = {}#get_properties("P212")
	prop_idents ={}
	get_identifiers()
	for id,label in id_label.items():
		prop_idents[id+"_"+label] = get_properties(id,id+"_"+label)
	js = json.dumps(prop_idents)
	f = open("prop_idents.json","w+")
	f.write(js)
	f.close()
