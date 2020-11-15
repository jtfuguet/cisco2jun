import sys, getopt

#function to convert each line in the source file into a juniper-compliant firewall rule
def convert(line):
	print line

if (len(sys.argv)!=3): #usage error, if num args != 3 then program was called incorrectly
	print 'Usage: cisco2jun <source_file> <dest_file>'
	quit()

print 'Num args:', len(sys.argv)
print 'Loading ACL source "', str(sys.argv[1]),'\"' 
ACLSource = open(sys.argv[1], 'r')
print 'Source loaded'

for line in ACLSource:
	convert(line)


