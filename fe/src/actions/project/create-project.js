import { RSAA } from 'redux-api-middleware';

import { saveProject } from './save-project';
import * as types from './types';
import { API_ENDPOINT } from '../../constants/endpoints';

export const createProject = (project) => (dispatch) => {
	dispatch({
		[RSAA]: {
			endpoint: `${API_ENDPOINT}/project`,
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(project),
			types: [
				types.CREATE_PROJECT_REQUEST,
				{
					type: types.CREATE_PROJECT_SUCCESS,
					payload: (_, __, res) => {
						res.json().then(data => {
							dispatch(saveProject(data));
						});
					},
				},
				types.CREATE_PROJECT_FAIL,
			],
		},
	});
};
