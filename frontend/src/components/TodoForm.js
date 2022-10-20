import React from 'react';


class TodoForm extends React.Component{
    constructor(props) {
        super(props)
        let today = new Date()
        this.state = { todo_author: 0, todo_project: 0, todo_text: '', todo_creation_date: today, todo_updated_date: today, todo_is_active: 'True'}
    }


    handleChange(event){
        this.setState(
            {[event.target.name]: event.target.value}
        );
        // console.log('todo_author' ,this.state.todo_author)
        // console.log('todo_project', this.state.todo_project)
        // console.log('todo_text', this.state.todo_text)
        // console.log('todo_creation_date' ,this.state.todo_creation_date)
        // console.log('todo_updated_date', this.state.todo_updated_date)
        // console.log('todo_is_active', this.state.todo_is_active)

    }
    handleSubmit(event){
        // this.props.get_token(this.state.login, this.state.password)
        // console.log(this.state.project_name)
        // console.log(this.state.project_users)
        this.props.createTodo(this.state.todo_author, this.state.todo_project, this.state.todo_text, this.state.todo_creation_date, this.state.todo_updated_date, this.state.todo_is_active)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>

                <div className="form-group">
                <label for="todo_author">Author of the todo</label>
                    <select name='todo_author'  onChange={(event)=>this.handleChange(event)}>
                        {this.props.users.map((item)=><option value={item.id}>{item.username}</option>)}
                    </select>
                </div>

                <div className="form-group">
                <label for="todo_project">Project</label>
                    <select name='todo_project' onChange={(event)=>this.handleChange(event)}>
                        {this.props.projects.map((item)=><option value={item.id}>{item.project_name}</option>)}
                    </select>
                </div>

                <div className="form-group">
                <label for="todo_text">Text todo</label>
                    <input type="text" className="form-control" name="todo_text" placeholder="Text to do" value={this.state.todo_text} onChange={(event)=>this.handleChange(event)} />
                </div>


                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }

}

export default TodoForm