import csv
import requests
import urllib.parse
import urllib.request
import json
import sys


'''
Query statistics such as views,likes,video titles and top comments.
on Youtube using Youtube's API.
'''


class YouCrawler:
    '''
    List of provided Youtube APIs
    Possible query types:
    videos, search, channels, playlists, playlistItems, activities
    '''
    channel_id = None
    upload_id = None
    channel_name = None

    apis = {
        'videos': 'https://www.googleapis.com/youtube/v3/videos',
        'search': 'https://www.googleapis.com/youtube/v3/search',
        'channels': 'https://www.googleapis.com/youtube/v3/channels',
        'playlists': 'https://www.googleapis.com/youtube/v3/playlists',
        'playlistItems': 'https://www.googleapis.com/youtube/v3/playlistItems',
        'activities': 'https://www.googleapis.com/youtube/v3/activities',
    }

    def __init__(self, APIkey):
        self.APIkey = APIkey

    def get_json(self, query_type, param, default=False):
        '''
        Helper method to grab JSON associated with various query_type and parameters.
        :param query_type: type of query. (refer to possible queries in apis variable)
        :param param: dictionary containing parameter:value pairs.
        :param default: boolean indicating if there are multiple parameters? (True/False)
        '''
        if default:
            url = YouCrawler.apis[query_type] + '?' + \
                urllib.parse.urlencode(param, True)
        else:
            url = YouCrawler.apis[query_type] + \
                '?' + urllib.parse.urlencode(param)

        return requests.get(url).json()

    def get_channel_id(self, channel_username, helper=False):
        '''
        Get Channel ID of a Youtube Channel with channel username.
        :param channel_name: channelName, youtube.com/channel/(BuzzFeedVideo)
        :param helper: boolean indicating if method is used as helper function. If it is, certain printed strings will be omitted.
        '''
        param = {
            'part': 'id',
            'key': self.APIkey,
            'forUsername': channel_username
        }

        json_data = self.get_json('channels', param)
        print(json_data)
        if not json_data['items']:  # If items is empty
            print("Can't find channel ID associated with username.")
            return False

        temp_channel_id = json_data['items'][0]['id']
        if temp_channel_id:
            self.channel_id = temp_channel_id
            if not helper:
                print("%s's Youtube Channel ID is found: %s\nSaving channel ID..." % (
                    channel_username, self.channel_id))
            return self.channel_id
        else:
            print("Youtube Channel ID is not found.")
            return False

    def get_channel_name(self, channel_id=None, helper=False):
        '''
        Get channel name from channel ID.
        :param channel id: If no channel_id is specified, object's channel_id variable is used.
        :param helper: boolean indicating if method is used as helper function. If it is, certain printed strings will be omitted.
        '''
        if channel_id:  # If channel_id is specified
            pass

        elif self.channel_id:
            channel_id = self.channel_id  # Else use object's channel_id.

        # Else if both channel_id is not specified and object's channel id is empty.
        elif not channel_id and not self.channel_id:
            print(
                "Please input a channel ID or search for a channel ID with the channel's username.")
            return False

        param = {
            'part': 'snippet',
            'key': self.APIkey,
            'id': channel_id
        }

        json_data = self.get_json('channels', param)
        item_type = json_data['items'][0]['kind']

        if item_type == 'youtube#channel':
            channel_name = json_data['items'][0]['snippet']['title']
            print("Channel name found: %s" % channel_name)
            print("Saving Youtube channel name...")
            self.channel_name = channel_name

    def get_upload_playlist_id(self, input=None, type="username", helper=False):
        '''
        Get playlist ID for uploads of a channel by channel_name.
        :param channel_name: channelName, youtube.com/channel/(BuzzFeedVideo)
        :type: specify type of input (username/channelID)
        :param helper: boolean indicating if method is used as helper function. If it is, certain printed strings will be omitted.
        '''

        if not input:  # If no input
            if self.channel_id:
                channel_id = self.channel_id
            elif self.channel_name:
                channel_id = self.get_channel_name(channel_id)
            else:  # If both object channel name and ID are empty.
                print("Please input or initialise Channel ID/username.")
                return

        else:
            if type == 'username':
                channel_id = self.get_channel_id(input)
            else:
                channel_id = input

        if not channel_id:
            print("please input a valid username/channel ID.")
            return False

        param = {
            'part': 'snippet,contentDetails,statistics',
            'id': self.channel_id,
            'key': self.APIkey
        }

        json_data = self.get_json('channels', param)
        self.upload_id = json_data["items"][0]['contentDetails']['relatedPlaylists']['uploads']
        print("Upload playlist id is found! : %s\nSaving upload's playlist id..." % (
            self.upload_id))

    def get_all_video_id(self, default='all_video_ids.txt'):
        '''
        Get all video ids associated with a channel's uploads (using playlistItems)
        Write results into a txt file.
        :param optional default: filepath to write to
        This method only runs if upload_id is initialised as a variable.

        '''
        if self.upload_id == None:
            print('Please input or initialise upload_id method!')
            return

        param = {
            'playlistId': self.upload_id,
            'maxResults': 50,
            'part': 'contentDetails',
            'key': self.APIkey
        }

        json_data = self.get_json('playlistItems', param)
        print(json_data)
        li_video_id = []

        total = 0
        page = 1
        i = 0

        # Nested/inner loop iterates through each playlistItem and get video id
        # Outer loop iterates through each page by:
        # - appending new nextPageToken to param
        # - request new json_data with new param
        while True:
            try:
                print('Appending result number %d' % i)
                li_video_id.append(
                    json_data['items'][i]['contentDetails']['videoId'])
                i += 1
            except IndexError:
                print(
                    'Reached end of page. Total of %d results collected on page %d' % (i, page))
                # Increment total pages by number of results found on this page.
                total += i+1
                page += 1
                i = 0
                try:
                    param['pageToken'] = json_data['nextPageToken']
                    json_data = self.get_json('playlistItems', param)
                except KeyError:
                    print('nextPageToken missing on page %d.' % page)
                    break  # exit loop

        print('Total results collated are %d, sifting through %d pages.' %
              (total, page))
        print('List of video_ids assigned to self.video_ids.')

        self.video_ids = li_video_id
        with open(default, 'w') as f:
            for line in li_video_id:
                f.write('%s\n' % line)

        return li_video_id

    # Main code.
    def process_metadata(self, li_video_ids):
        '''
        :param li_video_ids: txt file containing all video ids

        maxResults = 50, iterate each page using nextPageToken.
        part = statistics,snippet (Statistics for metadata we want, snippet for title to be appended
        alongside video ID.)

        1) Dealing with 2 data structures:
        - python list containing all the video IDs
        - dictionary to contain all the data we want (video_id: views,likes... )

        '''

        param = {
            'part': 'statistics,snippet',
            'maxResults': 50,
            'key': self.APIkey
        }

        cache_crosscheck = {}

        headers = ['title', 'description', 'views', 'likes',
                   'dislikes', 'comments', 'tags']  # 7 headers
        items = []

        total = 0

        while len(li_video_ids) != 0:
            process_ids = li_video_ids[:50]  # Can
            li_video_ids = li_video_ids[50:]
            param['id'] = ','.join(process_ids)

            json_data = self.get_json('videos', param, True)

            for i in range(json_data['pageInfo']['totalResults']):
                if json_data['items'][i]['id'] not in cache_crosscheck:
                    cache_crosscheck[json_data['items'][i]['id']] = None
                    try:
                        title = json_data['items'][i]['snippet']['title']
                    except:
                        title = ''
                        print('Title missing from %s.' %
                              json_data['items'][i]['id'])
                    try:
                        description = json_data['items'][i]['snippet']['description']
                    except:
                        description = ''
                        print('Description missing from %s.' %
                              json_data['items'][i]['id'])
                    try:
                        views = json_data['items'][i]['statistics']['viewCount']
                    except:
                        views = ''
                        print('Views missing from %s.' %
                              json_data['items'][i]['id'])
                    try:
                        likes = json_data['items'][i]['statistics']['likeCount']
                    except:
                        likes = ''
                        print('Likes missing from %s.' %
                              json_data['items'][i]['id'])
                    try:
                        dislikes = json_data['items'][i]['statistics']['dislikeCount']
                    except:
                        dislikes = ''
                        print('Dislikes missing from %s.' %
                              json_data['items'][i]['id'])
                    try:
                        comments = json_data['items'][i]['statistics']['commentCount']
                    except:
                        comments = ''
                        print('Comments missing from %s.' %
                              json_data['items'][i]['id'])
                    try:
                        tags = ','.join(
                            json_data['items'][i]['snippet']['tags'])
                    except:
                        tags = ''
                        print('Tags missing from %s.' %
                              json_data['items'][i]['id'])

                    print('Appending result number %d.' % total)
                    items.append([title, description, views,
                                  likes, dislikes, comments, tags])
                    total += 1
        print('Total number of results appended is %d' % total)
        return headers, items

    def write_data_to_csv(self, readpath, writepath, function_type=None):
        '''
        Write processed metadata to csv file.
        :readpath: path of txt files containing all video ids
        :writepath: path of csv file to write to
        :function_type: function to pass on list of video ids, default is process_metadata()

        Path of readpath must contain list of all video ids to be processed.
        '''
        if function_type == None:
            function_type = self.process_metadata

        with open(readpath, 'r', encoding='utf-8-sig') as readpath:
            # video ids contained in a list.
            li_video_ids = readpath.read().splitlines()
            print(li_video_ids)  # Line for debugging.

            with open(writepath, 'w', encoding='utf-8-sig') as writepath:
                headers, items = function_type(li_video_ids)
                # i is to be iterated to get all maxResults = 50.
                writer = csv.writer(writepath)
                writer.writerow(headers)
                for row in items:
                    writer.writerow(row)


