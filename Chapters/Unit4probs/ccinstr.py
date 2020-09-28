def record_user_click(index, keyword, url):
    urls = lookup(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] = entry[1]+1

def add_to_index(index, keyword, url):
    # format of index: [[keyword, [[url, count], [url, count],..]],...]
    for entry in index:
        if entry[0] == keyword:
            for urls in entry[1]:
                if urls[0] == url:
                    return
            entry[1].append([url,0])
            return
    # not found, add new keyword to index
    index.append([keyword, [[url,0]]])

