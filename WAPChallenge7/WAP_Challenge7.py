#!/usr/bin/env python

from optparse import OptionParser

use = "Usage: %prog [options] argument1 argument2"

parser = OptionParser(usage = use)

parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="Set mode to verbose.")
parser.add_option("-p", "--pcap", dest="pcap" metavar="FILE", help="pcap file location"),
parser.add_option("-pass", "--passwordfile", dest="passwordfile" metavar="FILE", help="password file location"),
