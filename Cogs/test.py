from google_images_search import GoogleImagesSearch
import bpy

gis = GoogleImagesSearch('AIzaSyCwFVDYXihj2SC1wji3QlY464vM1lv51g8', '77f01332c891ebbec')

_search_params = {
    'q': 'waifu',
    'num': 10,
    'fileType': 'jpg|gif|png',
    }

results = []

for i in range(0, 10):
    results.append(gis.search(search_params=_search_params))
    imgage_object = bpy.data.images.load(results[i])

