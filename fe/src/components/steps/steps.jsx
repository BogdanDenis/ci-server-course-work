import React, { Component } from 'react';
import classnames from 'classnames';
import uuid from 'uuid/v1';

import {
	Button,
	Icon,
} from '../';
import './steps.scss';

const stepsToObjectArray = steps => {
	return steps.map((step) => ({
		id: uuid(),
		value: step,
	}));
};

class Steps extends Component {
	constructor(props) {
		super(props);

		let steps = stepsToObjectArray(props.steps);
		if (!steps.length) {
			steps = [{
				id: uuid(),
				value: '',
			}];
		}

		this.state = {
			initialSteps: stepsToObjectArray([...props.steps]),
			steps,
		};
	}

	static getDerivedStateFromProps(nextProps, prevState) {
		if (!nextProps.editMode) {
			return {
				initialSteps: stepsToObjectArray([...nextProps.steps]),
				steps: stepsToObjectArray(nextProps.steps),
			}
		}
	}

	handleStepEdit(e, id) {
		const { value } = e.target;

		this.setState({
			steps: this.state.steps.map(step => ({
				id: step.id,
				value: step.id === id ? value : step.value,
			})),
		});
	}

	handleRemoveClick(e, id) {
		e.preventDefault();
		let newSteps = this.state.steps.filter(step => step.id !== id);
		if (!newSteps.length) {
			newSteps = [{
				id: uuid(),
				value: '',
			}];
		}

		this.setState({
			steps: newSteps,
		});
	}

	handleAddClick(e, id) {
		e.preventDefault();
		this.setState({
			steps: this.state.steps.reduce((acc, cur) => {
				acc.push(cur);

				if (cur.id === id) {
					acc.push({
						id: uuid(),
						value: '',
					});
				}

				return acc;
			}, []),
		});
	}

	handleSave(e) {
		e.preventDefault();
		const {
			onStepsSave,
		} = this.props;

		const steps = this.state.steps
			.filter(step => step.value.length)
			.map(step => step.value);

		onStepsSave(steps);
	}

	handleCancel(e) {
		e.preventDefault();
		this.setState({
			steps: [...this.state.initialSteps],
		});
	}

	render() {
		const {
			classes,
			editMode,
		} = this.props;
		const { steps } = this.state;
	
		return (
			<section className={classnames('steps', classes)}>
				<h3 className="steps__heading">Steps:</h3>
				<ul className="steps__list">
					{
						steps.map((step) => {
							return (
								<li className='step'>
									{
										editMode ? (
											<div>
												<input type="text" value={step.value} onInput={e => this.handleStepEdit(e, step.id)}/>
												<Button
													classes="remove-step"
													onClick={(e) => this.handleRemoveClick(e, step.id)}
													disabled={steps.length === 0}
												>
													<Icon icon="times" version="5" />
												</Button>
												<Button classes="add-step" onClick={(e) => this.handleAddClick(e, step.id)}>
													<Icon icon="plus" version="5" />
												</Button>
											</div>
										) : (step.value)
									}
								</li>
							);
						})
					}
				</ul>
				{
					editMode ? (
						<>
							<Button classes="save btn-primary" onClick={(e) => this.handleSave(e)}>
								Save steps
							</Button>
							<Button classes="cancel btn-danger" onClick={(e) => this.handleCancel(e)}>
								Cancel
							</Button>
						</>
					) : null
				}
			</section>
		);
	}
}

export { Steps };
