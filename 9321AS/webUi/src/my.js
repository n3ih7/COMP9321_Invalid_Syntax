
import backend from './backend_url.js'
//get api address
export function signup(signup_username, signup_password, signup_email, signup_name) {
    return API('auth/signup', {
      method: "POST",
      body: JSON.stringify({
        "username": signup_username,
        "password": signup_password,
        "email": signup_email,
        "name": signup_name,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
}
// funtion to connect signup api
export function vote(token,id){
  return API('post/vote/' + '?id='+id ,{
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      'Authorization' : `Token ${token}`
  } 
  });
}

//function to connect vote api

export function login(login_username, login_password) {
  return API('auth/login', {
    method: "POST",
    body: JSON.stringify({
      "username": login_username,
      "password": login_password,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });
}
//function to connect login api

export function feed_public() {
  return API('post/public');
}
export function feed_user(token,p,n){
  return API('user/feed',{
    method: "GET",
    headers: {
      'Authorization' : `Token ${token}`
  }
  });

}
//function to connect feed api

export function user_profile(token){
  return API('user/',{
    method: "GET",
    headers: {
      'Authorization' : `Token ${token}`
  } 
  });
}
//function to connect user api

export function user_Upvotes(token,username,id){
  return API('user/' + '?username='+username + '&id=' +id,{
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      'Authorization' : `Token ${token}`
  } 
  });
}
//function to connect other user api

export function make_commen(token,comment,id){
  return API('post/comment/' + '?id=' +id,{
    method: "PUT",
    body: JSON.stringify({
      "comment": comment,
    }),
    headers: {
      "Content-Type": "application/json",
      'Authorization' : `Token ${token}`
  } 
  });
}
//function to connect comment api

export function user_post(title, text,subseddit,image,token) {
  return API('post/', {
    method: "POST",
    body: JSON.stringify({
      "title": title,
      "text": text,
      "subseddit" :subseddit,
      "image": image,
    }),
    headers: {
      "Content-Type": "application/json",
      'Authorization' : `Token ${token}`
    },
  });
}
//function to connect post api

export function API(path, options) {
return fetch(backend +'/'+ path, options)
    .then(result => {
    return result;
    })
}
//function of connection api