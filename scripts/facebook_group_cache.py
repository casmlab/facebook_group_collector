import glob, os, io, json, datetime
from configparser import ConfigParser

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

if __name__ == "__main__":
    # Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
    # tab of
    #   https://cloud.google.com/console
    # Please ensure that you have enabled the YouTube Data API for your project.
    config = ConfigParser()
    script_dir = os.path.dirname(__file__)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(script_dir, '../settings.cfg')
    config.read(config_file)
    
    # DEVELOPER_KEY = config.get('youtube', 'api_key')

    group_id = config.get('cache', 'group_id')
    group_name = config.get('cache', 'group_name')
    # max_results = int(config.get('collect', 'max_results'))
    # os.rename('../data_samples/raw_data_sample.json' , '../data_samples/raw_data_sample.json')
    data_dir = './data_samples/raw_data_sample.json'
    outfile = os.path.join(os.getcwd(), './data_samples/cached_data_sample.json')
    combine(group_id, group_name, data_dir, outfile)
