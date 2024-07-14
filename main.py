from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from dhooks import Embed, Webhook
import vk_api

import config

vk_session = vk_api.VkApi(token=config.ACCESS_TOKEN)
longpoll = VkBotLongPoll(vk_session, int(config.GROUP_ID))

webhook = Webhook(
	config.WEBHOOK_URL,
	username="Grenny",
	avatar_url="https://cdn.discordapp.com/avatars/893949906820145163/a040ef2025e373233bb3f0582916c204.webp"
)

for event in longpoll.listen():
	if event.type	== VkBotEventType.WALL_POST_NEW and event.object.post_type == 'post':
		title = str("Новый пост в группе ВКонтакте!")
		description = str(event.object.text)
		url = f"https://vk.com/club{event.group_id}?w=wall-{event.group_id}_{event.object.id}"

		mainEmbed = Embed(
			title=title,
			description=description,
			url=url,
			color=0xFFFFFF
		)

		listEmbeds = []

		for image in event.object.attachments:
			embed = Embed(color=0xFFFFFF)
			url = image.get('photo').get('orig_photo').get('url')
			embed.set_image(url)
			listEmbeds.append(embed)

		try:
			webhook.send( embeds=[ mainEmbed, *listEmbeds ] )
		except Exception:
			print(Exception)
