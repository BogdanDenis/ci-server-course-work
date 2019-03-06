import { RSAA } from 'redux-api-middleware';
import { push } from 'react-router-redux';

import * as types from './types';
import { HOME_ROUTE } from '../../constants/routes';

export const loginUser = (login, password) => (dispatch) => {
	dispatch({
		[RSAA]: {
			endpoint: 'http://localhost:5000/login',
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				login,
				password,
			}),
			types: [
				types.LOGIN_REQUEST,
				{
					type: types.LOGIN_SUCCESS,
					payload: (_, __, res) => {
						res.json().then(data => {
							dispatch(push(HOME_ROUTE));
						});
					},
				},
				types.LOGIN_FAILURE,
			],
		},
	});
};
