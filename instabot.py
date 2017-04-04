import requests
Access_Token = '2014479056.b79054f.e93bfd8ad67448788e997ac8a25926cf'
Base_URL="http://api.instagram.com/v1"



def MyInfo():
    request_url = Base_URL + "/users/self/?access_token=" + Access_Token
    my_info=requests.get(request_url).json()
    print(my_info['data']['full_name'])


def get_user_id(user_name):
    request_url = (Base_URL + "/users/search?q=%s&access_token=%s") %(user_name,Access_Token)
    user_info = requests.get(request_url).json()
    if len(user_info['data']):
        return(user_info['data'][0]['id'])
    else:
        print("user does not exist")
def user_recent_posts(user_name):
    user_id = get_user_id(user_name)
    request_url = (Base_URL + "/users/%s/media/recent/?access_token=%s") % (user_id, Access_Token)
    user_posts = requests.get(request_url).json()
    if len(user_posts['data']):
        text=str(input("Enter the caption for which the post id is to be calculated"))
        for i in range(len(user_posts['data'])):
            if (user_posts['data'][i]['caption']):
                if (user_posts['data'][i]['caption']['text']==text):
                    print("The Post id is" + user_posts['data'][i]['id'])
                    return(user_posts['data'][i]['id'])

    else:
        print("user does not exist")

def like_user_post(user_name):
    post_id=user_recent_posts(user_name)
    payload={'access_token':Access_Token}
    request_url = (Base_URL + "/media/%s/likes") % (post_id,)
    print(request_url)
    post_a_like=requests.post(request_url,payload).json()
    print(post_a_like)
    if post_a_like['meta']['code']==200:
        print(len(post_a_like['data']))
        print("Like Successful")
    else:
        print("Try Again")


like_user_post("piyushsharma576")
def comment_on_user_post(user_name):
    post_id = user_recent_posts(user_name)
    comment=str(input("Enter the comment which you want to make"))
    request_url = (Base_URL + "/media/%s/comments?") % (post_id)
    request_data = {'access_token':Access_Token,'text':comment}
    get_a_comment=requests.get(request_url,request_data).json()
    print(get_a_comment)
    if get_a_comment['meta']['code']==200:
        print("Commented Successfully")
    else:
        print("Try Again")


#comment_on_user_post("piyushsharma576")

def get_all_the_comments(user_name):
    post_id = user_recent_posts(user_name)
    request_url = (Base_URL + "/media/%s/comments?access_token=%s") % (post_id, Access_Token)
    get_a_comment = requests.get(request_url).json()
    print(get_a_comment)
    if get_a_comment['meta']['code'] == 200:
        for i in range(len(get_a_comment['data'])):
            print("The comment is made by" + get_a_comment['data'][i]['from']['username'])
            print("The comment is" + get_a_comment['data'][i]['text'])
    else:
        print("There was error in URL")
#get_all_the_comments('piyushsharma576')

def return_comment_id(user_name):
    word=str(input("Enter the word for which the comment is to be searched for"))
    post_id = user_recent_posts(user_name)
    request_url = (Base_URL + "/media/%s/comments?access_token=%s") % (post_id,Access_Token)
    get_a_comment=requests.get(request_url).json()
    if get_a_comment['meta']['code'] == 200:
        for i in range(len(get_a_comment['data'])):
            if word in get_a_comment['data'][i]['text']:
                #print("the comment id is" + get_a_comment['data'][i]['id'])
                #print("Comment found successfully")
                return(get_a_comment['data'][i]['id'])
        else:
            print("Comment Not Found")
    else:
        print("There was error in URL")


def delete_comment_according_to_the_word(user_name):
    post_id = user_recent_posts(user_name)
    comment_id=return_comment_id("user_name")
    print(comment_id)
    request_url = (Base_URL + "/media/%s/comments/%s?access_token=%s") % (post_id,comment_id,Access_Token)
    print(request_url)
    delete_a_comment=requests.delete(request_url).json()
    print(delete_a_comment['data'])
    """if delete_a_comment['meta']['code'] == 200:
        print("The Comment is deleted successfully")
    else:
        print("There was error in URL")"""


#delete_comment_according_to_the_word("piyush_chaturvedi1996")





