import { SET_VIEWED_PROJECET } from './types';

const setViewedProject = id => ({
	type: SET_VIEWED_PROJECET,
	payload: id,
});

export { setViewedProject };
