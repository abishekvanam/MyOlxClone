import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Redirect} from "react-router-dom";
import Cookies from 'universal-cookie';
import './Auth.css';

class LoginComp extends Component{
    cookies = new Cookies();
    createCookie(name,value,days) {
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 *1000));
            var expires = "; expires=" + date.toGMTString();
        }

        else {
            var expires = "";
        }
        document.cookie = name + "=" + value + expires + "; path=/";
    }

    login(){
        const name = document.getElementById("usernameField").value;
        const pass = document.getElementById("passwordField").value;
        fetch('http://127.0.0.1:8000/api-token-auth/', {
            method: 'post',
            headers: {
                "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            },
            body: `username=${name}&password=${pass}`
            }).then(function(response) {
            return response.json();
        })
        .then((myJson) => {
            if ('token' in myJson){
                this.cookies.set('userJwtToken', myJson, { path: '/',expires: new Date(Date.now()+2592000)} );
                this.cookies.set('username',name, {path : '/', expires: new Date(Date.now()+2592000)})
                console.log(this.cookies.get('userJwtToken'));
                this.props.setLoginStatus(true, name, "1");
                this.setState(prev => ( {buttonName : 'Logout'}));
                console.log("Redirecting....")
            }
            else{
                alert("Invalid Credentials");
            }
        })
        .catch(e => {console.log("Error occured in fetching details..")
        });
    }
//        }).then(res => {
//            if(res.status==400)
//            {
//                alert("Invalid details")
//            }
//            else
//            {
//                res.json()
//                .then(response => {
//                    this.createCookie("JWT", response.token, 1);
//                    this.createCookie("username", name);
//                    fetch("http://127.0.0.1:8000/olx/user_permissions", {headers: {
//                        'Authorization': "JWT "+response.token
//                      }
//                    })
//                .then(res =>{
//                    if(res.status==403)
//                    {
//                        this.props.setLoginStatus(true, name, "0");
//                    }
//                    else
//                    {
//                        this.props.setLoginStatus(true, name, "1");
//                    }
//                })
//                })
//            }
//        });
//    }

    render(){
        return(
        this.props.isLoggedIn?<Redirect to="/olx/logouts"/>:
        <div>
            <div className="olxlogin-form">
                <input className="form-control mr-sm-2" type="text" id="usernameField" placeholder="username"/>
                <input className="form-control mr-sm-2" type="password" id="passwordField" placeholder="password"/>
                <button type="button" className="btn btn-info" onClick={() => this.login()}>Login</button>
            </div>
        </div>
        )
    }
}

export default LoginComp;






