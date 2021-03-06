# Purpose: parse all aacn raw data files into one curated file including
# post id, parent id, author name, content, meta data [has links, has events, etc]
# Author: Xi Rao
# Date: March 7, 2016
import json
import os

path = './data_samples/cached_data_sample.json'
allposts = 0
first_level_comments = 0
second_level_comments = 0
all_data = []


def grabData(f,outputFile):

  data = dict()
  # cleanData()

  message = ''  # post["message"] may be none
  description = ''
  postId = ''   # post["id"]
  parentPostId = ''   # post["id"] or 
  parentCommentId = '' 
  authorName = '' # post["from"]["name"]
  hasLink = False # post["type"] == "link" or post["attachment"]["url"]
  hasEvent = False  # post["type"] == "event"
  hasPhoto = False  # post["type"] == "photo" or post["attachment"]["media"]["image"]
  hasVideo = False  # post["type"] == "video"
  hasTags = False   # post["message_tags"] under comments

  c = json.loads(f.read())
  for post in c["data"]:
    # convert data to json
    # t = json.loads(line)
    # print t
    # grab all messages in loop

    # for post in content:
      # grab post
    global allposts
    allposts = allposts + 1
    postId = post["id"]
    authorName = post["from"]["name"]
    if post["type"] == "link":
      hasLink = True
    elif post["type"] == "event":
      hasEvent = True
    elif post["type"] == "photo":
      hasPhoto = True
    elif post["type"] == "video":
      hasVideo = True
    else:
      print("This type is status.")

    # test tags
    try:
      tags = post["message_tags"] # list
      hasTags = True
    except:
      print("no tags")
    # grab message  
    try:
      message = post["message"]
      # print message
      # add to data
      # data = data + message + '\n'
      # data.append(message)
      # allposts = allposts + 1
      # grab comments
      # try:
      #   comments = post["comments"]["data"]
      #   print "Comments exist!"
      #   for comment in comments:
      #     c = comment["message"]
      #     # data = data + c + '\n'
      #     data.append(c)
      #     allposts = allposts + 1
      # except:
      #   print "no comments"
    except:
      pass
    try:
      description = post["description"]
      
    except:
      pass

    data["postId"] = postId
    data["parentPostId"] = parentPostId
    data["parentCommentId"] = parentCommentId
    data["authorName"] = authorName
    data["message"] = message
    data["description"] = description
    data["hasVideo"] = hasVideo
    data["hasPhoto"] = hasPhoto
    data["hasEvent"] = hasEvent
    data["hasLink"] = hasLink
    data["hasTags"] = hasTags
    
    print(json.dumps(data))
    outputFile.write(json.dumps(data) + '\n')
    # cleanData()
    # all_data.append(data)
    message = ''  # post["message"] may be none
    description = ''
    # postId = ''   # post["id"]
    parentPostId = ''   # post["id"] or 
    parentCommentId = '' 
    authorName = '' # post["from"]["name"]
    hasLink = False # post["type"] == "link" or post["attachment"]["url"]
    hasEvent = False  # post["type"] == "event"
    hasPhoto = False  # post["type"] == "photo" or post["attachment"]["media"]["image"]
    hasVideo = False  # post["type"] == "video"
    hasTags = False   # post["message_tags"] under comments

    try:
      comments = post["comments"]["data"]
      print("Comments exist!")
      for comment in comments:
        # print("test in circle")
        addComments(comment, postId, outputFile)
        print("test after comment")
        global first_level_comments
        first_level_comments = first_level_comments + 1

        try:
          cs = comment["comments"]["data"]
          print("Second Comments exist!")
          for c in cs:
            addComments(c, postId, outputFile)
            global second_level_comments
            second_level_comments = second_level_comments + 1
            # first_level_comments = first_level_comments + 1
        except:
          print("no second comments")

    except:
      print("no comments")

  # txt = ''.join(data)
  # print txt
  # outputFile.write(txt.encode("utf-8"))
      # end grabData function


def addComments(comment, parent_post_id, outputFile):
  data = dict()
  message = ''  # post["message"] may be none
  description = ''
  postId = ''   # post["id"]
  parentPostId = ''   # post["id"] or 
  parentCommentId = ''
  authorName = '' # post["from"]["name"]
  hasLink = False # post["type"] == "link" or post["attachment"]["url"]
  hasEvent = False  # post["type"] == "event"
  hasPhoto = False  # post["type"] == "photo" or post["attachment"]["media"]["image"]
  hasVideo = False  # post["type"] == "video"
  hasTags = False   # post["message_tags"] under comments
  # cleanData()

  postId = comment["id"]
  parentPostId = parent_post_id
  # parentCommentId = parent_comment_id
  authorName = comment["from"]["name"]
  message = comment["message"]
  print("test in comment")
  try:
    url = comment["attachment"]["url"]
    hasLink = True
  except:
    print("no link")

  try:
    image = comment["attachment"]["media"]["image"]
    hasLink = True
  except:
    print("no photo")

  # test tags
  try:
    tags = comment["message_tags"]
    hasTags = True
  except:
    print("no tags")

  try:
    parentCommentId = comment["parent"]["id"]
  except:
    print("no parent comment id")

  data["postId"] = postId
  data["parentPostId"] = parentPostId
  data["parentCommentId"] = parentCommentId
  data["authorName"] = authorName
  data["message"] = message
  data["description"] = description
  data["hasVideo"] = hasVideo
  data["hasPhoto"] = hasPhoto
  data["hasEvent"] = hasEvent
  data["hasLink"] = hasLink
  data["hasTags"] = hasTags

  print(json.dumps(data))
  outputFile.write(json.dumps(data) + '\n')
  # all_data.append(data)
  # cleanData()
  message = ''  # post["message"] may be none
  description = ''
  postId = ''   # post["id"]
  parentPostId = ''   # post["id"] or 
  parentCommentId = '' 
  authorName = '' # post["from"]["name"]
  hasLink = False # post["type"] == "link" or post["attachment"]["url"]
  hasEvent = False  # post["type"] == "event"
  hasPhoto = False  # post["type"] == "photo" or post["attachment"]["media"]["image"]
  hasVideo = False  # post["type"] == "video"
  hasTags = False   # post["message_tags"] under comments

  # try:
  #   comments = comment["comments"]["data"]
  #   print "Comments exist!"
  #   for c in comments:
  #     addComments(c, postId, outputFile)
  #     allcomments = allcomments + 1
  # except:
  #   print ("no comments")

  # End addComments function
  

def main():
  # Main Funtion: Go through all files in the directory
  outputFile = open('./data_samples/parsed_data_sample.json', 'w+')

  # for file in os.listdir(path):
  f = open(path, 'r')
  # Iterate in one file
  grabData(f,outputFile)
  # outputFile.write(json.dumps(all_data))
  f.close()
  outputFile.close()

  print('All ' + str(allposts) + ' posts')
  print('All ' + str(first_level_comments) + ' first_level_comments')
  print('All ' + str(second_level_comments) + ' second_level_comments')

  # end main function

# Call the main function
if __name__ == '__main__' :
    main()