import json
import sys

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
