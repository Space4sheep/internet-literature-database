import { BrowserRouter } from "react-router-dom";
import { configureStore } from "@reduxjs/toolkit";
import { Provider as ReduxProvider } from "react-redux";

import { App } from "./components/App/App";
import { ErrorBoundary } from "./components/ErrorBoundary/ErrorBondary";
import { rootReducer } from "./store/rootReducer";


import './styles/index.scss';

const store = configureStore({ reducer: rootReducer });

export const Root = () => (
	<ReduxProvider store={store}>
		<BrowserRouter>
			<ErrorBoundary>
				<App/>
			</ErrorBoundary>
		</BrowserRouter>
	</ReduxProvider>
);


