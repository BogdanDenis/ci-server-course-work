import React, { Component } from 'react';

import { LoginFormContainer } from './components/login-form/login-form-container';
import {
	Link,
} from '../../components';

import './login.scss';

class LoginPage extends Component {
	render() {
		return (
			<div className="wrapper fade-in-down login-page">
				<div className="login-form-wrapper">
					<div className="fade-in first">
						<img
							src="http://danielzawadzki.com/codepen/01/icon.svg"
							alt="User Icon"
						/>
					</div>
					<LoginFormContainer />
					<div className="login-form-footer">
						<Link
							classes={'underline-hover'}
							href={'#'}
						>Forgot Password?</Link>
					</div>
				</div>
			</div>
		);
	}
}

export { LoginPage };
