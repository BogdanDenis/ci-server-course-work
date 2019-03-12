import React, { Component } from 'react';
import classnames from 'classnames';

import {
	Icon,
} from '../';
import './time-passed.scss';

class TimePassed extends Component {
	constructor(props) {
		super(props);

		this.state = {
			timePassed: '',
		};
	}

	componentDidMount() {
		const { startTime } = this.props;

		this.timerInterval = setInterval(() => {
			const now = new Date().getTime();
			const diff = now - startTime;

			let timePassed = '';

			if (diff < 60000) {
				const secondsPassed = Math.floor(diff / 1000);

				timePassed = `${secondsPassed}s`;
			} else if (diff < 60 * 60 * 1000) {
				const minutesPassed = Math.floor(diff / 60000);

				timePassed = `${minutesPassed}m`;
			} else if (diff < 24 * 60 * 60 * 1000){
				const hoursPassed = Math.floor(diff / (60 * 60 * 1000));
				const minutesPassed = Math.floor((diff - hoursPassed * 60 * 60 * 1000) / 60000);

				timePassed = `${hoursPassed}h ${minutesPassed}m`;
			} else {
				const daysPassed = Math.floor(diff / (24 * 60 * 60 * 1000));

				timePassed = `${daysPassed}d`;
			}

			this.setState({
				timePassed,
			});
		}, 500);
	}

	componentWillUnmount() {
		clearInterval(this.timerInterval);
	}

	render() {
		const {
			classes,
			startTime,
		} = this.props;
		const { timePassed } = this.state;

		return (
			<section className={classnames('time-passed', classes)} title={new Date(startTime).toLocaleString()}>
				<Icon version={5} icon="stopwatch" text={timePassed} classes='time-passed__icon'></Icon>
			</section>
		);
	}
}

export { TimePassed };
