import { SAVE_BUILDS } from './types';

export const saveBuilds = builds => ({
	type: SAVE_BUILDS,
	payload: builds,
});
