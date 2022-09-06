#!/usr/bin/python3

import sys
import re
import logging
import os

pattern = re.compile(r'^\[Switching to Thread 0x[0-9a-f]+ \(LWP (?P<LWPID>[0-9]+)\)]')
DIRECTORY = "./LWP"

class Spooler:
    def __init__(self, path):
        self.msg = ""
        self.path = path
        self.lwp_no = "0000"

    def spool(self):
        with open(path, "r") as f:
            for line in f:
                m = pattern.search(line)
                if m:
                    yield (self.lwp_no, self.msg)
                    self.lwp_no =  m.group("LWPID")
                    self.msg = ""
                self.msg += line

class DrawGraph:
    def __init__(self):
        self.header = "digraph {"
        self.rankdir = "rankdir = LR;"
        self.tail = "}"
        self.edges = {}
        self.indent = 0
        self.sep = " " * 4

        self.dest_pattern = re.compile("^#0  (?P<FN>[a-z][a-z0-9\_A-Z]+) ")
        self.src_pattern = re.compile("^#1  0x[0-9a-f]+ in (?P<FN>[a-z][a-z0-9\_A-Z]+) ")

    def get_edges_from_section(self, lwp, msg):
        dest = None
        src = None
        if not (lwp in self.edges):
            self.edges[lwp] = {}

        for line in msg.split("\n"):
            m = self.dest_pattern.search(line)
            if m:
                dest = m.group("FN")
            m = self.src_pattern.search(line)
            if m:
                if dest:
                    src = m.group("FN")
                else:
                    dest = None
            if src and dest:
                self.edges[lwp][src] = dest

    def ingest(self, path):
        p = Spooler(path)
        for lwp, msg in p.spool():
            self.get_edges_from_section(lwp, msg)

    def get_indent(self):
        return self.sep * self.indent

    def print(self, f, line):
        f.write("%s%s" % (self.get_indent(), line))

    def dump_subgraph(self, lwp, edges):
        filename = "%s/%s_subgraph.dot" % (DIRECTORY, lwp)
        with open(filename, "a") as f:
            self.print(f, self.header)
            self.indent += 1
            self.print(f, "%s" % (self.rankdir))
            for k,v in edges.items():
                self.print(f, "%s -> %s;" % (k, v))
            self.indent -= 1
            self.print(f, "}")
        svg_filename = "%s/%s_subgraph.svg" % (DIRECTORY, lwp)
        os.system("dot -T svg %s -o %s; rm -f %s" % (filename, svg_filename, filename))

    def dump(self):
        for lwp, edges in self.edges.items():
            self.dump_subgraph(lwp, edges)

    def spool(self, path):
        self.ingest(path)
        self.dump()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: %s LOGFILE" % sys.argv[0])
        sys.exit(1)
    path = sys.argv[1]
    g = DrawGraph()
    g.spool(path)

