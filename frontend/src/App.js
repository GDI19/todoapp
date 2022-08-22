import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import ProjectsList from './components/Projects.js'
import TodosList from './components/Todos.js'
import NotFound404 from './components/NotFound404.js'
import axios from 'axios'
import {BrowserRouter, Route, Redirect, Link, Switch} from 'react-router-dom'



class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos':[]
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                    this.setState(
                        {
                            'users': users
                        }
                    )
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                const projects = response.data
                    this.setState(
                        {
                            'projects': projects
                        }
                    )
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                const todos = response.data
                    this.setState(
                        {
                            'todos': todos
                        }
                    )
            }).catch(error => console.log(error))
    }

    render () {
        return(
            <div>
                <BrowserRouter>
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
                        <Route exact path='/' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectsList projects={this.state.projects} /> } />
                        <Route exact path='/todos' component={() => <TodosList todos={this.state.todos} /> } />
                        <Redirect from='/users' to='/' />
                        <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }

}
export default App;