import { RSAA } from 'redux-api-middleware';

import { saveProjectSteps } from './save-project-steps';
import * as types from './types';
import { API_ENDPOINT } from '../../constants/endpoints';

export const updateProjectSteps = (id, steps) => (dispatch) => {
	dispatch({
		[RSAA]: {
			endpoint: `${API_ENDPOINT}/project/${id}/updateSteps`,
			method: 'POST',
			body: JSON.stringify({
				steps,
			}),
			headers: {
				'Content-Type': 'application/json',
			},
			types: [
				types.UPDATE_PROJECT_STEPS_REQUEST,
				{
					type: types.UPDATE_PROJECT_STEPS_SUCCESS,
					payload: () => {
						dispatch(saveProjectSteps({
							id,
							steps,
						}));
					},
				},
				types.UPDATE_PROJECT_STEPS_FAIL,
			],
		},
	});
};