##################
# Improvements
'''
1) Processed_ids and li_video_ids can be split better. Time complexity is O(n) for slicing list (li[:50] and li[50:])

# Extensions
1) Think of a way/data structure to hold all metadata, so we can process things like top rated, most viewed, most commented.
'''
##################
# Deprecated code

'''
#	Extension: this method's quota is too high for what we want (100 unit), better to use playlistItems (1 unit)
def process_search(self,json_data):
	headers = ['Video ID','Published At','Title','Description','Thumbnail']
	items = []
	i = 0
	while True:
		try:	
			# This block of code deals with extracting the JSON data.
			if json_data['items'][i]['id']['kind'] == 'youtube#video':
				print('Appending result number %d.'%i)
				video_id = json_data['items'][i]['id']['videoId']
				published_at = json_data['items'][i]['snippet']['publishedAt']
				title = json_data['items'][i]['snippet']['title']
				description = json_data['items'][i]['snippet']['description']
				thumbnail = json_data['items'][i]['snippet']['thumbnails']['high']['url']

				items.append([video_id,published_at,title,description,thumbnail])
				i += 1
				print(i)

			else:
				print('Skipping result %d, not a youtube video.'%i)
				i += 1
				continue

		except KeyError as k:
			print(k,'Invalid key value for result number %d.' %i)

		except IndexError as l:
			print('Reached end of page. Appended total of %d results.' % i)
			break
	return headers, items
'''

##################

if __name__ == '__main__':
    session = YouCrawler('')
    session.get_channel_id('universityofexeter')
    session.get_channel_name()
    session.get_upload_playlist_id()
    session.get_all_video_id()
    session.write_data_to_csv('all_video_ids.txt', 'exeter.csv')
