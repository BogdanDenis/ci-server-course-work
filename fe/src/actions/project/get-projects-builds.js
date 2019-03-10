import { RSAA } from 'redux-api-middleware';

import { saveProjectsBuilds } from './save-projects-builds';
import * as types from './types';
import { API_ENDPOINT } from '../../constants/endpoints';

export const getProjectsBuilds = (projectId) => (dispatch) => {
	dispatch({
		[RSAA]: {
			endpoint: `${API_ENDPOINT}/project/${projectId}/builds`,
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
			},
			types: [
				types.GET_PROJECTS_BUILDS_REQUEST,
				{
					type: types.GET_PROJECTS_BUILDS_SUCCESS,
					payload: (_, __, res) => {
						res.json().then(data => {
							dispatch(saveProjectsBuilds({
								id: projectId,
								builds: data,
							}));
						});
					},
				},
				types.GET_PROJECTS_BUILDS_FAILURE,
			],
		},
	});
};
