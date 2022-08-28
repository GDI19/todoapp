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

                <tr>
                    <th>First name</th>
                    <th>Last Name</th>
                    <th>E-mail</th>
                </tr>
                {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}

export default UserList