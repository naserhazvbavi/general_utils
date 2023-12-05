def write_array_to_txt_file(filename, array):
    """
    Saves an array in a text file as 3 digits number.
    :param filename: text file name for saving the array numbers.
    :param array: an array of numbers.
    :return:
    """
    np.savetxt(filename, array, fmt="%03d")


def read_array_from_txt_file(filename):
    """
    Reads an int array from input text file.
    :param filename: text file name to read from it.
    :return: an array of integers.
    """
    return np.loadtxt(filename, np.int32)


def write_array_to_pickle_file(filename, array):
    """
    Saves an array in a binary file.
    :param filename: binary file name for saving the array.
    :param array: an array of numbers.
    :return:
    """
    output = open(filename, 'wb')
    pickle.dump(array, output)
    output.close()


def read_array_from_pickle_file(filename):
    """
    Reads an array from input binary file.
    :param filename: binary file name to read from it.
    :return: an array of integers.
    """
    pkl_file = open(filename, 'rb')
    array = pickle.load(pkl_file)
    pkl_file.close()
    return array


def read_lines_from_txt_file(filename):
    """
    Reads a text file line by line.
    :param filename: text file name to read from it.
    :return: list of lines in the input text file.
    """
    with open(filename, encoding="utf8") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    lines = [x.strip() for x in content]
    return lines


def read_all_text_from_txt_file(filename):
    """
    Reads all content of a text file.
    :param filename: text file name to read from it.
    :return: file content
    """
    with open(filename, encoding="utf8") as f:
        data = f.read().replace('\n', ' ')
    return data


def write_str_to_txt_file(filename, str, append=False):
    """
    Writes an string to a text file.
    :param filename: text file to write the str.
    :param str: string to be wrote.
    :param append: add the text to end or re-creating the file.
    :return:
    """
    mode = "w"
    if append:
        mode = "a"
    file = open(filename, mode, encoding='utf-8')
    file.write(str)
    file.close()


def remove_dir_files(dir_path):
    """
    Clears all files in a directory.
    :param dir_path: the path directory for removing the files.
    :return:
    """
    for the_file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


def remove_dir_list_files(dir_path_list):
    """
    removes all files in the directories listed in dir_path_list. If the directory doesn't exist, create it.
    :param dir_path_list: list of directory pathes.
    :return:
    """
    for dir_path in dir_path_list:
        if os.path.isdir(dir_path):
            remove_dir_files(dir_path)
        else:
            os.makedirs(dir_path)


def get_all_dirs_from_dir(dir_path):
    """
    gets all directories in given dir path with 1 depth
    :param dir_path:
    :return: list of directories in the given path
    """
    if os.path.isdir(dir_path):
        return next(os.walk(dir_path))[1]
    return []


def get_all_files_from_dir(dir_path, sort_date=True):
    """
    returns all files of the input dir, sorted based on date if sort_date switch be on.
    :param dir_path: the input dir path for extracting the files.
    :param sort_date: a switch determinig that the files be sorted based on date or not.
    :return: list of file names and full path of them in to lists.
    """
    raw_file_names = os.listdir(dir_path)
    full_file_pathes = [os.path.join(dir_path, f) for f in raw_file_names]
    if sort_date:
        full_file_pathes.sort(key=lambda x: os.path.getmtime(x))
    return raw_file_names, full_file_pathes


def copy_file_from_Source_to_destination(source_path, destination_path):
    """
    copy specified file from source path to destination path.
    :param source_path:
    :param destination_path:
    :return: None
    """
    copy(source_path, destination_path)


def copy_directory_from_Source_to_destination(src, dst, symlinks=False, ignore=None):
    """
    copy dircetory with all its files and directories from source path to destination path.
    :param src: source path.
    :param dst: destination path.
    :param symlinks:
    :param ignore:
    :return: None
    """
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            copy2(s, d)


def get_current_date_time_formatted_string():
    """
    Gets current date time in format like : 20171217_125403
    :return: formatted date time string
    """
    currentDT = datetime.datetime.now()
    return currentDT.strftime("%Y%m%d_%H%M%S")


def get_current_date_time_string():
    """
    Gets current date time in format like : 2018-01-01 21:01:35.224871
    :return: date time string
    """
    return str(datetime.datetime.now())


def find_basename_and_dirname_path(path):
    """
    Get path and return basename and dirname of path
    :param path:
    :return:
    """
    return os.path.split(path)


def find_base_and_extension_filename(filename):
    """
    Gets filename and seperate file name without extension and its extension
    :param filename:
    :return:
    """
    filename, ext = os.path.splitext(filename)
    return filename, ext[1:]


def find_subword_index_in_subwords_refrence(subword, ref_subwords):
    """
    Example :: (find_subword_index_in_subwords_refrence('نه',ref_subwords))
    find index of a subword in subword reference List
    :param subword: sample 'نه'
    :param ref_subwords: list of all subwords
    :return:
    """
    indices = [i for i, s in enumerate(ref_subwords) if subword == s]
    return indices[0]


def show_data_in_one_cluster(list):
    """
    :param list:list of in one cluster subwords (labels are based on loaded data not by subwords index)
    :return: save images as oneCluster
    """
    transform = transforms.Compose([
        transforms.Grayscale(),
        transforms.ToTensor()
    ])
