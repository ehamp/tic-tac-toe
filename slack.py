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
                send_message(channel['id'], 'Sorry, another tic-tac-toe game '
											'is '
											'already in progress!')
	return None


def send_message(channel_id, message):
    slack_client.api_call(
	    "chat.postMessage",
		channel=channel_id,
		text=message,
		username='Tic Tac Toe',
		icon_emoji=':unicorn_face:'
	)


if __name__=='__main__':
	print("yo")


