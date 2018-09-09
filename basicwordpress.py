from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

wp = Client('http://yourwordpress.com/xmlrpc.php', 'username', 'password') #add your wordpress website, username and password
client = wp

filename="yourjpgimage.jpg" #add the path to the jpg you want to load

# prepare metadata
data = {
    'name': 'picture.jpg',
    'type': 'image/jpeg',  # mimetype
    }


with open(filename, 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())

response = client.call(media.UploadFile(data))
# response == {
#       'id': 6,
#       'file': 'picture.jpg'
#       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
#       'type': 'image/jpeg',
# }

#print (response)
testing1234 =raw_input("hit enter when ready")
attachment_id = response['id']



post = WordPressPost()

post.thumbnail = attachment_id
post.title = "some title" #add some title text here
post.content = "some content" # add some context text here
post.comment_status = 'open' #turn on comments or closed for off

post.terms_names = {
    #'post_tag': ['blog'], #add your tags
    'category': ['blog'] #add your category
    }

#publish or draft draft is the default
#post.post_status = 'publish'
wp.call(NewPost(post))
print ("new post, posted")
