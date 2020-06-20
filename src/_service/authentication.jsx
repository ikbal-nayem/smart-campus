import React from 'react';
import { Redirect } from 'react-router-dom';
import { isAuthenticate } from './handler'


class Authenticate extends React.Component{
	render(){
		if(!isAuthenticate()){
			return <Redirect to='/login' />
		}
		return(
			<React.Fragment>
				{this.props.children}
			</React.Fragment>
		)
	}
}

export { Authenticate };