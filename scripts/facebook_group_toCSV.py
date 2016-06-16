import json
# import csv
import os
import unicodecsv

def main():
  # open a file for writing
  outputFile = open('../data_samples/csv_data_sample.csv', 'wb+')

  # open file to read
  f = open('../data_samples/parsed_data_sample.json', 'r')

  count = 0
  # create the csv writer object
  csvwriter = unicodecsv.writer(outputFile)
  # write header
  csvwriter.writerow(["postId", "parentPostId", "parentCommentId","authorName","message","description","hasVideo","hasPhoto","hasEvent","hasLink","hasTags"])

  # d = json.loads(f.read())
  for line in f:
    data = json.loads(line)
    # print data["postId"]
    csvwriter.writerow([data["postId"],data["parentPostId"],data["parentCommentId"],data["authorName"],data["message"],data["description"],data["hasVideo"],data["hasPhoto"],data["hasEvent"],data["hasLink"],data["hasTags"]])

  f.close()   
  outputFile.close()

  # end main function

# Call the main function
if __name__ == '__main__' :
    main()