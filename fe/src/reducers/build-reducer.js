import * as types from '../actions/build/types';

const initialState = {
	builds: [],
};

export const buildReducer = (state = initialState, action) => {
	switch (action.type) {
		case types.SAVE_BUILDS:
			return {
				...state,
				builds: action.payload,
			};
		case types.SET_ACTIVE_BUILD:
			return {
				...state,
				builds: state.builds.map((build) => ({
					...build,
					_isActive: build.id === action.payload,
				})),
			};
		default:
			return state;
	}
};
