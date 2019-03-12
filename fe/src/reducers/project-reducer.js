import * as types from '../actions/project/types';

const initialState = {
	projects: [],
};

export const projectReducer = (state = initialState, action) => {
	switch (action.type) {
		case types.SAVE_PROJECTS:
			return {
				...state,
				projects: action.payload,
			};
		case types.SET_VIEWED_PROJECET:
			return {
				...state,
				projects: state.projects.map((project) => ({
					...project,
					_isActive: project.id === action.payload,
				})),
			};
		case types.SAVE_PROJECTS_BUILDS:
			return {
				...state,
				projects: state.projects.map((project) => {
					if (project.id !== action.payload.id) {
						return project;
					}

					return {
						...project,
						builds: action.payload.builds,
					};
				}),
			};
		case types.SAVE_PROJECT_STEPS:
			return {
				...state,
				projects: state.projects.map((project) => {
					if (project.id === action.payload.id) {
						return {
							...project,
							steps: action.payload.steps,
						};
					}

					return project;
				}),
			};
		default:
			return state;
	}
};
