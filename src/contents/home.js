import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Layout } from 'antd';
import './css/home.css';

import { HomeMenu, MainHeader } from '../components/home';
import Dashboard from './dashboard'
import Teacher from './teachers'
import Student from './students'
import Staff from './staffs'

const { Content } = Layout;

class Home extends React.Component{
    state = {
        collapsed: true,
    };
    
    toggle = () => {
        this.setState({ collapsed: !this.state.collapsed, });
    };

    render(){
        return(
            <Router>
                <Layout className='site-background'>
                    <MainHeader collapsed={this.state.collapsed} toggle={this.toggle} history={this.props.history} />
                    <HomeMenu collapsed={this.state.collapsed} />
                    <Layout className='site-background' style={{marginLeft: this.state.collapsed?80:200, transition: '.2s'}}>

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