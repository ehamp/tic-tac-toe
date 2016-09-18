import os
from slackclient import SlackClient

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
slack_client = SlackClient(SLACK_TOKEN) 

def message_game_state():
    channels = slack_client.api_call("channels.list")
    if channels.get('ok'):
        for channel in channels['channels']:
            if channel['name'] == 'test':
                # check conditions, send correct message depending on game state
                send_message(channel['id'], 'this is a test')
	return None


def send_message(channel_id, message):
    slack_client.api_call(
	    "chat.postMessage",
		channel=channel_id,
		text=message,
		username='Tic Tac Toe',
		icon_emoji=':unicorn_face:'
	)

def channel_info(channel_id):
    channel_info = slack_client.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None


if __name__=='__main__':
	#channels=list_channels()
	#if channels:
	#	for c in channels:
	#		if c['name'] == 'test':
	#			send_message(c['id'], board_state((c['id'])))
	#			detailed_info = channel_info(c['id'])
    #        	if detailed_info:
    #            	print(detailed_info['latest']['text'])
	#else:
	print("cant auth")


