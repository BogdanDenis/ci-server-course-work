import { SET_ACTIVE_BUILD } from './types';

export const setActiveBuild = id => ({
	type: SET_ACTIVE_BUILD,
	payload: id,
});
