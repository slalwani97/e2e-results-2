import os, sys, json, argparse, datetime

def main():
   parser = argparse.ArgumentParser(description='cli to get the required data')
   parser.add_argument('-bn', '--buildnumber', help='It is the build number from jenkins', required=True)
   parser.add_argument('-si', '--suiteid', help='It is the suite_id to check in json', required=True) 

   args = vars(parser.parse_args())
   suite_id = args['suiteid']
   buildNumber = args['buildnumber']
   date = date = datetime.datetime.today().strftime('%Y-%m-%d')
   path = '/tmp/%s/%s/testrail/suites.json' % (date, buildNumber)

   file = open(path, 'r+')
   data = json.load(file)

   # print(data)
   # print(suite_id in data)
   
   isPresent = False

   if suite_id in data:
      isPresent = True

   print(isPresent)
   
   return isPresent

if __name__ == '__main__':
   main()
