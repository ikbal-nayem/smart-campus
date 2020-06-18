import React from 'react';
import { Menu, Layout } from 'antd';
import {
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined,
} from '@ant-design/icons';
import './css/home-menu.css'

const { Sider } = Layout

const HomeMenu = ({ collapsed }) =>{
    return(
        <Sider trigger={null} collapsible collapsed={collapsed} className='sider' >
            <div className="logo" />
            <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
                <Menu.Item key="1" icon={<UserOutlined />}>
                nav 1
                </Menu.Item>
                <Menu.Item key="2" icon={<VideoCameraOutlined />}>
                nav 2
                </Menu.Item>
                <Menu.Item key="3" icon={<UploadOutlined />}>
                nav 3
                </Menu.Item>
            </Menu>
        </Sider>
    )
}

export default HomeMenu;