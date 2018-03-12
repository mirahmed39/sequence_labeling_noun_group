def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


def is_first_word(input_file_list, current_line_index):
    # the very first line is an empty line
    if current_line_index == 0:
        return False
    else:
        # if it is a first word, then it will have an empty line 1 index before it.
        line = input_file_list[current_line_index - 1].strip('\n')
        if line == "":
            return True
    return False


def is_second_word(input_file_list, current_line_index):
    # line at index 0 is empty and index 1 is the first word, not second
    if current_line_index == 0 or current_line_index == 1:
        return False
    else:
        # if it is a second word, then it will have an empty line 2 index before it.
        line = input_file_list[current_line_index - 2].strip('\n')
        if line == "":
            return True
    return False


def is_last_word(input_file_list, current_line_index):
    # safeguard against out of range error
    if current_line_index >= len(input_file_list) - 1:
        return False
    # it if the current word is the last word then it will have an empty line on the next index
    line = input_file_list[current_line_index+1].strip('\n')
    if line == "":
        return True
    return False


def is_second_to_last_word(input_file_list, current_line_index):
    # safeguard against out of range error
    if current_line_index >= len(input_file_list) - 2:
        return False
    # if it a second to last word, then it will have an empty line two index after it.
    line = input_file_list[current_line_index+2].strip('\n')
    if line == "":
        return True
    return False


def get_next_word(input_file_list, current_line_index):
    # if the current word is the last word, we want to give the next word an "END" value
    # otherwise, we retrieve the next word based on format of the input file.
    if is_last_word(input_file_list, current_line_index):
        return "END"
    else:
        return input_file_list[current_line_index+1].strip('\n').split('\t')[0]


def get_next_pos_tag(input_file_list, current_line_index):
    # the logic here is same as the previous function "get_next_word"
    # only the value we retrieve is the next pos tag this time.
    if is_last_word(input_file_list, current_line_index):
        return "END"
    else:
        return input_file_list[current_line_index+1].strip('\n').split('\t')[1]


def get_previous_word(input_file_list, current_line_index):
    # if the current word is the first word, we want to give the previous word a "BEGIN" value
    # otherwise, we retrieve the word based on format of the input file.
    if is_first_word(input_file_list, current_line_index):
        return "BEGIN"
    else:
        return input_file_list[current_line_index-1].strip('\n').split('\t')[0]


def get_previous_pos_tag(input_file_list, current_line_index):
    # the logic here is same as the previous function "get_previous_word"
    # only the value we retrieve is the next pos tag this time.
    if is_first_word(input_file_list, current_line_index):
        return "END"
    else:
        return input_file_list[current_line_index-1].strip('\n').split('\t')[1]


def is_capital(input_file_list, current_line_index):
    # if the current word is in upper case then we give it a value "TRUE"
    # otherwise, the value is "Flase"
    word = input_file_list[current_line_index].strip('\n').split('\t')[0]
    if word[0].isupper(): # checking the first letter of the word
        return "TRUE"
    else:
        return "FALSE"


def is_previous_word_capital(input_file_list, current_line_index):
    # First we need to check if the current word is the very first word of the sentence.
    # if it is then there is no previous word and we want to give the previous word a value "FALSE"
    # otherwise we just check if the word is capital and give it an appropriate value.
    if is_first_word(input_file_list, current_line_index):
        return "False"
    else:
        word = input_file_list[current_line_index-1].strip('\n').split('\t')[0]
        if word[0].isupper(): # checking the first letter of the word
            return "TRUE"
        else:
            return "FALSE"


def is_next_word_capital(input_file_list, current_line_index):
    # First we need to check if the current word is the last word of the sentence.
    # if it is then there is no next word and we want to give the next word a value "FALSE"
    # otherwise we just check if the word is capital and give it an appropriate value.
    if is_last_word(input_file_list, current_line_index):
        return "False"
    else:
        word = input_file_list[current_line_index+1].strip('\n').split('\t')[0]
        if word[0].isupper(): # checking the first letter of the word
            return "TRUE"
        else:
            return "FALSE"


