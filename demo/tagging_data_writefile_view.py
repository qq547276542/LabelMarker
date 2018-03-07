# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
import random

##  先将标注写入文件，之后跳转到tagging_cache.html再进行新页面的跳转
def tagging_push(request):
	ctx = {}
	# 先将已有的labels存入字典中
	file_object = open('label_data/labeled_data.txt','r')
	s = set()
	for f in file_object:
		pair = f.strip().split()
		curs = ""
		for i in range(1,len(pair)):
			if i>1 :
				curs += ' '
			curs += str(pair[i])
		s.add(curs.strip())
	
	file_object.close()
	
	file_object = open('label_data/unlabeled_data.txt','r')
	all_list = []
	for f in file_object:
		all_list.append(f.strip())
	ln = len(all_list)
	next_title = all_list[random.randint(0,ln-1)]
	
	if 'label' in request.GET and 'title' in request.GET:
		print(str(request.GET)+".....")
		title = str(request.GET['title']).strip()
		label = str(request.GET['label']).strip()
		if label != None:
			file_object = open('label_data/labeled_data.txt','a')
			if title in s:
				print("该title已存在，冲突！")
			else:
				file_object.write(label+" "+title+"\n")
				s.add(title)
			file_object.close()
		else:
			print('用户未选择label')
	
	if len(s) >= len(all_list) :
		return render(request, "over.html", ctx)	
		
	while next_title in s:  # 如果冲突就再选
		next_title = all_list[random.randint(0,ln-1)].strip()
		
	ctx['next'] = "<input id='next' value='" + next_title + "' style='display:none;'></input>"
		
			
	return render(request, "tagging_cache.html", ctx)

