#!/usr/bin/python
#coding=utf-8

#-------------------------------------------------------
# 功能：添加Other Linker Flags
# 说明：
# 1）第一个参数为xcodeproj文件路径
# 2）第二个参数及以后参数为Flags
#-------------------------------------------------------
# 作者：dyf
# 邮箱：1659640627@qq.com
# 日期：2016/3/15
#-------------------------------------------------------

import sys

from mod_pbxproj import XcodeProject

def addOtherFlags():
	le = len(sys.argv)
	if le > 1:
		if "xcodeproj" not in sys.argv[1]:
			print "XProjAddOtherFlags: 无效的*.xcodeproj文件路径."
		else:
			if le > 2:
				pbx_path = sys.argv[1] + "/" + "project.pbxproj"
				project = XcodeProject.Load(pbx_path)
				for idx in range(2, le):
					project.add_other_ldflags(sys.argv[idx])
				project.save()
			else:
				print "XProjAddOtherFlags: 没有传入Other Linker Flags参数."
	else:
		print "XProjAddOtherFlags: 没有传入*.xcodeproj文件路径."

if __name__ == "__main__":
	addOtherFlags()
