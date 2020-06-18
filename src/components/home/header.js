import React from 'react';
import { Layout } from 'antd';
import {
    MenuUnfoldOutlined,
    MenuFoldOutlined
} from '@ant-design/icons';
import './css/header.css'

const { Header } = Layout;

const MainHeader = ({ collapsed, toggle }) =>{
    return(
        <Header className='header' style={{paddingLeft: collapsed?80:200, transition: '.2s'}}>
            {React.createElement(collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, {
            className: 'trigger',
            onClick: toggle,
            })}
            <p>Logout</p>
        </Header>
    )
}


export default MainHeader;