from django.shortcuts import render
import requests
import requests_cache
import facebook

# Create your views here.
def crawl_group(request):

    if request.method == 'POST':
        # install cache
        requests_cache.install_cache('demo_cache')

        # get query text and token from POST request
        q = request.POST['group_name']
        token = request.POST['token']

        # create object graph
        graph = facebook.GraphAPI(access_token=token, version='2.9')
        res = graph.search(type='group', q=q, fields='name,privacy,updated_time')
        data = res['data']

        # get data on next page
        try:
            next_page = res['paging']['next']
            r = requests.get(next_page)
            next_data = r.json()['data']
            if next_data:
                data += next_data
        except Exception as e:
            pass

        # add field link into data
        for d in data:
            d['link'] = 'https://www.facebook.com/groups/' + d['id']

        return render(request, 'crawl_group/crawl_group.html', {
            'data': data,
            'q': q,
            'token': token
        })

    return render(request, 'crawl_group/crawl_group.html')