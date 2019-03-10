export const selectActiveBuild = state => {
	return state.build.builds.find(build => build._isActive);
};
