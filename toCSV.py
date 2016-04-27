import json
# import csv
import os
import unicodecsv

def main():
  # open a file for writing
  outputFile = open('csv-data-sample/data.csv', 'wb+')

  # open file to read
  f = open('parsed-data-sample/data.json', 'r')

  count = 0
  # create the csv writer object
  csvwriter = unicodecsv.writer(outputFile)
  # write header
  csvwriter.writerow(["postId", "parentPostId", "parentCommentId","authorName","message","hasVideo","hasPhoto","hasEvent","hasLink","hasTags"])

  d = json.loads(f.read())
  for data in d:
    # data = json.loads(i)
    # print data["postId"]
    csvwriter.writerow([data["postId"],data["parentPostId"],data["parentCommentId"],data["authorName"],data["message"],data["hasVideo"],data["hasPhoto"],data["hasEvent"],data["hasLink"],data["hasTags"]])

  f.close()   
  outputFile.close()

  # end main function

# Call the main function
if __name__ == '__main__' :
    main()