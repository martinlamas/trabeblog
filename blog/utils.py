def truncate(str, max_len=25):
    if(len(str) < 4 or len(str) <= max_len):
        return str

    return f'{str[0:max_len - 3]}...'
