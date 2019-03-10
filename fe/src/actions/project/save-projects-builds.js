import { SAVE_PROJECTS_BUILDS } from './types';

export const saveProjectsBuilds = data => ({
	type: SAVE_PROJECTS_BUILDS,
	payload: data,
});
