import { Route, Routes } from 'react-router-dom';

import { HomePage } from '../../pages/HomePage/HomePage';
import { AuthPage } from '../../pages/AuthPage/AuthPage';
import './App.scss';

export const App = () => {
	return (
		<div className="app">
			<Routes>
				<Route path='/' element={<HomePage/>}/>

				<Route path='/auth' element={<AuthPage/>}/>
			</Routes>
		</div>
	)
}