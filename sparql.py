from SPARQLWrapper import SPARQLWrapper, JSON,XML
import re,json

def get_properties(P_ID):
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
		print(P_ID)
	return cur_json


def get_identifiers():
	global P_nodes
	#sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
	sparql = SPARQLWrapper("http://sitaware.isi.edu:8080/bigdata/namespace/wdq/sparql")
	#sparql.setTimeout(1000)
	sparql.setQuery("""select ?p where {
		?p wikibase:propertyType wikibase:ExternalId .
		}""")
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	res = results["results"]["bindings"]
	for r in res:
		try:
			P_node = re.search(r'[A-Za-z][0-9]+',r["p"]["value"]).group()
			P_nodes.append(P_node)
			# label = r["P_IDLabel"]["value"]
			# id_label[id]=label
		except:
			continue
if __name__ == "__main__":
	id_label = {}#get_properties("P212")
	P_nodes = []
	prop_idents ={}
	get_identifiers()
	for idx,P_node in enumerate(P_nodes):
		print(idx,P_node)
		prop_idents[P_node] = get_properties(P_node)
	js = json.dumps(prop_idents)
	f = open("prop_idents_v2.json","w+")
	f.write(js)
	f.close()
