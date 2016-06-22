#!/usr/bin/python3.5 -tt
import sys

def Hello(nam):

  if nam == 'Alice':
    nam = nam + '????'
  else:
  	print 'Else'
  nam = nam + '!!!!'
  print 'Hello', nam
	


def main():
  Hello(sys.argv[1])
 	
if __name__ == '__main__':
  main()

