import { RSAA } from 'redux-api-middleware';

import { saveBuilds } from './save-builds';
import * as types from './types';
import { API_ENDPOINT } from '../../constants/endpoints';

export const getBuilds = () => (dispatch) => {
	dispatch({
		[RSAA]: {
			endpoint: `${API_ENDPOINT}/build`,
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
			},
			types: [
				types.GET_BUILDS_REQUEST,
				{
					type: types.GET_BUILDS_SUCCESS,
					payload: (_, __, res) => {
						res.json().then(data => {
							dispatch(saveBuilds(data));
						});
					},
				},
				types.GET_BUILDS_FAIL,
			],
		},
	});
};
