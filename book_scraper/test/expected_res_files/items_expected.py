fill_searched_items_expected_res = [{  # 'reviews': 0,
    'rating': 4,
    'description': 'WICKED above her hipbone',
    'title': 'Sharp Objects',
    'genre': 'Mystery',
    'price': 47.82,
    'available': 20,
    'upc': 'e00eb4fd7b871a48'},
    {  # 'reviews': 1,
        'rating': 1,
        'description': 'description',
        'title': 'Objects',
        'genre': 'smt',
        'price': 40.0,
        'available': 10,
        'upc': 'eb871a48'},
    {  # 'reviews': 0,
        'rating': 5,
        'description': 'hipbone',
        'title': 'title',
        'genre': 'genre',
        'price': 50.21,
        'available': 50,
        'upc': 'e00eb4fd748'}]

filter_succs_expected_res = [
    {'available': 20, 'rating': 4, 'description': 'WICKED above her hipbone', 'title': 'Sharp Objects',
     'genre': 'Mystery', 'price': 47.82, 'upc': 'e00eb4fd7b871a48'}]

key_in_desc_expected_res = [{  # 'reviews': 0,
    'rating': 5,
    'description': 'hipbone blip',
    'title': 'title',
    'genre': 'genre',
    'price': 50.21,
    'available': 50,
    'upc': 'e00eb4fd748'}]

gen_value_expected_res = [{  # 'reviews': 1,
    'rating': 1,
    'description': 'description',
    'title': 'Objects',
    'genre': 'smt',
    'price': 40.0,
    'available': 10,
    'upc': 'eb871a48'}]

sort_succ_expected_res = [{'available': 50,
                           'rating': 5,
                           'description': 'hipbone',
                           'title': 'title',
                           'genre': 'genre',
                           'price': 50.21,
                           # 'reviews': 0,
                           'upc': 'e00eb4fd748'},
                          {'available': 20,
                           'rating': 4,
                           'description': 'WICKED above her hipbone',
                           'title': 'Sharp Objects',
                           'genre': 'Mystery',
                           'price': 47.82,
                           # 'reviews': 0,
                           'upc': 'e00eb4fd7b871a48'},
                          {'available': 10,
                           'rating': 1,
                           'description': 'description',
                           'title': 'Objects',
                           'genre': 'smt',
                           'price': 40.0,
                           # 'reviews': 1,
                           'upc': 'eb871a48'}]

print_expected_res = """{
    "available": 20, 
    "rating": 4, 
    "description": "WICKED above her hipbone", 
    "title": "Sharp Objects", 
    "price": 47.82, 
    "upc": "e00eb4fd7b871a48", 
    "genre": "Mystery"
}
{
    "available": 10, 
    "rating": 1, 
    "description": "description", 
    "title": "Objects", 
    "price": 40.0, 
    "upc": "eb871a48", 
    "genre": "smt"
}
{
    "available": 50, 
    "rating": 5, 
    "description": "hipbone", 
    "title": "title", 
    "price": 50.21, 
    "upc": "e00eb4fd748", 
    "genre": "genre"
}
"""

return_n_succ_expected_res = [
    {'available': 20, 'rating': 4, 'description': 'WICKED above her hipbone', 'title': 'Sharp '
                                                                                       'Objects',
     'genre': 'Mystery', 'price': 47.82, 'upc': 'e00eb4fd7b871a48'}]

return_n_fail_expected_res = [{
    'available': 20,
    'rating': 4,
    'description': 'WICKED above her hipbone',
    'title': 'Sharp Objects',
    'genre': 'Mystery',
    'price': 47.82,
    'upc': 'e00eb4fd7b871a48'
},
    {
        'available': 10,
        'rating': 1,
        'description': 'description',
        'title': 'Objects',
        'genre': 'smt',
        'price': 40.0,
        'upc': 'eb871a48'
    },
    {
        'available': 50,
        'rating': 5,
        'description': 'hipbone',
        'title': 'title',
        'genre': 'genre',
        'price': 50.21,
        'upc': 'e00eb4fd748'
    }]