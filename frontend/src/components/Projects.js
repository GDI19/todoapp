import React from 'react'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.project_name}
            </td>
            <td>
                {project.project_link}
            </td>
            <td>
                {project.project_users}
            </td>
        </tr>
    )
}

const ProjectsList = ({projects}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>
                        Project name
                    </th>
                    <th>
                        Project Link
                    </th>
                    <th>
                        Project Users
                    </th>
                </tr>
            </thead>
            <tbody>
                    {projects.map((project) => <ProjectItem project={project} />)}
            </tbody>
        </table>
    )
}

export default ProjectsList