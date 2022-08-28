import React from 'react';
import logo from './logo.svg';
import './App.css';
import AppUsers from './components/User.js'
import ProjectsList from './components/Projects.js'
import TodosList from './components/Todos.js'
import NotFound404 from './components/NotFound404.js'
import axios from 'axios'
import {BrowserRouter, Route, Link, Routes, Navigate} from 'react-router-dom'



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
                    <Routes>
                        <Route path='/' element={ <AppUsers />} />
                        <Route path='/projects' element={() => <ProjectsList projects={this.state.projects} /> } />
                        <Route path='/todos' element={() => <TodosList todos={this.state.todos} /> } />
                        <Route path='/users' element={<Navigate replace to='/' />} />
                        <Route path='*' element={<NotFound404 />} />
                    </Routes>
                </div>
                </BrowserRouter>

        )
    }

}
export default App;