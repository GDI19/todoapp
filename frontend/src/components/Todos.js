import React from 'react'
import {Link} from 'react-router-dom';

const TodoItem = ({todo, delete_todo}) => {
    return (

        <tr>
            <td>{todo.todo_author}</td>
            <td>{todo.todo_project}</td>
            <td>{todo.todo_text}</td>
            <td>{todo.todo_creation_date}</td>
            <td>{todo.todo_updated_date}</td>
            <td>{todo.todo_is_active}</td>
            <td><button onClick={()=>delete_todo(todo.id)} type='button'>Снять задачу</button></td>
        </tr>
    )
}

const TodosList = ({todos, delete_todo}) => {
    return (
        <div>
            <table>
                <thead>
                    <tr>
                        <th>Author</th>
                        <th>Project</th>
                        <th>Text</th>
                        <th>Creation date</th>
                        <th>Updated</th>
                        <th>Open/Closed</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                        {todos.map((todo) => <TodoItem todo={todo} delete_todo={delete_todo}/>)}
                </tbody>
            </table>
            <Link to='/todos/create'>Создать пометку</Link>
        </div>
    )
}

export default TodosList;