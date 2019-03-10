import { RSAA } from 'redux-api-middleware';

import { getProjectsBuilds } from './';
import * as types from './types';
import { API_ENDPOINT } from '../../constants/endpoints';

export const rebuildProject = (id) => (dispatch) => {
	dispatch({
		[RSAA]: {
			endpoint: `${API_ENDPOINT}/project/${id}/rebuild`,
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			types: [
				types.REBUILD_PROJECT_REQUEST,
				{
					type: types.REBUILD_PROJECT_SUCCESS,
					payload: (_, __, res) => {
						dispatch(getProjectsBuilds(id));
					},
				},
				types.REBUILD_PROJECT_FAIL,
			],
		},
	});
};
