from django.shortcuts import render
import requests
from datetime import datetime

headers = {
    'Authorization': 'Bearer 5',
    'Accept': 'application/json'
}

def getResponse(response):
    if response.status_code == 200:
        return True, response.json()
    else:
        return False, f'{response.status_code}: {response.reason}'

def getBlogs():
    url =   'https://blogger.googleapis.com/v3/users/op/blogs'

    response = requests.get(url, headers=headers)

    isSuccess, data = getResponse(response)

    blogs = {}

    if isSuccess:
        for blog in data['items']:
            blogs[blog['name']] = blog['id']
            
    return blogs

def dashboard(request):
    return render(request, 'blogger_apiv3/dashboard.html')

def createPage(request):
    if request.method == 'POST':
        blogId = request.POST.get("blogId")

        data = {
            "title": request.POST.get("title"),
            "content": request.POST.get("content"),
        }

        url =   'https://blogger.googleapis.com/v3/blogs/' + blogId + '/pages'

        response = requests.post(url, headers=headers, json=data)

        isSuccess, message = getResponse(response)

        return render(request,'blogger_apiv3/createPage.html', {'isSuccess': isSuccess, 'message': message, 'blogs': getBlogs()})

    return render(request, 'blogger_apiv3/createPage.html', {'blogs': getBlogs()})

def createPost(request):
    if request.method == 'POST':
        blogId = request.POST.get("blogId")

        data = {
            "title": request.POST.get("title"),
            "content": request.POST.get("content"),
        }

        url =   'https://blogger.googleapis.com/v3/blogs/' + blogId + '/posts'

        response = requests.post(url, headers=headers, json=data)

        isSuccess, message = getResponse(response)

        return render(request,'blogger_apiv3/createPost.html', {'isSuccess': isSuccess, 'message': message, 'blogs': getBlogs()})

    return render(request, 'blogger_apiv3/createPost.html', {'blogs': getBlogs()})

def listBlogs(request):
    url =   'https://blogger.googleapis.com/v3/users/op/blogs'

    response = requests.get(url, headers=headers)

    isSuccess, data = getResponse(response)

    allBlogs = []
    count = 0

    if isSuccess:
        for blog in data['items']:        
            tempBlog = dict()
            tempBlog['id'] = blog['id']
            tempBlog['name'] = blog['name']
            tempBlog['noOfPages'] = blog['pages']['totalItems']
            tempBlog['noOfPosts'] = blog['posts']['totalItems']
            tempBlog['publishDate'] = datetime.strptime(blog['published'][0:19], "%Y-%m-%dT%H:%M:%S").date()
            tempBlog['status'] = blog['status']
            tempBlog['url'] = blog['url']
            allBlogs.append(tempBlog)
            count += 1
        data = allBlogs

    return render(request,'blogger_apiv3/listBlogs.html', {'isSuccess': isSuccess, 'data': data, 'count': count})

def listPages(request):
    if request.method == 'POST':
        blogId = request.POST.get("blogId")

        url =   'https://blogger.googleapis.com/v3/blogs/' + blogId + '/pages'

        response = requests.get(url, headers=headers)

        isSuccess, data = getResponse(response)
        
        allPages = []
        count = 0

        if isSuccess:
            for page in data['items']:        
                tempPage = dict()
                tempPage['id'] = page['id']
                tempPage['blogId'] = page['blog']['id']
                tempPage['publishDate'] = datetime.strptime(page['published'][0:19], "%Y-%m-%dT%H:%M:%S").date()
                tempPage['title'] = page['title']
                tempPage['url'] = page['url']
                allPages.append(tempPage)
                count += 1
            data = allPages

        return render(request,'blogger_apiv3/listPages.html', {'isSuccess': isSuccess, 'data': data, 'count': count})

    return render(request, 'blogger_apiv3/listPages.html', {'blogs': getBlogs()})

def listPosts(request):
    if request.method == 'POST':
        blogId = request.POST.get("blogId")
        
        url =   'https://blogger.googleapis.com/v3/blogs/' + blogId + '/posts'

        response = requests.get(url, headers=headers)

        isSuccess, data = getResponse(response)
        
        allPosts = []
        count = 0

        if isSuccess:
            for post in data['items']:        
                tempPost = dict()
                tempPost['id'] = post['id']
                tempPost['blogId'] = post['blog']['id']
                tempPost['publishDate'] = datetime.strptime(post['published'][0:19], "%Y-%m-%dT%H:%M:%S").date()
                tempPost['title'] = post['title']
                tempPost['commentCount'] = post['replies']['totalItems']
                tempPost['url'] = post['url']
                allPosts.append(tempPost)
                count += 1
            data = allPosts

        return render(request,'blogger_apiv3/listPosts.html', {'isSuccess': isSuccess, 'data': data, 'count': count})
    
    return render(request, 'blogger_apiv3/listPosts.html', {'blogs': getBlogs()})

def userProfile(request):
    url =   'https://blogger.googleapis.com/v3/users/op'
        
    response = requests.get(url, headers=headers)

    isSuccess, data = getResponse(response)

    user = dict()

    if isSuccess:    
        user['id'] = data['id']
        user['name'] = data['displayName']
        user['about'] = data['about']
        user['url'] = data['url']
        user['creationDate'] = datetime.strptime(data['created'][0:19], "%Y-%m-%dT%H:%M:%S").date()
        user['country'] = data['locale']['country'] if data['locale']['country'] else '-'
        user['language'] = data['locale']['language']
        user['languageVariant'] = data['locale']['variant'] if data['locale']['variant'] else '-'
        data = user 

    return render(request, 'blogger_apiv3/userProfile.html', {'isSuccess': isSuccess, 'data': data})