import { Component } from "react";


	export class ErrorBoundary extends Component {

	state = {
		error: null
	}

	static getDerivedStateFromError(error) {
		return {error};
	}

	render () {
		const { children } = this.props;
		const { error } = this.state;

		if (!error) return children;

		return <div>{error.message}</div>
	}
}