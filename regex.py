from enum import Enum
import re

RegexId = r"\[id(.+)\|(.+)\]"
RegexClub = r"\[club(.+)\|(.+)\]"

class Regex(Enum):
	ID = 0
	PUBLIC = 1

	@classmethod
	def getType(self, regexType) -> str:
		return [
			"id",
			"public"
		][regexType.value]

	@classmethod
	def get(self, regexType) -> str:
		return [
			RegexId,
			RegexClub
		][regexType.value]


def VK2MD(string: str) -> str:
	string = regex(Regex.ID, string)
	string = regex(Regex.PUBLIC, string)
	return string

def regex(regexType: Regex, string: str) -> str:
	matches = re.finditer(Regex.get(regexType), string, re.MULTILINE)
	
	for match in matches:
		string = string.replace(
			match.group(0),
			f"[{match.group(2)}](https://vk.com/{Regex.getType(regexType)}{match.group(1)})"
		)
		print(string)
	
	return string;