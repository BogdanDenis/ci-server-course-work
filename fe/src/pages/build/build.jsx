import React, { Component } from 'react';

import {
	Status,
	TimePassed,
	CommitAuthor,
	Output,
} from '../../components';
import './build.scss';

class BuildPage extends Component {
	constructor(props) {
		super(props);
	}

	trySetViewedBuild() {
		this.setActiveBuildTimeout = setTimeout(() => {
			const {
				build,
				setActiveBuild,
				location,
			} = this.props;

			if (!build) {
				const buildId = location.pathname.split('/')[2];
				setActiveBuild(buildId);
				this.trySetViewedBuild();
			} else {
				clearTimeout(this.setActiveBuildTimeout);
			}
		}, 200);
	}

	componentDidMount() {
		const {
			build,
		} = this.props;

		if (!build) {
			this.trySetViewedBuild();
		}
	}

	render() {
		const {
			build,
		} = this.props;

		if (!build) {
			return null;
		}

		console.log(build);

		const {
			commitMessage,
			commitAuthor,
			commitId,
			startTime,
			endTime,
			status,
			output,
		} = build;

		return (
			<section className="build">
				<h2 className="build__message">Message: {commitMessage}</h2>
				<h3 className="build__hash">Hash: {commitId}</h3>
				<CommitAuthor author={commitAuthor} classes={'build__author'} />
				<Status status={status} showText />
				<TimePassed startTime={startTime ? startTime.$date : 0} />
				<Output text={output} />
			</section>
		);
	}
}

export { BuildPage };
