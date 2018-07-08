import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";


class ChoiceComp extends Component{
    render(){
        return(
        <React.Fragment>
            <h6><Link to={'/olx/logins/'}>Login</Link></h6>
            <h6><Link to={'/olx/signups/'}>singup</Link></h6>
            </React.Fragment>
        )
    }
}



export default ChoiceComp;

