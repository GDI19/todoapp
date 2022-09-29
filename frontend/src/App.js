import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import LoginForm from './components/Auth.js'
import ProjectsList from './components/Projects.js'
import TodosList from './components/Todos.js'
import ProjectForm from './components/ProjectForm.js'

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
        this.setState({'token': token}, ()=>this.load_data())
    }

    is_authenticated(){
        return this.state.token !== ''
    }

    logout(){
        this.set_token('')
    }

    get_token_from_storage(){
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, ()=>this.load_data())
    }

    get_token(username, password){
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                // console.log(response.data)
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers (){
        let headers ={ 'Content-Type': 'application/json' }
        if (this.is_authenticated()){
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    delete_project(id){
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/projects/${id}/`, {headers}).then(response => {
                //const projects = this.state.projects.filter((item)=>item.id !== id)
                //    this.setState({'projects': projects})
                this.load_data()
            }).catch(error => {
                console.log(error)
                this.setState({'projects': []})
                })

    }

    delete_todo(id){
        // console.log(id)
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/todo/${id}/`, {headers}).then(response => {
                //const projects = this.state.projects.filter((item)=>item.id !== id)
                //    this.setState({'projects': projects})
                this.load_data()
            }).catch(error => {
                console.log(error)
                this.setState({'todos': []})
                })

    }

    createProject(name, project_link, user){
        const headers = this.get_headers()
        const data = {project_name:name, project_link:project_link, project_users:user}
        axios.post(`http://127.0.01.:8000/api/projects/`, data, {headers})
            .then(response => {
                // let new_project = response.data
                // const user = this.state.users.filter((item)=> item.id === new_project.project_users)[0]
                // new_project.project_users = user
                // this.setState({projects: [...this.state.projects, new_project]})
                this.load_data()
            }).catch(error =>{
                console.log(error)
                this.setState({projects:[]})
                })
    }

    load_data() {
        const headers = this.get_headers()
        console.log(headers)
        axios.get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data
                // console.log(users)
                    this.setState(
                        {
                            'users': users
                        }
                    )
            }).catch(error => console.log(error))


        axios.get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                const projects = response.data
                // console.log(projects)
                    this.setState(
                        {
                            'projects': projects
                        }
                    )
            }).catch(error => {
                console.log(error)
                this.setState({'projects': []})
                })




        axios.get('http://127.0.0.1:8000/api/todo/', {headers})
            .then(response => {
                const todos = response.data
                    this.setState(
                        {
                            'todos': todos
                        }
                    )
            }).catch(error => {
                console.log(error)
                this.setState({'todos': []})
                })
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    render () {
        return(

                <BrowserRouter>
                <div>
                    <nav>
                        <ul>
                            <li><Link to='/'>Users</Link></li>
                            <li><Link to='/projects'>Projects</Link></li>
                            <li><Link to='/todos'>Todos</Link></li>
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Routes>
                        <Route path='/' element={ <UserList users={this.state.users} />} />
                        <Route path='/projects' element={<ProjectsList projects={this.state.projects} delete_project={(id)=>this.delete_project(id)} /> } />
                        <Route path='/projects/create' element={<ProjectForm users={this.state.users} createProject={(name, project_link, user) => this.createProject(name, project_link, user)} /> } />
                        <Route path='/todos' element={<TodosList todos={this.state.todos} delete_todo={(id)=>this.delete_todo(id)} /> } />
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