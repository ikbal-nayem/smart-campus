import React from 'react';
import { Layout } from 'antd';
import './css/home.css';

import HomeMenu from '../components/home/home-menu';
import MainHeader from '../components/home/header';

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
            <Layout className='site-background'>
                <MainHeader collapsed={this.state.collapsed} toggle={this.toggle} />
                <HomeMenu collapsed={this.state.collapsed} />
                <Layout className='site-background' style={{marginLeft: this.state.collapsed?80:200, transition: '.2s'}}>

                    <Content className='site-content'>
                        Content<br/>
                        Content<br/>
                        Content<br/>
                        Content<br/>
                        Content<br/>
                        Content<br/>
                        Content<br/>
                        Content<br/>
                    </Content>

                </Layout>
            </Layout>
        )
    }
}

export default Home;