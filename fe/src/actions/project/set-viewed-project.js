import { SET_VIEWED_PROJECET } from './types';

import { getProjectsBuilds } from './get-projects-builds';

const setViewedProject = id => dispatch => {
	dispatch({
		type: SET_VIEWED_PROJECET,
		payload: id,
	});

	dispatch(getProjectsBuilds(id));
};

export { setViewedProject };
