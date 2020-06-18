import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import LoginForm from './contents/auth/login';
import SignupForm from './contents/auth/register';
import Home from './contents/home'

function App() {
	return (
		<div className="App">
			<Router>
				<Switch>
					<Route path='/login' component={LoginForm} />
					<Route path='/register' component={SignupForm} />
					<Route path='/' exact component={Home} />
				</Switch>
			</Router>
		</div>
	);
}

export default App;
