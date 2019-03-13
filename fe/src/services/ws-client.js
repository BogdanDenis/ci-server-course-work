import { WS_SERVER } from '../constants/endpoints';

export const WsClient = () => (dispatch) => {
	const socket = new WebSocket(WS_SERVER);

	socket.addEventListener('open', () => {});

	socket.addEventListener('message', (event) => {
		const action = JSON.parse(event.data);

		dispatch(action);
	});
};
