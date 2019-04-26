from SPARQLWrapper import SPARQLWrapper, JSON,XML
import re,json

def get_properties(P_ID):
	sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
	cur_json = {}
	#sparql = SPARQLWrapper("http://sitaware.isi.edu:8080/bigdata/namespace/wdq/sparql")
	#sparql.setTimeout(1000)
	sparql.setQuery("""
	    SELECT ?x ?v WHERE { ?x wdt:""" + P_ID + """ ?v. }
	""")
	sparql.setReturnFormat(JSON)
	try:
		results = sparql.query().convert()
		for result in results["results"]["bindings"]:
			value = result["v"]["value"]
			Q = re.search(r'Q[0-9]+',result["x"]["value"])
			if Q:
				Q_node = Q.group(0)
				cur_json[value] = Q_node
				if(value[0]=="0" and value.isdigit()):
					rm_leading0 = str(int(value))
					cur_json[rm_leading0] = Q_node
	except:
		print('get_properties() Error:',P_ID)
	return cur_json

def get_identifiers():
	global P_nodes
	sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
	#sparql = SPARQLWrapper("http://sitaware.isi.edu:8080/bigdata/namespace/wdq/sparql")
	#sparql.setTimeout(1000)
	sparql.setQuery("""select ?p where {
		?p wikibase:propertyType wikibase:ExternalId .
		}
		""")
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	res = results["results"]["bindings"]
	for r in res:
		try:
			P_node = re.search(r'[A-Za-z][0-9]+',r["p"]["value"]).group()
			P_nodes.append(P_node)
		except:
			print('get_identifiers Error()', r)
if __name__ == "__main__":
	P_nodes = []
	prop_idents ={}
	get_identifiers()
	for idx,P_node in enumerate(P_nodes):
		print(idx,P_node)
		prop_idents[P_node] = get_properties(P_node)
	js = json.dumps(prop_idents)
	f = open("prop_idents_v4.json","w+")
	f.write(js)
	f.close()
