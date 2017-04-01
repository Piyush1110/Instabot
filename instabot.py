import requests
Access_Token = '2014479056.b79054f.e93bfd8ad67448788e997ac8a25926cf'
Base_URL="http://api.instagram.com/v1"



def MyInfo():
    request_url = Base_URL + "/users/self/?access_token=" + Access_Token
    my_info=requests.get(request_url).json()
    print(my_info['data']['full_name'])


def get_user_id(user_name):
    request_url = (Base_URL + "/users/search?q=%s&access_token=%s") %(user_name,Access_Token)
    print("Requesting URL from data" + request_url)
    user_info = requests.get(request_url).json()
    if len(user_info['data']):
        return(user_info['data'][0]['id'])
    else:
        print("user does not exist")
def user_recent_posts(user_name):
    user_id = get_user_id(user_name)
    request_url = (Base_URL + "/users/%s/media/recent/?access_token=%s") % (user_id, Access_Token)
    print("Requesting URL from data" + request_url)
    user_posts = requests.get(request_url).json()
    if len(user_posts['data']):
        print("Returning the post id for which the caption is some user definable text")
        text=str(input("Enter the text for which the post id is to be calculated"))
        for i in range(len(user_posts['data'])):
            if (user_posts['data'][i]['caption']):
                if (user_posts['data'][i]['caption']['text']==text):
                    print("The Post id is" + user_posts['data'][i]['id'])
                    return(user_posts['data'][i]['id'])

    else:
        print("user does not exist")
user_recent_posts("piyush_chaturvedi")



