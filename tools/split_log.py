#!/usr/bin/python3

import sys
import re
import logging

pattern = re.compile(r'^\[Switching to Thread 0x[0-9a-f]+ \(LWP (?P<LWPID>[0-9]+)\)]')
DIRECTORY = "./LWP"

class LogFiles:
	def __init__(self):
		self.logfiles = {}

	def get_logfile(self, lwp_no):
		if not(lwp_no in self.logfiles):
			filename = "%s/%s.log" % (DIRECTORY, lwp_no)
			logging.info("filename: ", filename)
			f = open(filename, "a+")
			self.logfiles[lwp_no] = f
		return self.logfiles[lwp_no]

	def spool(self, lwp_no, msg):
		f = self.get_logfile(lwp_no)
		f.write(msg)
		f.flush()

class Spooler:
	def __init__(self):
		self.logfiles = LogFiles()
		self.msg = ""
		self.lwp_no = "0000"

	def spool(self):
		for line in sys.stdin:
			m = pattern.search(line)
			if m:
				self.logfiles.spool(self.lwp_no, self.msg)
				self.lwp_no = m.group("LWPID")
				self.msg = ""
			self.msg += line

if __name__ == "__main__":
	p = Spooler()
	p.spool()

