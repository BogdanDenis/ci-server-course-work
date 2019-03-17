import React, { Component } from 'react';

import { CREATE_PROJECT_ROUTE } from '../../constants/routes';
import './header.scss';

class Header extends Component {
	handleCreateProjectClick() {
		const { push } = this.props;

		push(CREATE_PROJECT_ROUTE);		
	}

	render() {
		return (
			<header className="header">
				<button
					className="btn btn-primary btn-create-project"
					onClick={() => this.handleCreateProjectClick()}
				>
					Create a project
				</button>
			</header>
		);
	}
}

export { Header };
