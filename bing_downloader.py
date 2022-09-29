from bing_image_downloader import downloader
#bing-image-downloader==1.1.2

keywords = ["wizard", "fruit", "city", "dragon", "house", "landscape", "world", "woman", "man"]
appends = ["pixel art", "pixelated"]
downloads_per = 10
output_dir = "bing_output"

def bing_download(query_string, nb_images_to_download, output_dir):
    downloader.download(query_string,
    limit= nb_images_to_download,
    output_dir=output_dir,
    adult_filter_off=True,
    force_replace=False,
    timeout=60,
    verbose=False)

for kw in keywords:

    # prefix
    for app in appends:
        query = app + " " + kw
        print(query)
        bing_download(query, downloads_per, output_dir + "/" + kw)


    # suffix
    for app in appends:
        query = kw + " " + app
        print(query)
        bing_download(query, downloads_per, output_dir + "/" + kw)
