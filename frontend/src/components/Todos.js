import React from 'react'


const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.todo_author}</td>
            <td>{todo.todo_project}</td>
            <td>{todo.todo_text}</td>
            <td>{todo.todo_creation_date}</td>
            <td>{todo.todo_updated_date}</td>
            <td>{todo.todo_is_active}</td>
        </tr>
    )
}

const TodosList = ({todos}) => {
    return (
        <table>
            <tr>
                <th>Author</th>
                <th>Project</th>
                <th>Text</th>
                <th>Creation date</th>
                <th>Updated</th>
                <th>Open/Closed</th>
            </tr>
            {todos.map((todo) => <TodoItem todo={todo} />)}
        </table>
    )
}

export default TodosList