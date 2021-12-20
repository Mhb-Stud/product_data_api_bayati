<pre>
an api for processing product information 
there are four main routes in my app admin/ api/ user/ shop/

admin/ is for admin tasks!

api/ is for connecting to crawler and exchanging data

user/                                       route is for user authentication, user register and all user related actions
user/auth/token/                            is for login and getting jwt access key
user/auth/registration/                     is for sign up in the api
user/auth/token/refresh/                    is for extending the authentication period
user/products/                              is for the user to see all of his products if he is also a vendor else it returnes an empty list
user/photo/                                 is for the user to upload a photo to be set as their profile picture you should provide the image url in the post request

shop/                                       this route is for the shop it self or general public and not vendors
shop/products/                              it returns all the products in the database
shop/products/{product_id}/get_product/     it returns the product matching the product_id in the database it also increments product number_of_views in the backend
</pre>
