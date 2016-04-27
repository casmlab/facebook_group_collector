import glob, os, io, json, datetime

def saveJSONfile(outfilename, data):
    outfile = io.open(outfilename, mode='wt', encoding='utf8')
    outfile.write(json.dumps(data, ensure_ascii=False))
    outfile.flush()
    outfile.close()

def combine(group_id, name, data_dir, outfile):
    json_data = {'facebookGroupName': name, 'facebookGroupID': group_id, 'data': []}
    data = []
    page = 0
    latestPost, latestPostID = None, None
    # for f in glob.glob(os.path.join(data_dir, '*')):
    file = open(data_dir, 'r')
    c = json.loads(file.read())
    for content in c:
        # print len(content['data'])
        try:
            latest = content['data'][0]
            if latestPost == None:
                latestPost = latest['created_time']
                latestPostID = latest['id']
            else:
                if compareTimestamp(latest['created_time'], latestPost):
                    latestPost = latest['created_time']
                    latestPostID = latest['id']
            data += content['data']
            page += 1
        except:
            continue
            
    json_data['latestPost'] = latestPost
    json_data['latestPostID'] = latestPostID
    json_data['data'] = data
    print(str(page) + " pages done.")
    if data != []:
        saveJSONfile(outfile, json_data)
    else:
        print('Data not found in the given directory:' + data_dir)

def compareTimestamp(st1, st2):
    t1 = datetime.datetime.strptime(st1, "%Y-%m-%dT%H:%M:%S+0000")
    t2 = datetime.datetime.strptime(st2, "%Y-%m-%dT%H:%M:%S+0000")
    if t1 > t2:
        return True
    else:
        return False

group_id = '111111111111111'
group_name = 'asianamericanchicagonetwork'
data_dir = '../data_samples/raw_data_sample.json'
outfile = os.path.join(os.getcwd(), '../data_samples/cached_data_sample.json')
combine(group_id, group_name, data_dir, outfile)
