import os
os.chdir('../..')
from Classes.language_usage_data import LanguageUsageData
from Classes.utterance import Utterance
from Classes.token import Token
from Auxiliaries.artificial_generation import generate_utterance

utterance = generate_utterance()

language_usage_data = LanguageUsageData(utterance.tokens)
major_lang = language_usage_data.select_major_lang()
minor_lang = language_usage_data.select_minor_lang()
print(utterance)
print("Major Lang:" + major_lang)
print("Minor Lang:" + minor_lang)
for token in utterance.tokens:
	print(token, token.lang)

utterance = Utterance(speaker='NET',tokens=[])

language_usage_data = LanguageUsageData(utterance.tokens)
major_lang = language_usage_data.select_major_lang()
minor_lang = language_usage_data.select_minor_lang()
print(utterance)
print("Major Lang:" + str(major_lang))
print("Minor Lang:" + str(minor_lang))
for token in utterance.tokens:
	print(token.surface + ': ' + str(token.lang))

print(language_usage_data)