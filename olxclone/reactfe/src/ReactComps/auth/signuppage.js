import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Redirect} from "react-router-dom";
import Cookies from 'universal-cookie';
import './Auth.css';

class SignUpComp extends Component{

    cookies=new Cookies()

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

    readCookie(name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for(var i=0;i < ca.length;i++) {
            var c = ca[i];
            while (c.charAt(0)==' ') {
                c = c.substring(1,c.length);
            }
            if (c.indexOf(nameEQ) == 0) {
                return c.substring(nameEQ.length,c.length);
            }
        }
        return null;
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
            console.log('Inside login after signup!!!');
                this.cookies.set('userJwtToken', myJson, { path: '/',expires: new Date(Date.now()+2592000)} );
                console.log('step1')
                this.cookies.set('username',name, {path : '/', expires: new Date(Date.now()+2592000)})
                console.log('step2')
                console.log(this.cookies.get('userJwtToken'));
                this.props.setLoginStatus(true, name, "1");
                this.setState(prev => ( {buttonName : 'Logout'}));
                this.props.setLoginStatus(true, name, "1");
                console.log("Redirecting....")
            }
            else{
                alert("Invalid Credentials");
            }
        })
        .catch(e => {console.log("Error occured in fetching details..")
        });
    }

    SignUp(){
        const name = document.getElementById("usernameField").value;
        const pass = document.getElementById("passwordField").value;
        const repass = document.getElementById("Re-passwordField").value;
        const email = document.getElementById("emailFeild").value;
        const first = document.getElementById("FistName").value;
        const last = document.getElementById("LastName").value;
        if(name=="" || pass =="")
        {
            alert("username and password cannot be empty")
            return;
        }
        if(pass!=repass)
        {
            alert("passwords donot match")
            return;
        }
        const reg = /^([A-Za-z0-9_\-\-.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
        if(email != "" && !reg.test(email))
        {
            alert("Invalid email address")
            return;
        }
        const data = { username: name, password: pass, email: email, first_name: first, last_name: last}
        fetch("http://127.0.0.1:8000/olx/signup", {
                    method: 'post',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                      body: JSON.stringify(data)
            })
        .then((res) => {
            if(res.status==201)
                this.login()
            else if(res.status==400)
                alert("A user with the username already exists");
            })
    }

    render(){
        return(
        this.props.isLoggedIn?<Redirect to="/olx/logouts" />:
            <div className="olxlogin-form">
                <input className="form-control mr-sm-2" type="text" id="usernameField" placeholder="Username *"/>
                <input className="form-control mr-sm-2" type="password" id="passwordField" placeholder="Password *"/>
                <input className="form-control mr-sm-2" type="password" id="Re-passwordField" placeholder="Re-Enter password *"/>
                <input className="form-control mr-sm-2" type="text" id="FistName" placeholder="First Name"/>
                <input className="form-control mr-sm-2" type="text" id="LastName" placeholder="Last Name"/>
                <input className="form-control mr-sm-2" type="text" id="emailFeild" placeholder="Email"/>
                <button type="button" className="btn btn-info" onClick={() => this.SignUp()}>Sign Up</button>
            </div>
        )
    }
}

export default SignUpComp;