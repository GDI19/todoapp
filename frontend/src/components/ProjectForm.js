import React from 'react';


class ProjectForm extends React.Component{
    constructor(props) {
        super(props)
        this.state = { project_name: '', project_link:'', project_users: []}
    }

    handleUserChange(event){
        if(!event.target.selectedOptions){
            this.setState({
                'project_users': []
            })
            return;
        }
        let project_users = []
        for (let i=0; i<event.target.selectedOptions.length; i++ ){
            project_users.push(event.target.selectedOptions.item(i).value)
        }
        this.setState({
            'project_users': project_users
        })
    }


    handleChange(event){
        this.setState(
            {[event.target.name]: event.target.value}
        );
        // console.log(event.target.name ,event.target.value)
        // console.log(this.state.project_name)
        // console.log(this.state.project_users)
    }
    handleSubmit(event){
        // this.props.get_token(this.state.login, this.state.password)
        // console.log(this.state.project_name)
        // console.log(this.state.project_users)
        this.props.createProject(this.state.project_name, this.state.project_link, this.state.project_users)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                <label for="login">Name</label>
                    <input type="text" className="form-control" name="project_name" placeholder="name" value={this.state.project_name} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                <label for="projectlink">Project link</label>
                    <input type="text" className="form-control" name="project_link" placeholder="project link" value={this.state.project_link} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                <label for="users">Users</label>

                    <select name='project_users' multiple onChange={(event)=>this.handleUserChange(event)}>
                        {this.props.users.map((item)=><option value={item.id}>{item.username}</option>)}
                    </select>
                </div>

                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }

}

export default ProjectForm