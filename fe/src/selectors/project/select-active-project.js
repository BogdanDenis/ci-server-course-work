export const selectActiveProject = state => {
	return state.project.projects.find(project => project._isActive);
};
