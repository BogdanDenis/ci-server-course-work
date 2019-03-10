import {
	getProjects,
	getBuilds,
} from './';

export const loadBuilds = (dispatch) => dispatch(getBuilds());
