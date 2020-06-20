import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import { LoginForm, SignupForm } from './contents/auth';
import { Authenticate }  from './_service/authentication';
import Home from './contents/home';

function App() {
	return (
		<div className="App">
			<Router>
				<Switch>
					<Route path='/login' component={LoginForm} />
					<Route path='/register' component={SignupForm} />
					<Authenticate>
						<Route path='/' component={Home} />
					</Authenticate>
				</Switch>
			</Router>
		</div>
	);
}

export default App;
