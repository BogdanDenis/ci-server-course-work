import { connect } from 'react-redux';

import { LoginForm } from './login-form';
import { loginUser } from '../../../../actions';

export const LoginFormContainer = connect(
	null,
	{
		loginUser,
	},
)(LoginForm);
