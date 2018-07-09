import React, {Component} from 'react';
import { BrowserRouter as Router, Link} from "react-router-dom";
class NavBar extends Component{
    constructor(props)
    {
        super(props);
        this.state = {
            isLoggedIn: this.props.isLoggedIn,
        }
    }

    render(){

    return(

        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <div class="container-fluid">

    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand nav_a" href="#">Brand</a>
    </div>

    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li><a href="#" class="nav_a">Link <span class="sr-only">(current)</span></a></li>
        <li><a href="#" class="nav_a">Link</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle nav_a" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#" class="nav_a">Action</a></li>
            <li><a href="#" class="nav_a">Another action</a></li>
            <li><a href="#" class="nav_a">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#" class="nav_a">Separated link</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#" class="nav_a">One more separated link</a></li>
          </ul>
        </li>
      </ul>
      <form class="navbar-form navbar-left" method="get" action="{% url 'olx:search_advt' %}">
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Search" name="search_box">
        </div>
        <button type="submit" class="btn btn-default">Submit</button>
      </form>
        {% if request.user.is_authenticated %}
        <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
          <a href="#" class="dropdown-toggle nav_a" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{request.user.username}} <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">My Profile</a></li>
            <li><a href="{% url 'olx:chat_list' %}">My Chats</a></li>
            <li><a href="#">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="{% url 'olx:logout' %}">Logout</a></li>
          </ul>
        </li>
        </ul>

        {% else %}

            <ul class="nav navbar-nav navbar-right">
            <li><a href="{% url 'olx:login' %}" class="nav_a">Login</a></li>
            <li><a href="{% url 'olx:signup' %}" class="nav_a">Signup</a></li>
            </ul>

        {% endif %}




    </div>
  </div>
</nav>


    )

    }

}


