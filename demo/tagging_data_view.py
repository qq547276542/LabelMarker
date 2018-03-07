# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf

# 数据标注页面的view
# 接收GET请求数据
def showtagging_data(request):
	ctx = {}
	if 'title' in request.GET:
		ctx['title'] = str(request.GET['title'])
		## 动态生成check控件----------------------------------
		
		text = ""
		tag_name_list = []
		file_object = open('label_data/label_list.txt','r')
		for f in file_object:
			tag_name_list.append(f.strip())
		file_object.close()
				
		count = 0
		for tag in tag_name_list:
			text += '<div class="radio"> <label class="form-check-label">'
			text += '<input type="radio" name="label" value="' + str(tag) + '">'
			text +=  str(tag)
			text += '</label>  </div>'
			count += 1
			
		# 放置一个隐藏的输入框，传递title的值到缓冲页面
		text += "<input name='title' value='" + str(request.GET["title"]) + "'  style='display:none;' ></input>"
		
		ctx['taggingCheck'] = text
		
		# 统计当前标注情况
		file_object = open('label_data/labeled_data.txt','r')
		s = {}
		sum = 0
		LEN = len(tag_name_list)
		for i in tag_name_list:
			s[i] = 0
		for f in file_object:
			pair = f.split()
			s[pair[0].strip()] += 1
		for i in tag_name_list:	
			sum += s[i]
		file_object.close()
		text = "" ##用于记录已标注样本个数
		for i in tag_name_list:
			text += '<p>label ' + str(i) + ': ' + str(s[i]) + '</p>'
		text += '<p>Sum: ' + str(sum) + '</p>'
		ctx['already'] = text

				
	return render(request, "tagging_data.html", ctx)
	