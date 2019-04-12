############Git test###########
import json
import sys


class Notebook:
	def __init__(self, path):
		
		self.path = path 

	def __getitem__(self, index):
		
		gcell = []

		with open(self.path) as notebook:
			notebook_str = notebook.read()
			notebook_json = json.loads(notebook_str)
			cells = notebook_json['cells']
			gcell.append(cells[index - 1])
			del notebook_json['cells']

		cell = {}
		cell['cells'] = gcell
		cell.update(notebook_json)
		cell_str = json.dumps(cell) 

		with open('get_cell.ipynb', 'w') as get_cell:
			get_cell.write(cell_str)

	def __add__(self, another):
		
		with open(self.path) as notebook1:
			notebook1_str = notebook1.read()
			notebook1_json = json.loads(notebook1_str)
			cells1 = notebook1_json['cells']

			del notebook1_json['cells']

		with open(another.path) as notebook2:
			notebook2_str = notebook2.read()
			notebook2_json = json.loads(notebook2_str)
			cells2 = notebook2_json['cells']

		target_cell = cells1 + cells2
		target_notebook = {}

		target_notebook['cells'] = target_cell
		target_notebook.update(notebook1_json)

		target_str = json.dumps(target_notebook)

		with open('target_notebook.ipynb', 'w') as target:
			target.write(target_str)


notebook1 = Notebook('1.ipynb')
notebook4 = Notebook('4.ipynb')

notebook4[2]
notebook1 + notebook4 



'''
#handle argument exceptions
if len(sys.argv) < 3:
	raise Exception('参数数量必须大于2')

#accept argument
notebook_path_lst = sys.argv[1:]

cells_lst = []
target_notebook = {}

#read notebook path list
try:
	for path in notebook_path_lst:
		with open(path) as notebook:
			notebook_str = notebook.read()
			notebook_json = json.loads(notebook_str)
			cells = notebook_json['cells']

			del notebook_json['cells']

			cells_lst += cells
except FileNotFoundError:
	print('输入文件未找到')
except json.decoder.JSONDecodeError:
	print('文件内容格式错误')

target_notebook['cells'] = cells_lst

#add another argument
try:
	with open(notebook_path_lst[0]) as ntb:
		ntb_str = ntb.read()
		ntb_json = json.loads(ntb_str)

		del ntb_json['cells']

		target_notebook.update(ntb_json)
except FileNotFoundError:
	print('输入文件未找到')


target_str = json.dumps(target_notebook)

with open('target_notebook.ipynb', 'w') as target:
	target.write(target_str)
'''