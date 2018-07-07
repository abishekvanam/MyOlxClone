import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Redirect} from "react-router-dom";
import './App.css';


import LoginComp from './ReactComps/auth/loginpage';
import SignUpComp from './ReactComps/auth/signuppage';

class App extends Component {
  constructor(props)
  {
    super(props);
    this.state = {isLoggedIn: false, username: "", isStaff: ""};
  }

  readCookie(name) {
    var nameEQ = name + "=";
    console.log('Cookie is  :'+document.cookie);
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

  componentWillMount()
  {
    console.log(this.readCookie("JWT"))
    if(this.readCookie("JWT")==null)
      this.setState({isLoggedIn: false, username: "", isStaff: ""})
    else
    {

        console.log('Inside will mount else!!!');
      const uname = this.readCookie("username");
      const staff = this.readCookie("isStaff");
      console.log('uname is:'+uname);
      this.setState({isLoggedIn: true, username: uname, isStaff: staff})
    }
  }

  setLoginStatus = (newStatus, newUserName, newStaffStatus) => {
    this.setState({isLoggedIn: newStatus, username: newUserName, isStaff: newStaffStatus})
  }

  render() {
    return (
      <Router>
        <div className="App">
          <div className="jumbotron">
            <Route exact path="/lol" component={args => <Redirect to="/olx/advt_list/"/>} />
            <Route exact path="/olx/login" component={args => <LoginComp isLoggedIn={this.state.isLoggedIn} setLoginStatus={this.setLoginStatus}{...args}/>} />
            <Route exact path="/" component={args => <SignUpComp isLoggedIn={this.state.isLoggedIn} setLoginStatus={this.setLoginStatus}{...args}/>} />

            </div>
        </div>
      </Router>
    );
  }
}

export default App;



//import React, { Component } from 'react';
//import logo from './logo.svg';
//import './App.css';
//
//class App extends Component {
//  render() {
//    return (
//      <div className="App">
//        <header className="App-header">
//          <img src={logo} className="App-logo" alt="logo" />
//          <h1 className="App-title">Welcome to React</h1>
//        </header>
//        <p className="App-intro">
//          To get started, edit <code>src/App.js</code> and save to reload.
//        </p>
//      </div>
//    );
//  }
//}
//
//export default App;
