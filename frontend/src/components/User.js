import React from 'react'


const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.e_mail}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>First name</th>
                    <th>Last Name</th>
                    <th>E-mail</th>
                </tr>
            </thead>
            <tbody>
                    {users.map((user) => <UserItem user={user} />)}
            </tbody>
        </table>
    )
}

class AppUsers extends React.Component {
    constructor(props) {
        super(props)
        this.state = { 'users': [] }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                    this.setState(
                        { 'users': users }
                    )
            }).catch(error => console.log(error))
    }
    render () {
        return ( <UserList users={this.state.users} />)
    }





export default AppUsers;