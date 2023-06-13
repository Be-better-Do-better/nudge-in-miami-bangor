from Auxiliaries.utils import WELL_DEFINED_LANGUAGE_OPTIONS


def extract_raw_languages_probabilities(list_language_tags_sequences: list[list[str]]) -> dict:
	language_tag_probabilities = None  # output init

	frequency_of_language_tags_dict = {}
	for lang in WELL_DEFINED_LANGUAGE_OPTIONS:
		frequency_of_language_tags_dict[lang] = 0

	total_num_of_tags = 0
	for single_dialogue_language_tags in list_language_tags_sequences:
		for language_tag in single_dialogue_language_tags:
			frequency_of_language_tags_dict[language_tag] += 1
			total_num_of_tags += 1

	if total_num_of_tags > 0:
		language_tag_probabilities = {}
		for lang in WELL_DEFINED_LANGUAGE_OPTIONS:
			language_tag_probabilities[lang] = frequency_of_language_tags_dict[lang] / total_num_of_tags

	return language_tag_probabilities
