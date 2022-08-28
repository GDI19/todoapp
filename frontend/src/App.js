import React from 'react';
import logo from './logo.svg';

import {BrowserRouter, Route, Redirect, Link, Switch} from 'react-router-dom'
import './App.css';
import UserList from './components/User.js'
import ProjectsList from './components/Projects.js'
import TodosList from './components/Todos.js'
import NotFound404 from './components/NotFound404.js'
import axios from 'axios'



// const DOMAIN = 'http://127.0.0.1:8001/api/'
// const get_url = (url) => `${DOMAIN}${url}`

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                // console.log(users)
                // console.log(typeof users)
                // console.log(Array.isArray(users))
                    this.setState(
                        {
                            'users': users
                        }
                    )
            }).catch(error => console.log(error))


        axios.get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                const projects = response.data
                // console.log(projects)
                // console.log(typeof projects)
                // console.log(Array.isArray(projects))
                    this.setState(
                        {
                            'projects': projects
                        }
                    )
            }).catch(error => console.log(error))


        axios.get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                    const todos = response.data
                    // console.log(todos)
                    // console.log(typeof todos)
                    // console.log(Array.isArray(todos))
                    this.setState(
                        {
                            'todos': todos
                        }
                    )
            }).catch(error => console.log(error))
    }

    render () {
        return(

            <BrowserRouter>
                    <div>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/todos'>Todos</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/'> <UserList users={this.state.users} /> </Route>
                        <Route exact path='/projects'> <ProjectsList projects={this.state.projects} />  </Route>
                        <Route exact path='/todos'> <TodosList todos={this.state.todos} />  </Route>
                        <Redirect from='/users' to='/' />
                        <Route component={NotFound404} />
                    </Switch>
                </div>
            </BrowserRouter>

        )
    }

}
export default App;