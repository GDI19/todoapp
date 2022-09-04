import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import LoginForm from './components/Auth.js'
import ProjectsList from './components/Projects.js'
import TodosList from './components/Todos.js'
import NotFound404 from './components/NotFound404.js'
import axios from 'axios'
import {BrowserRouter, Route, Link, Routes, Navigate} from 'react-router-dom'
import Cookies from 'universal-cookie';



class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos':[],
            'token':[]
        }
    }

    set_token(token){
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token})
    }

    is_authenticated(){
        return this.state.token != ''
    }

    logout(){
        this.set_token('')
    }

    get_token_from_storage(){
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token})
    }

    get_token(username, password){
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                // console.log(response.data)
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    load_data() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                // console.log(users)
                    this.setState(
                        {
                            'users': users
                        }
                    )
            }).catch(error => console.log(error))


        axios.get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                const projects = response.data
                    this.setState(
                        {
                            'projects': projects
                        }
                    )
            }).catch(error => console.log(error))



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

    componentDidMount() {
        this.get_token_from_storage()
        this.load_data()
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
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Routes>
                        <Route path='/' element={ <UserList users={this.state.users} />} />
                        <Route path='/projects' element={<ProjectsList projects={this.state.projects} /> } />
                        <Route path='/todos' element={<TodosList todos={this.state.todos} /> } />
                        <Route path='/login' element={ <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                        <Route path='/users' element={<Navigate replace to='/' />} />
                        <Route path='*' element={<NotFound404 />} />
                    </Routes>
                </div>
                </BrowserRouter>

        )
    }

}
export default App;