def build_training_output_line(current_word, current_pos, current_bio, next_word, next_pos, previous_word,
                                   previous_pos, current_cap, previous_cap, next_cap):
    current_word = current_word
    current_pos = 'POS=' + current_pos
    current_bio = current_bio # no suffix here like others to conform with output format.
    next_word = 'next_word=' + next_word
    next_pos = 'next_POS=' + next_pos
    previous_word = 'previous_word=' + previous_word
    previous_pos = 'previous_POS=' + previous_pos
    current_cap = 'is_current_word_capital=' + current_cap
    previous_cap = 'is_previous_word_capital=' + previous_cap
    next_cap = 'is_next_word_capital=' + next_cap

    param_list_for_training_file = [current_word, current_pos, next_word, next_pos, previous_word, previous_pos,
                                    current_cap,
                                    previous_cap, next_cap,
                                    current_bio]  # note that "current_bio" has been moved to the end so that it stay
                                    # at the end of the output line (in other words, it is the last word)
    training_output_line = '\t'.join(param_list_for_training_file)

    return training_output_line


def build_test_output_line(current_word, current_pos, next_word, next_pos, previous_word,
                               previous_pos, previous_bio, current_cap, previous_cap, next_cap):
    current_word = current_word
    current_pos = 'POS=' + current_pos
    next_word = 'next_word=' + next_word
    next_pos = 'next_POS=' + next_pos
    previous_word = 'previous_word=' + previous_word
    previous_pos = 'previous_POS=' + previous_pos
    previous_bio = 'Previous_BIO=' + previous_bio
    current_cap = 'is_current_word_capital=' + current_cap
    previous_cap = 'is_previous_word_capital=' + previous_cap
    next_cap = 'is_next_word_capital=' + next_cap

    param_list_for_test_file = [current_word, current_pos, next_word, next_pos, previous_word, previous_pos,
                                current_cap,
                                previous_cap, next_cap,
                                previous_bio]  # note that "previous bio tag" has been moved to the end so that it stay
                                # at the end of the output line (in other words, it is the last word)
    test_output_line = '\t'.join(param_list_for_test_file)

    return test_output_line


def generate_training_file(input_file):
    with open(input_file, 'r') as input_file:
        with open('training.chunk', 'w') as training_output_file:
            data = input_file.readlines()
            line_written = 0
            for index, line in enumerate(data):
                line = line.rstrip('\n')
                if line != '':
                    current_word, current_pos_tag, current_bio_tag = line.split('\t')
                    next_word = get_next_word(data, index)
                    next_pos_tag = get_next_pos_tag(data, index)
                    previous_word = get_previous_word(data, index)
                    previous_pos_tag = get_previous_pos_tag(data, index)
                    current_word_capital = is_capital(data, index)
                    previous_word_capital = is_previous_word_capital(data, index)
                    next_word_capital = is_next_word_capital(data, index)

                    training_line = build_training_output_line(current_word, current_pos_tag,
                                                                       current_bio_tag, next_word, next_pos_tag,
                                                                       previous_word, previous_pos_tag,
                                                                       current_word_capital,
                                                                       previous_word_capital, next_word_capital)
                    training_output_file.write(training_line + '\n')
                else:
                    training_output_file.write('\n')

                line_written += 1
                print(str(line_written), " lines written for training file.")


def generate_test_file(input_file):
    with open(input_file, 'r') as input_file:
        with open('test.chunk', 'w') as test_output_file:
            data = input_file.readlines()
            line_written = 0
            for index, line in enumerate(data):
                line = line.strip('\n')
                if line != '':
                    current_word, current_pos_tag = line.split('\t')
                    next_word = get_next_word(data, index)
                    next_pos_tag = get_next_pos_tag(data, index)
                    previous_word = get_previous_word(data, index)
                    previous_pos_tag = get_previous_pos_tag(data, index)
                    previous_bio_tag = "@@"
                    current_word_capital = is_capital(data, index)
                    previous_word_capital = is_previous_word_capital(data, index)
                    next_word_capital = is_next_word_capital(data, index)

                    test_line = build_test_output_line(current_word, current_pos_tag,
                                                                       next_word, next_pos_tag,
                                                                       previous_word, previous_pos_tag,
                                                                       previous_bio_tag, current_word_capital,
                                                                       previous_word_capital, next_word_capital)
                    #print(test_line)
                    test_output_file.write(test_line + '\n')
                else:
                    test_output_file.write('\n')

                line_written += 1
                print(str(line_written), " lines written for test file.")


generate_training_file('WSJ_02-21.pos-chunk')
generate_test_file('WSJ_24.pos')