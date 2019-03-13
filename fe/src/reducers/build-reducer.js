import * as types from '../actions/build/types';
import * as wsTypes from '../constants/ws-message-types';

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
		case wsTypes.NEW_OUTPUT_LINE:
			return {
				...state,
				builds: state.builds.map((build) => ({
					...build,
					output: build.id === action.payload.buildId ?
						build.output + `\r\n${action.payload.line}`
						:
						build.output,
				})),
			};
		case wsTypes.BUILD_STATUS_CHANGE:
			return {
				...state,
				builds: state.builds.map((build) => ({
					...build,
					status: build.id === action.payload.buildId ?
						action.payload.status : build.status
				})),
			};
		case wsTypes.NEW_BUILD_STARTED:
			return {
				...state,
				builds: [...state.builds, action.payload.build],
			};
		default:
			return state;
	}
};
