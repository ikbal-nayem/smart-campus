import React from 'react';
import { Link } from 'react-router-dom';
import { Menu } from 'antd';
import {
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined,
} from '@ant-design/icons';
import './css/home-menu.css'



const HomeMenu = () =>{

    return(
        <React.Fragment>
            <div className="logo" />
            <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
                <Menu.Item key="1" icon={<UserOutlined />}>
                <Link to="/dashboard">Dashboard</Link>
                </Menu.Item>
                <Menu.Item key="2" icon={<VideoCameraOutlined />}>
                <Link to="/students">Students</Link>
                </Menu.Item>
                <Menu.Item key="3" icon={<UploadOutlined />}>
                <Link to="/teachers">Teachers</Link>
                </Menu.Item>
                <Menu.Item key="4" icon={<UploadOutlined />}>
                <Link to="staffs">Staffs</Link>
                </Menu.Item>
                <Menu.Item key="5" icon={<UploadOutlined />}>
                Exams
                </Menu.Item>
            </Menu>
        </React.Fragment>
    )
}

export {HomeMenu};