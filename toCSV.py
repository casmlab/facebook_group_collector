import json
# import csv
import os
import unicodecsv

def main():
  # open a file for writing
  outputFile = open('Forms/aacn-Mar8.csv', 'wb+')

  # open file to read
  f = open('ParsedData/parsed-data-Mar8.json', 'r')

  count = 0
  # create the csv writer object
  csvwriter = unicodecsv.writer(outputFile)
  # write header
  csvwriter.writerow(["postId", "parentPostId", "parentCommentId","authorName","message","hasVideo","hasPhoto","hasEvent","hasLink","hasTags"])


  for line in f:
    data = json.loads(line)
    # print data["postId"]
    csvwriter.writerow([data["postId"],data["parentPostId"],data["parentCommentId"],data["authorName"],data["message"],data["hasVideo"],data["hasPhoto"],data["hasEvent"],data["hasLink"],data["hasTags"]])

  f.close()   
  outputFile.close()

  # end main function

# Call the main function
if __name__ == '__main__' :
    main()