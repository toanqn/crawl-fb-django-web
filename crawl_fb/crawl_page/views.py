from django.shortcuts import render
import requests
import requests_cache
import facebook

# Create your views here.
def crawl_page(request):

    if request.method == 'POST':
        # install cache
        requests_cache.install_cache('demo_cache')

        # get query text and token from POST request
        q = request.POST['page_name']
        token = request.POST['token']

        # create object graph
        graph = facebook.GraphAPI(access_token=token, version='2.9')
        res = graph.search(type='page', q=q, fields='name,link,fan_count,rating_count,bio,category,phone')
        data = res['data']

        # # get data on next page
        # try:
        #     next_page = res['paging']['next']
        #     r = requests.get(next_page)
        #     next_data = r.json()['data']
        #     if next_data:
        #         data += next_data
        # except Exception as e:
        #     pass

        return render(request, 'crawl_page/crawl_page.html', {
            'data': data,
            'q': q,
            'token': token
        })

    return render(request, 'crawl_page/crawl_page.html')