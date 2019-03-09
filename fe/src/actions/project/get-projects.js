import { RSAA } from 'redux-api-middleware';

import { saveProjects } from './save-projects';
import * as types from './types';
import { API_ENDPOINT } from '../../constants/endpoints';

export const getProjects = () => (dispatch) => {
	dispatch({
		[RSAA]: {
			endpoint: `${API_ENDPOINT}/project`,
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
			},
			types: [
				types.GET_PROJECTS_REQUEST,
				{
					type: types.GET_PROJECTS_SUCCESS,
					payload: (_, __, res) => {
						res.json().then(data => {
							dispatch(saveProjects(data));
						});
					},
				},
				types.GET_PROJECTS_FAILURE,
			],
		},
	});
};
