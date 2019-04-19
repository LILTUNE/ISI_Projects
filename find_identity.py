from collections import Counter
import json, requests
class find_identity():
	def __init__(self):
		pass

	## input: strings, output dictionary of string and Qnode in wikidate
	#@classmethod
	def get_identtifier(self,strings):
		id_nodes_dict = self.call_redis(strings)
		keys = set(id_nodes_dict.keys())
		output = {} #key string, value:Q123
		print(len(keys))
		P_list = []
		for s in strings:
			if s in keys:
				P_list.extend([P_Q.split('/')[0] for P_Q in id_nodes_dict[s]])
		P_predict = Counter(P_list).most_common(1)[0][0] #[('P932', 8), ('P1566', 6), ('P698', 2)]
		for s in strings:
			if s in keys:
				for P_Q in id_nodes_dict[s]: #for P_Q in P_Qlist
					P_Q_splited = P_Q.split('/')
					if P_Q_splited[0] == P_predict:
						output[s] = P_Q_splited[1]
			else:
				output[s] = 'N/A'
		return output
	#@classmethod	
	def get_identifier_3(self,strings):
		id_nodes_dict = self.call_redis(strings)
		keys = set(id_nodes_dict.keys())
		result = []
		P_list = []
		for s in strings:
			if s in keys:
				P_list.extend([P_Q.split('/')[0] for P_Q in id_nodes_dict[s]])
		P_predicts = [x[0] for x in Counter(P_list).most_common(3)] #[('P932', 8), ('P1566', 6), ('P698', 2)]
		#print('Top 3 possible properties:')
		#print(P_predicts)
		for P_predict in P_predicts:
			output = {}#key string, value:Q123
			for s in strings:
				output[s] = 'N/A'
				if s in keys:
					for P_Q in id_nodes_dict[s]: #for P_Q in P_Qlist
						P_Q_splited = P_Q.split('/')
						if P_Q_splited[0] == P_predict:
							output[s] = P_Q_splited[1]
							continue
			result.append((P_predict,output))
		return result

	def call_redis(self,qnodes):
		payload = json.dumps({"ids": qnodes})
		search_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
		r = requests.post("http://minds03.isi.edu:4444/get_identifiers",
			data=payload,headers=search_headers)
		if r:
			val = r.json()
			return val
		else:
			return {}

if __name__ == "__main__":
	test1 = ['5333265','5333264','5333267','5333266','5333261','5333260','5333263','5333262']
	test2 = ['XX1007441','XX1012281','XX1018804','XX1033111','XX1041185','XX1041305','XX1044878','XX1049656','XX1069173']
	test3 = ['0','1','1212','1323','2112','2113','212','2141','2142','2144','2145','2147','215']
	f = find_identity()
	print('Testcase1, Truth P932:')
	for idx,res in enumerate(f.get_identifier_3(test1)):
		print('Top',idx+1,res[0])
		print(res[1])
	print('-'*30)
	print('Testcase2, Truth P950')
	for idx,res in enumerate(f.get_identifier_3(test2)):
		print('Top',idx+1,res[0])
		print(res[1])
	print('-'*30)
	print('Testcase3, Truth P952')
	for idx,res in enumerate(f.get_identifier_3(test3)):
		print('Top',idx+1,res[0])
		print(res[1])
	print('-'*30)
