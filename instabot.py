import requests

Access_Token = '2014479056.b79054f.e93bfd8ad67448788e997ac8a25926cf'

Base_URL="https://api.instagram.com/v1"

Average_of_letters_in_comments=0

Total_length=0

#Function to Display your details
def MyInfo():
    request_url = Base_URL + "/users/self/?access_token=" + Access_Token
    my_info=requests.get(request_url).json()
    print("Full Name is " + my_info['data']['full_name'])
    print("User Name is " + my_info['data']['username'])
    print("Profile picture is " + my_info['data']['profile_picture'])
    print("Bio is " + my_info['data']['bio'])
    print("Id is " + my_info['data']['id'])
    print("The No of Followers for the user are: " + str(my_info['data']['counts']['followed_by']))
    print("The No of people which the user follows are: " + str(my_info['data']['counts']['follows']))

#Function to return the user id according to the username
def get_user_id(user_name):
    request_url = (Base_URL + "/users/search?q=%s&access_token=%s") %(user_name,Access_Token)
    user_info = requests.get(request_url).json()
    if len(user_info['data']):

        print("The User id is" + user_info['data'][0][id])
        return(user_info['data'][0]['id'])
    else:
        print("user does not exist")

#Function to calculate the post_id if the User According to the caption entered for the post
def user_recent_posts(user_name):
    user_id = get_user_id(user_name)
    request_url = (Base_URL + "/users/%s/media/recent/?access_token=%s") % (user_id, Access_Token)
    user_posts = requests.get(request_url).json()
    if len(user_posts['data']):
        text=str(input("Enter the caption for which the post id is to be calculated"))
        for i in range(len(user_posts['data'])):
            if (user_posts['data'][i]['caption']):
                if (user_posts['data'][i]['caption']['text']==text):
                    print("The post id is:" + user_posts['data'][i]['id'])
                    return(user_posts['data'][i]['id'])

    else:
        print("user does not have any post")

#Function to post a like on the user post
def like_user_post(user_name):
    post_id=user_recent_posts(user_name)
    payload={'access_token':Access_Token}
    request_url = (Base_URL + "/media/%s/likes") % (post_id)
    post_a_like=requests.post(request_url,payload).json()
    if post_a_like['meta']['code']==200:
        print("Like Successful")
    else:
        print("Try Again")

#Function to pst a comment on the user post
def comment_on_user_post(user_name):
    post_id = user_recent_posts(user_name)
    comment=str(input("Enter the comment which you want to make"))
    request_url = (Base_URL + "/media/%s/comments?") % (post_id)
    request_data = {'access_token':Access_Token,'text':comment}
    get_a_comment=requests.post(request_url,request_data).json()
    if get_a_comment['meta']['code']==200:
        print("Commented Successfully")
    else:
        print("Try Again")

#Function to return the comment id according to the word entered from the post
def return_comment_id(user_name):
    word=str(input("Enter the word for which the comment is to be searched for"))
    post_id = user_recent_posts(user_name)
    request_url = (Base_URL + "/media/%s/comments?access_token=%s") % (post_id,Access_Token)
    get_a_comment=requests.get(request_url).json()
    if get_a_comment['meta']['code'] == 200:
        for i in range(len(get_a_comment['data'])):
            if word in get_a_comment['data'][i]['text']:
                print("Comment found successfully")
                return(get_a_comment['data'][i]['id'])
        else:
            print("Comment Not Found")
    else:
        print("There was error in URL")

#Function to delete the comment according to the word
def delete_comment_according_to_the_word(user_name):
    comment_id = return_comment_id("piyush_chaturvedi1996")
    post_id = user_recent_posts(user_name)
    request_url = (Base_URL + "/media/%s/comments/%s?access_token=%s") % (post_id,comment_id,Access_Token)
    delete_a_comment=requests.delete(request_url).json()
    if delete_a_comment['meta']['code'] == 200:
        print("The Comment is deleted successfully")
    else:
        print("There was error in URL")

#Function to calculate the average no of comments in a particular post considering all the comments in that post
def function_to_calculate_average(post_id):
    list_for_comments=[]
    sum=0
    request_url = (Base_URL + "/media/%s/comments?access_token=%s") % (post_id, Access_Token)
    get_a_comment = requests.get(request_url).json()
    print(get_a_comment)
    if get_a_comment['meta']['code']==200:
        Total_length=len(get_a_comment['data'])
        for comment in range(len(get_a_comment['data'])):
            list_for_comments=get_a_comment['data'][comment]['text'].split()
            sum+=len(list_for_comments)
        Average_of_letters_in_comments=sum/Total_length
        print(Average_of_letters_in_comments)
    else:
        print("There is an error in URL")
#function_to_calculate_average("piyush_chaturvedi1996")
ans='y'
username=input("Enter the username for which the action is to be performed")
while(ans=='y'or ans=='Y'):
    print("The work which the Instabot can perform is:-")
    print("1.Get your details from Instagram")
    print("2.Get the user id of some username from Instagram")
    print("3.Get the Post ID of the recent post of the user according to the caption on the Post")
    print("4.Like a post on Instagram")
    print("5.Comment on a post on Instagram")
    print("6.Delete a comment on a post on instagram")
    print("7.Calculate the average of comments on a post")
    print("8.Exit from the Instabot")
    choice=int(input("Enter the number against the work you want to perform"))

    if choice==1:
        MyInfo()

    elif choice==2:
        get_user_id(username)

    elif choice==3:
        user_recent_posts(username)

    elif choice==4:
        like_user_post(username)

    elif choice==5:
        comment_on_user_post(username)

    elif choice==6:
        delete_comment_according_to_the_word(username)

    elif choice==7:
        posts_id = user_recent_posts(username)
        function_to_calculate_average(posts_id)

    elif choice==8:
        exit()

    else:
        print("Wrong choice entered")
    ans=str(input("Do you want to continue(y/n)"))
