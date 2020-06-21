import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Layout } from 'antd';
import './css/home.css';

import { HomeMenu, MainHeader } from '../components/home';
import Dashboard from './dashboard'
import Teacher from './teachers'
import Student from './students'
import Staff from './staffs'

const { Content, Sider } = Layout;

class Home extends React.Component{
	state = {
		collapsed: true,
		collapseWidth: 80
	};
	
	toggle = () => {
		this.setState({ collapsed: !this.state.collapsed, });
	};

	onBroken = (broken) => {
    	broken ? 
    		this.setState({collapsed: true, collapseWidth: 0})
    		: 
    		this.setState({collapseWidth: 80})
	}

	render(){
		return(
			<Router>
				<Layout className='site-background'>
					<MainHeader
						collapsed={this.state.collapsed}
						collapseWidth={this.state.collapseWidth}
						toggle={this.toggle}
						history={this.props.history}
					/>
					<Sider trigger={null} collapsible
						collapsed={this.state.collapsed}
						className='sider'
						collapsedWidth={this.state.collapseWidth}
						breakpoint='md'
						onBreakpoint={this.onBroken}
					>
						<HomeMenu/>
					</Sider>

					<Layout
						className='site-background'
						style={{marginLeft: this.state.collapsed?this.state.collapseWidth:this.state.collapseWidth===0?0:200, transition: '.2s'}}
					>
						<Content className='site-content'>
							<Switch>
								<Route path='/' exact component={Dashboard} />
								<Route path='/students' component={Student} />
								<Route path='/teachers' component={Teacher} />
								<Route path='/staffs' component={Staff} />
							</Switch>
						</Content>

					</Layout>
				</Layout>
			</Router>
		)
	}
}

export default Home;