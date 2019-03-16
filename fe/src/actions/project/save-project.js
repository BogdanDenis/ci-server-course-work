import { SAVE_PROJECT } from './types';

export const saveProject = (project) => ({
	type: SAVE_PROJECT,
	payload: project,
});

