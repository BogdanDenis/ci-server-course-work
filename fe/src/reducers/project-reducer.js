import * as types from '../actions/project/types';

const initialState = {
	viewedProjectId: null,
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
				viewedProjectId: action.payload,
			};
		default:
			return state;
	}
};
