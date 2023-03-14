import random
MAJOR_LANGUAGE_ENCODE = {'eng': 'E', 'spa': 'S'}

def find_the_indices_longest_sequence_of_minor_language0(clean_utterance_language_labels, major_language):

    def evaluate_new_max(i, j, old_n_max, old_i_max, old_j_max):
        # print('evaluate_new_max')
        # print("i = {}, j = {}, old_n_max = {}, old_i_max = {}, old_j_max = {}".format(i, j, old_n_max, old_i_max, old_j_max))
        if old_n_max < (j - i + 1):
            # if found new max len sequence:
            new_i_max = i
            new_j_max = j
            new_n_max = j - i + 1

        else:
            new_i_max = old_i_max
            new_j_max = old_j_max
            new_n_max = old_n_max
        #print("new_i_max = {}, new_j_max = {}, new_n_max = {}".format(new_i_max, new_j_max, new_n_max))
        return new_i_max, new_j_max, new_n_max

    i_max = 0
    j_max = 0
    n_max = 0

    inside_minor = False

    for i in range(len(clean_utterance_language_labels)):
        for j in range(i, len(clean_utterance_language_labels)):
            #print("i = {}, j = {}".format(i, j))
            # current token is minor language
            if not clean_utterance_language_labels[j] == major_language:
                #print('current token is minor language')
                if not inside_minor:  # Went inside a minor sequence
                    inside_minor = True

                # if reached end with a minor language
                if j == len(clean_utterance_language_labels)-1:
                    #print('end reached with minor')
                    i_max, j_max, n_max = evaluate_new_max(i, j, n_max, i_max, j_max)

            else:  # current token is major language
                # print('current token is major language')
                if inside_minor:  # Went out of minor sequence
                    inside_minor = False
                    i_max, j_max, n_max = evaluate_new_max(i, j-1, n_max, i_max, j_max)

                else:
                    break

    print("The longest sequence of minor language tokens is " + str(n_max))
    print("first index of minor: " + str(i_max))
    print("last index of minor: " + str(j_max))


def find_the_indices_longest_sequence_of_minor_language(clean_utterance_language_labels, major_language):

    def evaluate_new_max(i, j, old_n_max, old_i_max, old_j_max):
        # print('evaluate_new_max')
        # print("i = {}, j = {}, old_n_max = {}, old_i_max = {}, old_j_max = {}".format(i, j, old_n_max, old_i_max, old_j_max))
        if old_n_max < (j - i + 1):
            # if found new max len sequence:
            new_i_max = i
            new_j_max = j
            new_n_max = j - i + 1

        else:
            new_i_max = old_i_max
            new_j_max = old_j_max
            new_n_max = old_n_max
        #print("new_i_max = {}, new_j_max = {}, new_n_max = {}".format(new_i_max, new_j_max, new_n_max))
        return new_i_max, new_j_max, new_n_max

    i_max = 0
    j_max = 0
    n_max = 0

    inside_minor = False
    i = 0
    j = 0
    while j < len(clean_utterance_language_labels):
        # print("i = {}, j = {}".format(i, j))
        # current token is minor language
        if not clean_utterance_language_labels[j] == major_language:
            # print('current token is minor language')
            if not inside_minor:  # Went inside a minor sequence
                inside_minor = True

            # if reached end with a minor language
            if j == len(clean_utterance_language_labels)-1:
                # print('end reached with minor')
                i_max, j_max, n_max = evaluate_new_max(i, j, n_max, i_max, j_max)

        else:  # current token is major language
            # print('current token is major language')
            if inside_minor:  # Went out of minor sequence
                inside_minor = False
                i_max, j_max, n_max = evaluate_new_max(i, j-1, n_max, i_max, j_max)
            else:  # major language token after major language token
                pass
            i = j+1
        j += 1

    print("The longest sequence of minor language tokens is " + str(n_max))
    print("first index of minor: " + str(i_max))
    print("last index of minor: " + str(j_max))


def test_find_the_indices_longest_sequence_of_minor_language():
    # clean_utterance_language_labels = ['eng', 'spa', 'eng']
    # clean_utterance_language_labels = ['eng', 'eng', 'spa']

    clean_utterance_language_labels = generate_random_sequence()

    major_language = MAJOR_LANGUAGE_DECODE[find_major_language(clean_utterance_language_labels)]

    print('clean_utterance_language_labels')
    print(clean_utterance_language_labels)
    print('major_language')
    print(major_language)
    find_the_indices_longest_sequence_of_minor_language(clean_utterance_language_labels, major_language)


def generate_random_sequence():
    num_of_samples = 3
    return random.choices(WELL_DEFINED_LANGUAGE_OPTIONS, weights=None, cum_weights=None, k=num_of_samples)


if __name__ == '__main__':
    num_of_trials = 5
    for _ in range(num_of_trials):
        test_find_the_indices_longest_sequence_of_minor_language()
    print("success!")