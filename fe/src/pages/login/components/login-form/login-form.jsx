import React, { Component } from 'react';

import './login-form.scss';

class LoginForm extends Component {
	constructor(props) {
		super(props);

		this.state = {
			email: '',
			password: '',
		};
	}

	setEmail(email) {
		this.setState({
			email,
		});
	}

	setPassword(password) {
		this.setState({
			password,
		});
	}

	handleSubmit(e) {
		e.preventDefault();

		console.log(this.state);

		this.props.loginUser(this.state.email, this.state.password);
	}

	render() {
		return (
			<form onSubmit={(e) => this.handleSubmit(e)}>
				<input
					type="email"
					className="fade-in second"
					name="login"
					placeholder="login"
					onChange={(e) => this.setEmail(e.target.value)}
				/>
				<input
					type="password"
					className="fade-in third"
					name="login"
					placeholder="password"
					onChange={(e) => this.setPassword(e.target.value)}
				/>
				<input
					type="submit"
					className="fade-in fourth"
					value="Log In"
					onClick={(e) => this.handleSubmit(e)}
				/>
			</form>
		);
	}
}

export { LoginForm };
