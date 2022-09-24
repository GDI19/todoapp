import React from 'react';


class ProjectForm extends React.Component{
    constructor(props) {
        super(props)
        this.state = {name: '', project_link:'', users: 0}
    }
    handleChange(event){
        this.setState(
            {[event.target.name]: event.target.value}
        );
    }
    handleSubmit(event){
        // this.props.get_token(this.state.login, this.state.password)
        // console.log(this.state.name)
        // console.log(this.state.users)
        this.props.createProject(this.state.name, this.state.project_link, this.state.user)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                <label for="name">Name</label>
                    <input type="text" className="form-group" name="name" placeholder="name" value={this.state.name} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                <label for="projectlink">Project link</label>
                    <input type="text" className="form-group" name="project_link" placeholder="project link" value={this.state.project_link} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                <label for="users">Users</label>
                    <input type="text" className="form-group" name="users" placeholder="users" value={this.state.users} onChange={(event)=>this.handleChange(event)} />
                </div>

                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }

}

export default ProjectForm