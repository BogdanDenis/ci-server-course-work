import { RSAA } from 'redux-api-middleware';
import { push } from 'react-router-redux';

import * as types from './types';
import { PROJECTS_ROUTE } from '../../constants/routes';
import { API_ENDPOINT } from '../../constants/endpoints';

export const loginUser = (login, password) => (dispatch) => {
	dispatch({
		[RSAA]: {
			endpoint: `${API_ENDPOINT}/login`,
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
							dispatch(push(PROJECTS_ROUTE));
						});
					},
				},
				types.LOGIN_FAILURE,
			],
		},
	});
};
