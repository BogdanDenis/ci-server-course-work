import { SAVE_PROJECT_STEPS } from './types';

export const saveProjectSteps = (payload) => ({
	type: SAVE_PROJECT_STEPS,
	payload,
});
