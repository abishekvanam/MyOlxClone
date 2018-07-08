import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link,Redirect } from "react-router-dom";
import Cookies from 'universal-cookie';

class HomeComp extends Component{

    cookies=new Cookies()

    logout = (props) =>
    {


        console.log('user token is:'+this.cookies.get('userJwtToken'));
        this.cookies.remove('userJwtToken');
        this.cookies.remove('username');
        console.log('user token after is:'+this.cookies.get('userJwtToken'));

        this.props.history.push('/');
        //<Redirect to="/home"/>

    }

    render(){
        return(

        <button type="button" className="btn btn-info" onClick={() => this.logout()}>Logout</button>

        )
    }
}



export default HomeComp;

