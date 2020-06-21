import React from 'react';
import { Layout, Button } from 'antd';
import { logout } from '../../_service'
import {
    MenuUnfoldOutlined,
    MenuFoldOutlined
} from '@ant-design/icons';
import './css/header.css'

const { Header } = Layout;

const MainHeader = ({ collapsed, collapseWidth, toggle, history }) =>{
    return(
        <Header className='header' style={{paddingLeft: collapsed?collapseWidth:200, transition: '.2s'}}>
            {React.createElement(collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, {
            className: 'trigger',
            onClick: toggle,
            })}
            <Button type='link' onClick={()=>{logout(history)}}>Logout</Button>
        </Header>
    )
}


export {MainHeader};