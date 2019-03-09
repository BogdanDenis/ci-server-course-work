import { SAVE_PROJECTS } from './types';

export const saveProjects = projects => ({
	type: SAVE_PROJECTS,
	payload: projects,
});
