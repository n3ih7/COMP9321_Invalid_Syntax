/**
 * Written by A. Hinds with Z. Afzal 2018 for UNSW CSE.
 * 
 * Updated 2019.
 */

// import your own scripts here.

// your app must take an apiUrl as an argument --
// this will allow us to verify your apps behaviour with 
// different datasets.
import * as my from './my.js';
function post_number(){
  return 50;
}
//define the number of posts
function initApp(apiUrl) {
  // your app initialisation goes here
  const signup_button = create('button', 'Sign Up', { id: 'signup', class: 'button button-secondary' });
  const signup_detial = create('div',null,{id : 'signup_detial' });
  const log_button = create('button', 'Log In', { id: 'login', class: 'button button-primary' });
  const log_detial = create('div',null,{id : 'login_detial' });
  const search_bar = create('input',null, {id :'serarch_bar' , type: 'text'});
  const feed = create('ul',null,{id : 'feed' });
  const feed_hearder = create ('div' , null ,{id : 'feed_header' });
  feed_hearder.appendChild(create ('h3','Popular posts' ,{class : 'feed-title alt-text'}));
  feed_hearder.appendChild(create ('button', 'Post',{id: 'post', class: 'button button-secondary'}));
  feed.appendChild(feed_hearder);
  //define the signup and log button
  const feed_post =create('ul',null,{id :'feed_post'});
  feed_post.appendChild(create('input', null, {id: 'post_title', type: 'text' ,placeholder: 'title'}));
  feed_post.appendChild(create('input', null, {id: 'post_text', type: 'text' ,placeholder: 'content'}));
  feed_post.appendChild(create('input', null, {id: 'post_subseddit', type: 'text' ,placeholder: 'subseddit'}));
  feed_post.appendChild(create('button', 'confirm', {id: 'post_confirm', class: 'button button-primary'}));
  feed_post.appendChild(create('button', 'cancel', {id: 'post_cancel', class: 'button button-secondary'}));
  feed_post.style.display = 'none';
  feed.appendChild(feed_post);
  //define the post function
  const feed_button_select = create ('div', null ,{id: 'feed_button_select'});
  feed_button_select.appendChild(create ('button', '1',{id: '1', class: 'button button-primary'}));
  feed_button_select.appendChild(create ('button', '2',{id: '2', class: 'button button-primary'}));
  feed_button_select.appendChild(create ('button', '3',{id: '3', class: 'button button-primary'}));
  feed_button_select.appendChild(create ('button', '4',{id: '4', class: 'button button-primary'}));
  feed_button_select.appendChild(create ('button', '5',{id: '5', class: 'button button-primary'}));
  feed_button_select.style.display = 'none';
  feed.appendChild(feed_button_select);
  //define the Pagination
  let i = 0;

  const user_profile = create('div',null, {id : 'profile',class : 'banner'});
  user_profile.appendChild(create ('h4',null,{id :'user_name'}));
  user_profile.appendChild(create ('h4',null,{id :'user_email'}));
  user_profile.appendChild(create ('h4',null,{id :'user_posts'}));
  user_profile.appendChild(create ('h4',null,{id :'user_following'}));
  //define the profile
  search_bar.setAttribute('data-id-search','');
  log_button.setAttribute('data-id-login','');
  signup_button.setAttribute('data-id-signup','');
  //define the search bar
  log_detial.appendChild(create('div' , 'Login'));
  log_detial.appendChild(create('input', null, {id: 'login_username', type: 'text' ,placeholder: 'Username'}));
  log_detial.appendChild(create('input', null, {id: 'login_password', type: 'text' ,placeholder: 'Password'}));
  log_detial.appendChild(create('button' , 'login' , { id: 'loginButton' , class: 'button button-primary'}));
  log_detial.appendChild(create('button' , 'cancel' , { id: 'logincancelButton' , class: 'button button-secondary'}));
  log_detial.appendChild(create('div',null ,{id :'log_token' }));
  signup_detial.appendChild(create('div' , 'register'));
  signup_detial.appendChild(create('input', null, {id: 'signup_username', type: 'text' ,placeholder: 'Username'}));
  signup_detial.appendChild(create('input', null, {id: 'signup_password', type: 'text' ,placeholder: 'Password'}));
  signup_detial.appendChild(create('input', null, {id: 'signup_email', type: 'text' ,placeholder: 'email'}));
  signup_detial.appendChild(create('input', null, {id: 'signup_name', type: 'text' ,placeholder: 'name'}));
  signup_detial.appendChild(create('button' , 'signup' , { id: 'signupButton' , class: 'button button-primary'}));
  signup_detial.appendChild(create('button' , 'cancel' , { id: 'signupcancelButton' , class: 'button button-secondary'}));  
  //define the detial about log and signup
  header.appendChild(signup_button);
  header.appendChild(signup_detial);
  header.appendChild(search_bar);
  header.appendChild(log_button);
  header.appendChild(log_detial);
  header.appendChild(user_profile);
  log_detial.style.display = 'none';
  signup_detial.style.display = 'none';
  document.getElementById("root").appendChild(header);
  document.getElementById("root").appendChild(feed);
  document.getElementById("signup").addEventListener("click" , function(){
    document.getElementById("signup").style.display = 'none';
    document.getElementById("signup_detial").style.display = 'block';
  })
  document.getElementById("signupcancelButton").addEventListener("click" ,function(){
    document.getElementById("signup").style.display = 'block';
    document.getElementById("signup_detial").style.display = 'none';
  })
  document.getElementById('signupButton').addEventListener("click" ,function(){
    signup(document.getElementById("signup_username").value , document.getElementById("signup_password").value , 
    document.getElementById("signup_email").value , document.getElementById("signup_name").value);
  })
  document.getElementById("login").addEventListener("click" , function(){
    document.getElementById("login").style.display = 'none';
    document.getElementById("login_detial").style.display = 'block';
  })
  document.getElementById("logincancelButton").addEventListener("click" ,function(){
    document.getElementById("login").style.display = 'block';
    document.getElementById("login_detial").style.display = 'none';
  })
  document.getElementById('loginButton').addEventListener("click" ,function(){
   login(document.getElementById("login_username").value , document.getElementById("login_password").value);
  })
  document.getElementById('post').addEventListener ("click" ,function(){
    if((document.getElementById("log_token").value)){
      document.getElementById('feed_post').style.display = 'block';
      document.getElementById('post').style.display = 'none';
    }    
  })
document.getElementById('post_cancel').addEventListener("click",function(){
  document.getElementById('feed_post').style.display = 'none';
  document.getElementById('post').style.display = 'block';
})
document.getElementById('post_confirm').addEventListener("click" , function(){
  console.log(document.getElementById('post_title').value);
  if (document.getElementById('post_image').value == ''){
    document.getElementById('post_image').value == "";
  }
  post(document.getElementById('post_title').value , document.getElementById('post_text').value ,
  document.getElementById('post_subseddit').value ,document.getElementById('post_image').value);
})
}





function create(tag, data, options = {}) {
  const elements = document.createElement(tag);
  elements.textContent = data; 
  return Object.entries(options).reduce(
      (element, [field, value]) => {
          element.setAttribute(field, value);
          return element;
      }, elements);
}
// Basic function of create a elements (learn from web)
export default initApp;
