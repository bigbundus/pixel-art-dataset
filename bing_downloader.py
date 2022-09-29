from bing_image_downloader import downloader
#bing-image-downloader==1.1.2


query_string = "pixel art wizard"

downloader.download(query_string,
limit=10,
output_dir='bing_output',
adult_filter_off=True,
force_replace=False,
timeout=60,
verbose=True)
