import React from 'react'
import {Link} from 'react-router-dom';

const ProjectItem = ({project, delete_project}) => {
    return (
        <tr>
            <td>{project.project_name}</td>
            <td>{project.project_link}</td>
            <td>{project.project_users}</td>
            <td><button onClick={()=>delete_project(project.id)} type='button'>Удалить</button></td>
        </tr>
    )
}

const ProjectsList = ({projects, delete_project}) => {
    return (
        <div>
        <table>
            <thead>
                <tr>
                    <th>Project name</th>
                    <th>Project link</th>
                    <th>Project Users</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                    {projects.map((project) => <ProjectItem project={project} delete_project={delete_project}/>)}
            </tbody>
        </table>
        <Link to='/projects/create'>Создать проект</Link>
        </div>
    )
}

export default ProjectsList;